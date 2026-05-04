"""
Deterministic token-similarity clustering for batch packing.

Goal: when handing N entities to an LLM in batches of size B, ensure that
entities sharing surface-variant or head-noun similarity end up in the SAME
batch — so the model sees the full set of candidates for a merge decision.

No embeddings, no LLM. Pure token analysis:
  1. Each name is reduced to a token signature: lowercased, hyphen-normalized,
     filler-suffix stripped (ability/capability/capacity/skill, singular and
     plural), simple-pluralized, with synonym verbs collapsed
     (comprehension/awareness → understanding) and morphology folded
     (logical→logic, mathematical→math, multi/cross/x-modal → multimodal).
  2. Two entities are linked if EITHER:
       - identical token signature → same surface concept (Reasoning vs
         Reasoning capabilities), OR
       - same head noun (last content token after normalization) → same
         thematic family (Reasoning vs Mathematical reasoning).
  3. Union-find clusters all linked entities together.
  4. Clusters are packed into batches with first-fit-decreasing: large
     clusters first, fitting smaller clusters into remaining space. Clusters
     bigger than batch_size are split into multiple batches but stay
     contiguous.

The output is a list of batches; each batch is a list of indices into the
original `nodes` list. The aggregator can iterate these batches directly.
"""

from __future__ import annotations

import re
from collections import defaultdict
from typing import Iterable, List, Sequence


# ── Token normalization ──────────────────────────────────────────────────────

_UNICODE_HYPHENS = "\u2010\u2011\u2012\u2013\u2014\u2015\u2212"

_FILLER_TOKENS = {
    "ability", "abilities",
    "capability", "capabilities",
    "capacity", "capacities",
    "skill", "skills",
    "proficiency", "proficiencies",
    "performance",
}

_STOPWORDS = {"a", "an", "the", "of", "to", "for", "in", "on", "with", "by", "and", "or"}

_SYNONYM_REPLACE = {
    "comprehension": "understanding",
    "awareness": "understanding",
    "identification": "recognition",
    "logical": "logic",
    "numerical": "numeric",
    "mathematical": "math",
}


def _stem_plural(word: str) -> str:
    if len(word) > 3 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 3 and word.endswith("ses"):
        return word[:-2]
    if len(word) > 1 and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def _normalize_to_tokens(name: str) -> List[str]:
    """Return the ordered list of content tokens for a name."""
    if not name:
        return []
    s = name.strip().lower()
    for uh in _UNICODE_HYPHENS:
        s = s.replace(uh, "-")
    # Treat hyphens, slashes, underscores as spaces. Drop other punctuation.
    s = re.sub(r"[-_/]", " ", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    # Collapse "multi modal" / "cross modal" / "x modal" → "multimodal"
    s = re.sub(r"\b(multi|cross|x)\s+modal\b", "multimodal", s)
    # Collapse "vis(io|ual) linguistic" → "vision language"
    s = re.sub(r"\b(visio|visual)\s+linguistic\b", "vision language", s)
    raw_tokens = [t for t in s.split() if t]
    out: List[str] = []
    for t in raw_tokens:
        if t in _STOPWORDS or t in _FILLER_TOKENS:
            continue
        # Stem plurals
        t = _stem_plural(t)
        # Synonym/morphology folding
        t = _SYNONYM_REPLACE.get(t, t)
        out.append(t)
    return out


def signature(name: str) -> str:
    """Order-independent normalized signature — entities sharing this signature
    are surface variants of the same concept."""
    return " ".join(sorted(set(_normalize_to_tokens(name))))


def head_noun(name: str) -> str:
    """The 'thematic family' key — last content token after normalization."""
    toks = _normalize_to_tokens(name)
    return toks[-1] if toks else ""


# ── Clustering ───────────────────────────────────────────────────────────────


class _UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra


def cluster_by_token_similarity(names: Sequence[str]) -> List[int]:
    """Return a list of cluster ids parallel to `names`.

    Linking is conservative: two names share a cluster only when they share
    an identical normalized token signature. This catches true surface
    variants (e.g. "Reasoning ability" / "Reasoning capabilities" /
    "Reasoning skills" all reduce to the same signature `reasoning`) without
    creating transitive mega-clusters through common head nouns.

    Broader thematic locality (putting all "X reasoning" or all
    "Hallucination X" items in adjacent batches) is handled by the *batch
    packing* stage, which sorts items by head-noun and first-token before
    slicing into batches — ensuring related items are neighbors even when
    they don't share a signature.
    """
    n = len(names)
    uf = _UnionFind(n)

    by_signature: dict[str, list[int]] = defaultdict(list)
    for i, nm in enumerate(names):
        sig = signature(nm)
        if sig:
            by_signature[sig].append(i)

    for indices in by_signature.values():
        for j in range(1, len(indices)):
            uf.union(indices[0], indices[j])

    return [uf.find(i) for i in range(n)]


def _sort_key(name: str) -> tuple:
    """Sort key that keeps thematically related names adjacent.

    Order: head noun → first content token → normalized signature → raw name.
    With this ordering, all items ending in "reasoning" cluster as one block,
    and within that block items starting with the same modifier are adjacent
    ("Mathematical reasoning" near "Multi-step reasoning"; "Hallucination" is
    adjacent to "Hallucination resistance" via first-token).
    """
    toks = _normalize_to_tokens(name)
    if not toks:
        return ("", "", "", name.lower())
    head = toks[-1]
    first = toks[0]
    sig = " ".join(sorted(set(toks)))
    return (head, first, sig, name.lower())


# ── Batch packing ────────────────────────────────────────────────────────────


def pack_clusters_into_batches(
    cluster_ids: Sequence[int],
    batch_size: int,
    min_batch_size: int = 0,
) -> List[List[int]]:
    """Pack node indices into batches that respect cluster contiguity.

    Strategy: group node indices by cluster, sort clusters from largest to
    smallest, then run first-fit-decreasing into bins of capacity batch_size.
    Clusters bigger than batch_size are split into chunks of batch_size each
    (those chunks stay together in their own batches).

    Args:
      cluster_ids: parallel array of cluster id per node
      batch_size:  target/maximum batch size
      min_batch_size: pack tiny clusters together to avoid sub-min batches

    Returns:
      list of batches; each batch is a list of node indices.
    """
    if not cluster_ids:
        return []

    # Bucket node indices by cluster id, preserving original order within cluster
    by_cluster: dict[int, list[int]] = defaultdict(list)
    for i, c in enumerate(cluster_ids):
        by_cluster[c].append(i)
    clusters: list[list[int]] = sorted(
        by_cluster.values(), key=lambda c: -len(c)
    )

    batches: list[list[int]] = []
    pending: list[list[int]] = []  # small clusters waiting to fill a batch

    for cluster in clusters:
        if len(cluster) >= batch_size:
            # Big cluster — split into contiguous chunks of batch_size
            for start in range(0, len(cluster), batch_size):
                batches.append(cluster[start : start + batch_size])
            continue
        # Small/medium cluster — try to combine with pending small clusters
        pending.append(cluster)
        # Greedy: fill a batch from pending whenever it would overflow
        running = sum(len(c) for c in pending)
        if running >= batch_size:
            # Pack pending using FFD
            pending.sort(key=lambda c: -len(c))
            current: list[int] = []
            leftover: list[list[int]] = []
            for c in pending:
                if len(current) + len(c) <= batch_size:
                    current.extend(c)
                else:
                    leftover.append(c)
            if current:
                batches.append(current)
            pending = leftover

    # Flush remaining pending clusters
    if pending:
        pending.sort(key=lambda c: -len(c))
        current: list[int] = []
        for c in pending:
            if len(current) + len(c) <= batch_size:
                current.extend(c)
            else:
                if current:
                    batches.append(current)
                current = list(c)
        if current:
            batches.append(current)

    # Optional: combine tail batches that are below min_batch_size
    if min_batch_size and len(batches) >= 2:
        merged: list[list[int]] = []
        for b in batches:
            if merged and len(merged[-1]) < min_batch_size and \
               len(merged[-1]) + len(b) <= batch_size:
                merged[-1].extend(b)
            else:
                merged.append(b)
        batches = merged

    return batches


def make_batches(names: Sequence[str], batch_size: int,
                 min_batch_size: int = 0) -> List[List[int]]:
    """Build batches that put thematically related names together.

    Two-phase strategy:
      1. Cluster by exact normalized signature (surface variants) — small
         tight clusters; pack these into batches first using FFD so each
         signature-cluster stays intact in a single batch.
      2. Within the assembled batches, *sort* by (head_noun, first_token,
         signature) so adjacent batch items are thematically related even
         when they aren't surface variants of each other.

    The two phases together: surface variants are guaranteed in the same
    batch (phase 1), and broader thematic neighbours are co-located within
    each batch (phase 2 sort).
    """
    cluster_ids = cluster_by_token_similarity(names)
    raw_batches = pack_clusters_into_batches(cluster_ids, batch_size, min_batch_size)
    # Phase 2: sort indices within each batch by thematic locality
    sorted_batches: List[List[int]] = []
    for batch in raw_batches:
        sorted_batch = sorted(batch, key=lambda i: _sort_key(names[i]))
        sorted_batches.append(sorted_batch)
    return sorted_batches


def make_batches_with_global_sort(names: Sequence[str], batch_size: int) -> List[List[int]]:
    """Alternative: globally sort all names by thematic key then slice.

    Simpler and produces the same family-locality but doesn't guarantee that
    surface-variant siblings (identical signature) end up in the same batch
    when a family straddles a batch boundary. Use make_batches() in
    production; this is here for comparison/debug.
    """
    order = sorted(range(len(names)), key=lambda i: _sort_key(names[i]))
    return [order[i : i + batch_size] for i in range(0, len(order), batch_size)]


# ── Sanity demo ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sample = [
        "Reasoning",
        "Reasoning ability",
        "Reasoning capabilities",
        "Reasoning skills",
        "Reasoning performance",
        "Mathematical reasoning",
        "Multi-step reasoning",
        "Cross-modal reasoning",
        "Multimodal reasoning",
        "Visual reasoning",
        "Hallucination",
        "Hallucination resistance",
        "Hallucination mitigation",
        "Hallucination reduction",
        "Hallucination susceptibility",
        "Code generation",
        "Code-generation ability",
        "Programming ability",
        "Generation quality",
        "Output quality",
        "Image quality",
    ]
    cids = cluster_by_token_similarity(sample)
    by_c: dict[int, list[str]] = defaultdict(list)
    for nm, c in zip(sample, cids):
        by_c[c].append(nm)
    print("Clusters formed:")
    for c, items in by_c.items():
        print(f"  cluster {c}: {items}")
    print()
    print("Batches with batch_size=8:")
    for i, batch in enumerate(make_batches(sample, batch_size=8)):
        print(f"  batch {i}: {[sample[j] for j in batch]}")
