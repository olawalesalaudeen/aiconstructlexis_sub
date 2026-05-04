import json
from typing import Any, Dict, List

# Constructs = abstract latent variables (capabilities, risks, traits). Behaviors = tasks/outputs/performance outcomes.
# Measurements = measurement instruments (benchmarks, datasets, user studies, surveys, etc.); no scores/metrics in extraction.
# Relationships: type is exactly one of: related, causes, correlates. Every node needs source_snippets; evidence must quote the paper.
example_nomological_network = nomological_network_example = {
    "constructs": [
        {
            "name": "Spatial reasoning",
            "description": "The latent ability to mentally represent and manipulate spatial relationships between objects.",
            "source_snippets": [
                '"we evaluate spatial reasoning through block-placement tasks" (Sec. 3)'
            ],
        },
        {
            "name": "Robustness",
            "description": "The degree to which model performance is stable under input perturbations.",
            "source_snippets": [
                '"robustness to adversarial rephrasings" (Abstract)'
            ],
        },
    ],
    "measurements": [
        {
            "name": "BlocksWorld",
            "description": "Planning benchmark requiring multi-step block rearrangement.",
            "source_snippets": ['"evaluated on BlocksWorld" (Table 1)'],
        },
        {
            "name": "User preference study",
            "description": "Human evaluation in which participants rate or rank model outputs on criteria such as helpfulness and coherence.",
            "source_snippets": [
                '"we conducted a user study with 50 participants rating outputs" (Sec. 5)'
            ],
        },
    ],
    "behaviors": [
        {
            "name": "Multi-step planning",
            "description": "Producing a sequence of actions to achieve a goal state from an initial state.",
            "source_snippets": [
                '"the model generates step-by-step plans" (Sec. 4)'
            ],
        },
    ],
    "relationships": [
        {
            "source": "Spatial reasoning",
            "target": "Multi-step planning",
            "type": "related",
            "evidence": '"spatial reasoning underlies the planning steps required" (Sec. 5).',
        },
        {
            "source": "BlocksWorld",
            "target": "Multi-step planning",
            "type": "related",
            "evidence": '"BlocksWorld directly measures multi-step planning ability" (Sec. 3).',
        },
    ],
}


EXTRACT_NOMOLOGICAL_NETWORK_PROMPT_OLD = (
    "The following is an academic paper. "
    "Extract every construct, i.e., latent traits like reasoning and intelligence, "
    "mentioned as a model capability and criteria, i.e., specific downstream tasks, "
    "e.g., downstream accuracy on stackoverflow QA, legal summarization accuracy, "
    "aerodynamics tasks, etc. Include all definitions (verbatim or "
    "paraphrase) and every benchmark or metric linked to the construct. "
    "Also list any explicit relationships (hierarchy, dependency, composition, etc.) "
    "This should be convertable into a nomological network, i.e., "
    "between constructs and sub-constructs or components, and between constructs/sub-constructs and benchmarks. "
    "Focus only on constructs related to large language model capabilities. "
    "For example, if MMLU is mentioned, it is not a construct, it is a benchmark. "
    "Accuracy here is a benchmark (measurement) not a construct. "
    "Intelligence might be the construct claimed for this. "
    "Make sure constructs are refering to latent traits or capabilities of large language models. "
    "Second, also include criterions , i.e., "
    "specific downstream tasks, e.g., downstream accuracy on stackoverflow QA, "
    "legal summarization accuracy, aerodynamics tasks, etc. and any benchmarks/metrics mentioned. "
    "Criterion should not be a construct, it should be a specific observable downstream task. "
    "Include criteria and benchmarks/metrics even if there are no constructs. "
    "Only includes things explicitly mentioned in the paper. "
    "So if there is no explicit definition, you can leave the definition empty; same for the rest. "
    "It is okay to not return null if the paper does not have this type of information; "
    "it might not be a paper relevant to large language models. "
    "Make sure it makes sense and isn't overly complicated. "
    "Observables should be measurable and specific; i.e., benchmark/dataset AND metric. "
    "They may be mediated by criterion to construct or "
    "child of an orphan criterion. "
    "Format exactly as (I included an example nomological network too) "
    f"'Notes: <concise general comments.>. Paper Summary: <concise paper summary>. Nomological Network: {str(example_nomological_network)}.' "
    "Do not include any other text or comments after the 'Nomological Network: <>'. "
)

EXTRACT_NOMOLOGICAL_NETWORK_PROMPT = (
    """Your task is to act as a research assistant. Analyze the following academic paper and extract a **psychometric-style nomological network** for **Large Language Models (LLMs)**: abstract constructs, measurement instruments (benchmarks, user studies, surveys, and other evaluation procedures), observable behaviors/tasks, and relationships grounded in what the paper actually claims. **Faithfulness is more important than coverage**—if you cannot tie an item to a quote from the paper text, **omit** it.

## Phase 1: High-Level Analysis
- **Paper Summary:** 1–3 sentences on core topic and findings.
- **Notes:** Brief relevance/comments.

## Phase 2: Extract entities, then relationships

### 1. Constructs — latent traits inferred from observable evidence

A construct is an **unobservable property of the model itself** — a cognitive ability, disposition, risk, or quality that persists across different tasks and settings. You never see a construct directly; you infer it from patterns of behavior and measurement. In psychometrics these are analogous to intelligence, personality factors, or aptitudes.

**Decision rules (apply in order):**

1. **"Could I watch the model do it?"** If you can point to specific model inputs and outputs that directly demonstrate it, it is a **behavior**, not a construct. If you can only infer it from patterns across multiple tasks or measurements, it is a **construct**.
2. **"Does it generalize as a trait across tasks?"** A construct should describe the model in a way that transfers across many different evaluation settings — the way "intelligence" transfers across math, verbal, and spatial tests. If it only describes what the model does in one specific task setting, it is probably a behavior.
3. **"Is it a property of the model, or of the experimental setup?"** Constructs are properties of the model. Benchmarks, architectures, training methods, and system names are not.

**Typical construct categories** (use as a guide, not a checklist — extract whatever the paper discusses):
- **Cognitive abilities:** reasoning (and its facets: mathematical, logical, commonsense, causal, analogical, spatial, temporal, abductive, etc.), language understanding, knowledge, perception, planning, creativity, abstraction
- **Safety and alignment traits:** harmlessness, helpfulness, toxicity, bias, fairness, robustness, sycophancy, trustworthiness, honesty, deception, safety
- **Model-level properties as latent traits:** generalization, memorization, calibration, interpretability, compositionality, multilinguality, instruction-following ability, in-context learning ability, few-shot learning ability, transfer learning

**What is NEVER a construct:**
- **Observable tasks or actions** → these are behaviors (see below)
- **Architecture components or mechanisms** (e.g. attention heads, mixture-of-experts routing, early-exit layers)
- **Training methods or algorithms** (e.g. RLHF, DPO, process supervision, distillation)
- **System or framework names** (e.g. a named pipeline, toolkit, or agent system)
- **Implementation details** (e.g. inference speed, memory usage, cost-efficiency of a method)
- **Benchmark/instrument names** → these are measurement instruments; **metric/scoring-function names** (accuracy, F1, BLEU, MSE, etc.) → exclude entirely (they are neither constructs nor measurement instruments)

**Resolving borderline cases — when a term names both a faculty and a task:**

Many terms (e.g. "reasoning", "comprehension", "commonsense reasoning") can refer to either a latent faculty or a task depending on context. Apply these rules:

- If a term describes a **broad cognitive ability** that explains performance across multiple tasks → **always classify as construct**, even if the paper also evaluates the model on tasks involving that ability. Terms like "commonsense reasoning", "mathematical reasoning", "language understanding", "logical reasoning" are **always constructs** — they name latent faculties, not specific observable tasks.
- Only classify something as a behavior if it describes a **specific, concrete task format** the model performs (e.g. "multiple-choice question answering", "code generation", "text summarization"). The task must be defined by its input/output format, not by the underlying ability.
- **When in doubt, prefer construct.** If a term could reasonably be either, classify it as a construct. It is better to over-include constructs than to misclassify latent abilities as behaviors.
- The corresponding behavior, if needed, should be named by the **task format** (e.g. construct "Commonsense reasoning" → behavior "Commonsense question answering"; construct "Mathematical reasoning" → behavior "Mathematical problem solving").

**Granularity rules:**
- **Split** distinct facets into separate constructs when the paper treats them as distinguishable abilities (e.g. "mathematical reasoning" and "logical reasoning" should be separate if the paper evaluates or discusses them differently).
- **Do not over-split:** if the paper mentions a term once in passing, it does not warrant a separate construct. The paper must discuss or evaluate it substantively.
- **Do not under-split:** if the paper explicitly contrasts two facets, they must be separate constructs.
- Use the **most specific name the paper supports.** If it discusses "spatial reasoning" specifically, use that — not the broader "Reasoning".

**Naming conventions:**
- Use **concise, community-standard noun phrases** that another researcher studying a different paper about the same trait would recognize.
- **Drop filler suffixes** like "ability", "capability", "skill" unless needed to disambiguate. Prefer "Mathematical reasoning" over "Mathematical reasoning ability".
- **Capitalize** only the first word (sentence case): "Mathematical reasoning", not "Mathematical Reasoning".

**Field requirements for each construct:**
- `name`: Concise noun-phrase label (2–5 words typical).
- `description`: One sentence that **defines** the latent trait so a reader who has not seen the paper can understand it. Do NOT just restate the name — add real explanatory content (e.g. for "Calibration" write "The degree to which the model's expressed confidence matches its actual accuracy across predictions").
- `source_snippets`: **Non-empty list**. Each entry is a **verbatim quote** copied directly from the paper text, optionally followed by a location reference like "(Sec. 3)" or "(Table 2)". Keep each snippet to the relevant phrase or sentence — not the whole paragraph. Do not paraphrase.

### 2. Behaviors — what you can observe the model doing

A behavior is an **observable action, output, or phenomenon the model exhibits**. This includes both intentional task performance AND emergent/unintended behaviors. If you could write an evaluation script that directly checks whether the model is doing it, it is a behavior.

**Two kinds of behaviors:**
1. **Task behaviors** — things the model is asked to do (e.g. code generation, question answering, translation). These are intentional and defined by their input/output format.
2. **Non-task behaviors** — observable patterns in the model's outputs that are not defined by a specific task format. These include emergent phenomena (e.g. hallucination, sycophancy, memorization of training data), failure modes (e.g. reward hacking, mode collapse, catastrophic forgetting), and other observable output patterns (e.g. self-correction, verbose generation, refusal).

Both are behaviors. The key distinction from constructs: a behavior is **directly observable in specific model outputs**, while a construct is a **latent trait inferred from patterns across behaviors**.

**Decision rules:**

1. **"Can I point to specific model outputs that demonstrate it?"** If yes → behavior (whether intentional or unintended). If you can only infer it from patterns across many outputs → construct.
2. **"Would this be a row in a leaderboard, or a column?"** Measurement instruments assess behaviors (rows); the latent trait the instrument is designed to probe is a construct (column).

**Typical behavior categories** (use as a guide, not strict buckets — extract whatever the paper discusses, even if it doesn't fit neatly into these categories):
- **Generation tasks:** text generation, code generation, translation, summarization, image captioning, dialogue generation, data-to-text generation
- **Comprehension tasks:** question answering, reading comprehension, natural language inference, sentiment analysis, textual entailment
- **Structured output tasks:** information extraction, named entity recognition, parsing, table generation, relation extraction
- **Interactive tasks:** instruction following, tool use, multi-turn conversation, negotiation, web navigation
- **Safety-related behaviors:** harmful content refusal, jailbreak resistance, response under adversarial perturbation, toxic content generation
- **Non-task behaviors:** hallucination (generating false or unsupported content), sycophancy (agreeing with the user regardless of correctness), memorization/regurgitation of training data, reward hacking, mode collapse, catastrophic forgetting, shortcut learning, self-correction, verbose generation, refusal
- **Domain-specific tasks:** clinical note generation, legal document analysis, scientific literature review, financial forecasting, robot manipulation

**Naming conventions:**
- Use **generic, reusable task names** that would apply across papers studying the same task — not paper-specific method names or overly narrow phrasings.
- **Abstract away** paper-specific framing to the standard community task name (e.g. "grade-school arithmetic solving" → "mathematical problem solving"; "vulnerability repair" → "code repair"; "step-level beam search inference" → the behavior it performs, not the method name).
- A measurement instrument that *assesses* a behavior is not itself a behavior. The behavior is the task; the instrument is how you test it. Do not use instrument names as behavior names.
- Use **present-tense gerund or noun form**: "Code generation", "Question answering", not "Generates code" or "Answer questions".
- **Capitalize** only the first word (sentence case).

**Field requirements for each behavior:**
- `name`: Concise noun-phrase label (2–5 words typical).
- `description`: One sentence describing what the model observably does, written so a reader can understand it without seeing the paper. Do NOT just restate the name — describe the task concretely enough that someone could design an evaluation for it.
- `source_snippets`: Same rules as constructs — verbatim quotes with optional location references. Non-empty list.

### 3. Measurement instruments — how constructs and behaviors are assessed

A measurement instrument is any **named, reproducible procedure used to assess model capabilities or behaviors**. This is broader than just benchmarks — it includes any structured way researchers gather evidence about a model.

**Categories of measurement instruments** (use as a guide, not strict buckets — extract whatever the paper uses, even if it doesn't fit neatly into these categories):
- **Benchmarks and datasets:** Named test sets the model is evaluated on (e.g. MMLU, HumanEval, SQuAD, ImageNet)
- **Human evaluation protocols:** User studies, preference studies, Likert-scale surveys, A/B tests, expert annotation tasks, crowdsourced ratings, inter-annotator agreement studies
- **Standardized questionnaires and scales:** Psychometric instruments, personality inventories, bias probes, Turing-test-style evaluations, red-teaming protocols
- **Evaluation suites and frameworks:** Named collections of tests (e.g. HELM, BIG-Bench, lm-eval-harness)
- **Domain-specific assessment procedures:** Clinical vignette evaluations, legal case analysis tasks, structured interviews with the model, simulation-based assessments

**What to include:** Any instrument the paper actually uses or explicitly references for evaluation that has a recognizable name or well-defined protocol. The instrument must be concrete enough that another researcher could replicate or reference it.

**What to exclude — scoring functions and evaluation metrics:** Any formula or algorithm that takes model output and returns a number is a **metric**, not a measurement instrument. Metrics are *how you score*; measurement instruments are *what you use to gather the data you score*. Exclude: accuracy, F1, BLEU, ROUGE, METEOR, BERTScore, MSE, MAE, RMSE, perplexity, pass@k, win rate, CIDEr, SPICE, EM (exact match), precision, recall, any "*-score" metric. Also exclude: evaluation settings (5-shot, zero-shot), training datasets (unless also used for evaluation), unnamed or ad-hoc test sets, and vague references like "our evaluation" or "the test set".

**Naming conventions:**
- Use the **community-standard short name** of the instrument — the name other researchers would use to look it up (e.g. the acronym if widely used).
- For human evaluations without a standard name, use a descriptive label that captures the method (e.g. "User preference study", "Expert annotation evaluation", "Red-teaming assessment").
- Put the full name and a brief description of what it assesses in the `description` field.
- Do NOT embed metric names or evaluation settings in the instrument name.
- **Capitalize** the name exactly as the community standard dictates (benchmark names are often acronyms or proper nouns; descriptive human evaluation names use sentence case).

**Field requirements for each measurement instrument:**
- `name`: The standard short name of the instrument or a descriptive label for the evaluation method.
- `description`: Full name (if the short name is an acronym) plus one sentence on what domain/ability/task it assesses and how (e.g. format, modality, population). Self-contained for a reader who has not seen the paper.
- `source_snippets`: Same rules as constructs — verbatim quotes with optional location references. Non-empty list.

### How constructs, behaviors, and measurement instruments relate

The three entity types form a layered structure:
- A **construct** (latent trait) manifests through one or more **behaviors** (observable tasks).
- A **measurement instrument** (benchmark, user study, evaluation protocol, etc.) is a procedure that directly tests a behavior and indirectly probes a construct.
- Example pattern: [Construct: latent trait] → [Behavior: observable task] ← [Measurement instrument: benchmark or evaluation]. The construct is *why* the model can do it; the behavior is *what* you see it do; the measurement instrument is the procedure you use to test it.
- The same instrument can relate to both a behavior (the task being measured) and a construct (the latent trait being probed). Include both links when the paper supports them.

**Final disambiguation check:** When in doubt between construct and behavior, **prefer construct**. If a term names a cognitive faculty or general ability (e.g. "reasoning", "comprehension", "commonsense reasoning"), it is always a construct. Only use behavior for terms that describe a specific, concrete task format defined by its inputs and outputs.

### Relationships

- Only edges **supported by the text**. `type` must be exactly one of: `related` (default when mechanism is unspecified), `causes` (explicit or strong causal claim), `correlates` (empirical association, regression, "predicts" in the statistical sense).
- `evidence` must include at least one quoted span from the paper.
- Any entity pair is allowed (construct↔construct, construct↔behavior, construct↔measurement instrument, measurement instrument↔behavior, measurement instrument↔measurement instrument, behavior↔behavior) as long as the paper supports it.
- Measurement instruments often relate to both behaviors (the task being measured) and constructs (the latent trait being probed). Include both when supported.

## Phase 3: Self-audit

After drafting, re-read the paper and run these checks:

1. **Quote check:** For every entity and relationship, confirm each quote in `source_snippets` or `evidence` **actually appears** in the supplied paper text. Delete or fix any that fail.
2. **Category check:** Re-apply the decision rules for every entity:
   - For each construct: "Could I watch the model do it?" (must be no) and "Does it generalize as a trait?" (must be yes). If a term names a cognitive faculty, it stays as a construct even if the paper also uses it in a task context.
   - For each behavior: "Is this a specific, concrete observable task defined by its input/output format?" (must be yes). If it is actually a latent trait or general ability name, reclassify as a construct.
   - For each measurement instrument: "Is this a named/described procedure for gathering evidence about a model?" (must be yes). If it is a scoring function (accuracy, F1, BLEU, MSE, ROUGE, BERTScore, win rate, etc.), **remove it** — metrics are not measurement instruments.
3. **Relationship check:** Verify direction, `type`, and that both source and target names exactly match entities in your lists.
4. **Naming check:** For each entity, ask: "Would another researcher studying a different paper about the same ability/task use the same name?" Normalize to community-standard terms.

## Phase 4: Final JSON

Return a single JSON object with keys: `Title`, `Notes`, `Paper Summary`, `Nomological Network`.

The `Nomological Network` must have exactly:
- `"constructs": [ { "name", "description", "source_snippets" }, ... ]`
- `"measurements": [ { "name", "description", "source_snippets" }, ... ]`
- `"behaviors": [ { "name", "description", "source_snippets" }, ... ]`
- `"relationships": [ { "source", "target", "type", "evidence" }, ... ]`

If the paper has no LLM-relevant content, use empty lists. No markdown or extra text outside the JSON.

Example shape (illustrative only):
"""
    + json.dumps(example_nomological_network, indent=2, ensure_ascii=False)
    + """
"""
)

EXTRACT_ENTITIES_PROMPT = (
    """Your task is to act as a research assistant. Analyze the following academic paper and extract **entities only** (no relationships yet) for a **psychometric-style nomological network** for **Large Language Models (LLMs)**: abstract constructs, measurement instruments (benchmarks, user studies, surveys, and other evaluation procedures), and observable behaviors/tasks. **Faithfulness is more important than coverage**—if you cannot tie an item to a quote from the paper text, **omit** it.

## High-Level Analysis
- **Paper Summary:** 1–3 sentences on core topic and findings.
- **Notes:** Brief relevance/comments.

## Entity Definitions

The three entity types form a layered structure: a **construct** (latent trait) manifests through one or more **behaviors** (observable tasks), and a **measurement instrument** is the procedure used to test a behavior and thereby probe a construct. The construct is *why* the model can do it; the behavior is *what* you see it do; the instrument is *how* you test it. The same instrument can relate to both a behavior and a construct — include both links when the paper supports them.

### 1. Constructs — latent traits inferred from observable evidence

A construct is an **unobservable property of the model** — a cognitive ability, disposition, risk, or quality that persists across tasks. You never see it directly; you infer it from patterns of behavior and measurement. Analogous to intelligence or personality factors in psychometrics.

**Decision rules (apply in order):**
1. **"Could I watch the model do it?"** If specific inputs and outputs directly demonstrate it → **behavior**. If you can only infer it from patterns across many tasks → **construct**.
2. **"Does it generalize as a trait across tasks?"** A construct transfers across different evaluation settings (the way "intelligence" transfers across math, verbal, and spatial tests). If it only describes one specific task setting, it is probably a behavior.
3. **"Is it a property of the model, or of the experimental setup?"** Only model properties count. Architectures, training methods, system/framework names, and implementation details (inference speed, memory, cost) are never constructs. Metric/scoring-function names (accuracy, F1, BLEU, MSE, etc.) are excluded entirely — they are neither constructs nor instruments.

**When in doubt between construct and behavior, prefer construct.** If a term names a cognitive faculty or general ability (e.g. "reasoning", "comprehension", "commonsense reasoning", "mathematical reasoning", "language understanding"), classify as construct even if the paper also evaluates tasks involving it. Only use behavior for terms defined by a specific input/output task format (e.g. "multiple-choice question answering", "code generation"). Corresponding behavior names should come from the task format (construct "Commonsense reasoning" → behavior "Commonsense question answering").

**Examples to give you a flavor of construct categories** (illustrative only — extract whatever the paper actually discusses, including things not listed here):
- *Cognitive abilities:* reasoning and its facets (mathematical, logical, commonsense, causal, spatial, temporal, …), language understanding, planning, creativity, abstraction
- *Safety and alignment traits:* harmlessness, helpfulness, toxicity, bias, fairness, robustness, sycophancy, honesty, deception
- *Model-level latent properties:* generalization, memorization, calibration, interpretability, compositionality, multilinguality, instruction-following, in-context learning

**Granularity:** split distinct facets into separate constructs when the paper treats them as distinguishable (e.g. "mathematical reasoning" vs "logical reasoning" if evaluated separately); do not over-split for passing mentions; use the most specific name the paper supports.

**Naming:** concise noun phrases another researcher would recognize; drop filler suffixes like "ability"/"capability"/"skill" unless needed to disambiguate; sentence case ("Mathematical reasoning", not "Mathematical Reasoning").

**Field requirements:**
- `name`: concise noun-phrase label (a few words typical).
- `description`: one sentence that **defines** the latent trait for a reader who has not seen the paper. Do NOT just restate the name — add real explanatory content (e.g. for "Calibration": "The degree to which the model's expressed confidence matches its actual accuracy across predictions").
- `source_snippets`: **non-empty list** of **verbatim quotes** from the paper, each optionally followed by a location reference like "(Sec. 3)". Keep to the relevant phrase or sentence. Do not paraphrase.

### 2. Behaviors — what you can observe the model doing

A behavior is an **observable action, output, or phenomenon the model exhibits** — both intentional task performance AND emergent/unintended behaviors. If you could write an evaluation script that directly checks whether the model is doing it, it is a behavior.

**Two kinds:**
1. **Task behaviors** — what the model is asked to do (code generation, question answering, translation); defined by input/output format.
2. **Non-task behaviors** — observable output patterns not defined by a task format: emergent phenomena (hallucination, sycophancy, memorization), failure modes (reward hacking, mode collapse, catastrophic forgetting), or other patterns (self-correction, verbose generation, refusal).

**Row-vs-column heuristic:** measurement instruments assess behaviors (rows); the latent trait being probed is a construct (column). A measurement instrument that *assesses* a behavior is not itself a behavior — do not use instrument names as behavior names.

**Examples to give you a flavor of behavior categories** (illustrative only — extract whatever the paper actually discusses, including things not listed here):
- *Generation:* text/code generation, translation, summarization, image captioning, dialogue
- *Comprehension:* question answering, reading comprehension, natural language inference, sentiment analysis
- *Structured output:* information extraction, NER, parsing, relation extraction
- *Interactive:* instruction following, tool use, multi-turn conversation, web navigation
- *Safety-related:* harmful-content refusal, jailbreak resistance, response under adversarial perturbation
- *Non-task patterns:* hallucination, sycophancy, memorization, reward hacking, mode collapse, refusal, self-correction

**Naming:** use generic, reusable task names that apply across papers — not paper-specific method names. Abstract paper framing to the community-standard name (e.g. "grade-school arithmetic solving" → "Mathematical problem solving"). Use noun/gerund form ("Code generation", not "Generates code"). Sentence case.

**Field requirements:**
- `name`: concise noun-phrase label (2–5 words typical).
- `description`: one sentence describing what the model observably does, concrete enough that someone could design an evaluation for it. Do NOT just restate the name.
- `source_snippets`: same rules as constructs — verbatim quotes, non-empty list.

### 3. Measurement instruments — how constructs and behaviors are assessed

A measurement instrument is any **named, reproducible procedure used to assess model capabilities or behaviors** — broader than benchmarks.

**Examples to give you a flavor of instrument categories** (illustrative only — extract whatever the paper actually uses, including things not listed here):
- *Benchmarks and datasets:* named test sets (MMLU, HumanEval, SQuAD, ImageNet, …)
- *Human evaluation protocols:* user studies, preference studies, Likert surveys, A/B tests, expert annotation, crowdsourced ratings, inter-annotator agreement
- *Standardized questionnaires and scales:* psychometric instruments, personality inventories, bias probes, Turing-test evaluations, red-teaming protocols
- *Evaluation suites:* HELM, BIG-Bench, lm-eval-harness, …
- *Domain-specific procedures:* clinical vignette evaluations, legal case analysis, simulation-based assessments

**Include** any instrument the paper uses or references that has a recognizable name or well-defined protocol, concrete enough to replicate.

**Exclude scoring functions/metrics entirely.** Metrics are *how you score*; instruments are *what you use to gather the data you score*. Exclude: accuracy, F1, BLEU, ROUGE, METEOR, BERTScore, MSE/MAE/RMSE, perplexity, pass@k, win rate, CIDEr, SPICE, EM, precision, recall, any "*-score" metric. Also exclude: evaluation settings (5-shot, zero-shot), training-only datasets, unnamed/ad-hoc test sets, and vague references ("our evaluation", "the test set").

**Naming:** use the community-standard short name (often an acronym). For unnamed human evaluations, use a descriptive label ("User preference study", "Expert annotation evaluation", "Red-teaming assessment"). Put the full name in `description`. Do not embed metric names or settings in the instrument name.

**Field requirements:**
- `name`: standard short name or descriptive label for the evaluation method.
- `description`: full name (if acronym) + one sentence on what domain/ability/task it assesses and how (format, modality, population). Self-contained.
- `source_snippets`: same rules as constructs — verbatim quotes, non-empty list.

## Self-Check

Before finalizing:
1. **Quote check:** every `source_snippets` entry must actually appear in the paper text. Delete or fix any that fail.
2. **Category check:** reapply the decision rules. Move latent traits misclassified as behaviors back to constructs; remove any metrics (accuracy, F1, BLEU, etc.) listed as instruments.
3. **Naming check:** would another researcher studying a different paper about the same ability/task use the same name? Normalize to community-standard terms.

## Output Format (JSON)

Return a single JSON object with keys: `Title`, `Notes`, `Paper Summary`, `Nomological Network`.
The `Nomological Network` must have exactly:
- `"constructs": [ { "name", "description", "source_snippets" }, ... ]`
- `"measurements": [ { "name", "description", "source_snippets" }, ... ]`
- `"behaviors": [ { "name", "description", "source_snippets" }, ... ]`

**Do NOT include a `relationships` key.** Relationships will be extracted in a separate step.

If the paper has no LLM-relevant content, use empty lists.

Example shape (illustrative only):
"""
    + json.dumps(
        {
            k: v
            for k, v in example_nomological_network.items()
            if k != "relationships"
        },
        indent=2,
        ensure_ascii=False,
    )
    + """
"""
)

EXTRACT_RELATIONSHIPS_PROMPT = """Your task is to act as a research assistant. You are given an academic paper and a set of **already-extracted entities** (constructs, measurement instruments, behaviors). Extract **relationships** between these entities that are explicitly supported by the paper text.

## Already-Extracted Entities

{entities_json}

## Relationship Extraction Rules

- **ONLY use entities from the list above** as source and target. Do NOT introduce new entity names.
- **`type` must be exactly one of:**
  - `causes` — explicit or strong causal claim ("X improves Y", "X enables Y", "X leads to Y")
  - `correlates` — empirical association, regression, or "predicts" in the statistical sense ("X is associated with Y", "higher X corresponds to higher Y")
  - `measured_by` — a construct or behavior is evaluated/operationalized by a measurement instrument ("We evaluate X using benchmark Y", "We conducted a user study to assess X")
  - `related` — a stated conceptual or empirical link that is NOT merely co-occurrence. The paper must describe HOW or WHY the two entities are connected.

### Evidence Quality Rules (STRICT)

- **`evidence`:** must be a **quoted substring** from the paper that **directly describes the connection** between source and target — not just mentions both in the same sentence.
- **Do NOT extract a relationship just because two entities appear in the same list, table, or sentence.** Listing instruments together (e.g. "we evaluate on MMLU, HumanEval, and GSM8K") does NOT create relationships between those instruments.
- **Do NOT extract a relationship if the evidence only shows co-occurrence** (e.g. "We test reasoning and code generation" does NOT mean reasoning → code generation).
- The evidence must answer: **"What does the paper say about how/why these two entities are connected?"** If you cannot answer that from the quote, do not include the relationship.

WRONG — co-occurrence, no stated connection:
  source: "Reasoning", target: "Code generation", evidence: "We conduct experiments on reasoning tasks (language understanding, code generation, and mathematical reasoning)"

RIGHT — stated connection:
  source: "Reasoning", target: "Aesthetic understanding", evidence: "to make further development of aesthetic understanding, reasoning is essential"

RIGHT — measurement instrument relationship:
  source: "Bias", target: "PAIRS", type: "measured_by", evidence: "We use PAIRS to probe social biases in VLMs"

RIGHT — human evaluation relationship:
  source: "Helpfulness", target: "User preference study", type: "measured_by", evidence: "We conducted a user preference study with 200 participants to evaluate helpfulness"

- **Allowed source–target patterns** (any combination justified by the text):
  - construct ↔ construct
  - construct ↔ behavior
  - construct → measurement instrument (measured_by)
  - measurement instrument → behavior
  - measurement instrument ↔ measurement instrument (e.g. a benchmark suite contains a sub-benchmark, or two instruments measure overlapping domains)
  - behavior ↔ behavior

## Self-Check

After drafting, verify:
- Every source and target name **exactly matches** an entity name from the list above.
- Every evidence quote **appears** in the supplied paper text.
- The evidence **describes a connection**, not just co-occurrence.
- Direction and `type` match the paper's claims.
- Prefer fewer, higher-quality relationships over many weak ones.

## Output Format (JSON)

Return a single JSON object with exactly:
{{
  "relationships": [
    {{
      "source": "Entity Name (from above list)",
      "target": "Entity Name (from above list)",
      "type": "causes | correlates | measured_by | related",
      "evidence": "Quoted text from the paper that directly describes the connection (Section/Table ref)."
    }}
  ]
}}

If no relationships are supported, return `{{"relationships": []}}`.

Return only the JSON object, no additional text."""


SCREENING_PAPERS_PROMPT = """
You are a document classifier. Determine if the following paper is about large language model (LLM) capabilities, risks, evaluation, behavior, or tasks.

Answer "Yes" if the paper:
- Discusses LLM capabilities, risks, safety, fairness, understanding, benchmarks, performance, etc.
- Evaluates or measures LLMs (benchmarks, tasks, metrics).
- Addresses LLM behavior, risks, or real-world use.

Answer "No" if the paper is not about LLMs or does not address capabilities, risks, safety, fairness, understanding, benchmarks, performance, etc.

Respond with exactly one word: Yes or No.

Response:
"""

# Backwards compatibility
SCREEINING_PAPERS_PROMPT = SCREENING_PAPERS_PROMPT

# =============================================================================
# Shared merge rules — used identically whether the input is raw extracted names
# or already-grouped canonical groups from a prior pass. Merge logic doesn't
# depend on which pass; it only depends on whether two names refer to the same
# concept.
# =============================================================================

_SHARED_MERGE_PRINCIPLE = """**The principle:** two names refer to the same concept when a domain expert would use them interchangeably in a paper. If you can swap one for the other in a sentence and the meaning is unchanged, they are the same concept and should merge. If the swap would change the meaning, scope, or specificity, they are different concepts and should stay separate.

In practice, this means **merging surface variants** (different ways of writing the same idea) and **keeping conceptual variants separate** (different ideas, even if related).

A few illustrative examples — extrapolate the spirit, don't treat as an exhaustive checklist:

- *Surface variants → merge*: hyphenation/spacing ("Multi-step" / "Multistep" / "Multi step"), grammatical inflection ("ability" / "abilities" / "capability" / "capabilities"), morphology ("Logical" / "Logic"), interchangeable synonyms ("understanding" / "comprehension" / "awareness"), equivalent prefixes (e.g. "Multimodal" / "Cross-modal"), rephrasings of the same idea ("Alignment with human preferences" / "Preference alignment").

- *Conceptual variants → keep separate*: hierarchical relationships ("Reasoning" vs "Mathematical reasoning"), distinct facets ("Mathematical reasoning" vs "Commonsense reasoning"), different domains ("Legal reasoning" vs "Medical reasoning"), different cognitive modes ("Deductive" vs "Inductive" vs "Abductive"), qualified/scoped variants vs bare parent ("Adversarial robustness" vs "Robustness").

When two surface forms differ only in trivial ways (filler words like "ability"/"capability"/"capacity"/"skill" — singular or plural — that don't change the concept; whitespace; punctuation; case; common synonym verbs), strongly prefer to merge. Save the "keep separate" judgment for cases where the underlying concepts genuinely differ."""


AGGREGATE_CONSTRUCTS_PROMPT = (
    """Deduplicate constructs (latent LLM capabilities, risks, traits) by grouping rows that name the **same concept** under different wording.

Each input row has an `id`. Output only the grouping as `{canonical_name: [ids]}`. All metadata (definitions, papers, snippets) is resolved from the IDs programmatically — do NOT repeat them.

**Canonical name:** concise, community-standard noun phrase, sentence case. When several surface forms collapse to one concept, pick the bare form a domain expert would use in writing — strip filler words like "ability"/"capability" when they're separable, but keep them when they're integral to the term ("Interpretability", "Scalability").

"""
    + _SHARED_MERGE_PRINCIPLE
    + """

**Output format:**
```json
{"groups": {"Reasoning": [0, 3, 7, 11], "Logical reasoning": [5]}, "ungrouped": [12]}
```
`ungrouped` lists IDs that don't merge with anything else. Every input ID must appear exactly once.

**Input rows:**
{constructs_json}

Return only the JSON object."""
)

AGGREGATE_MEASUREMENTS_PROMPT = (
    """Deduplicate measurement instruments (benchmarks, datasets, user studies, surveys, human evaluations, and other named evaluation procedures) by grouping rows that refer to the **same instrument** under different names. Do NOT merge or split based on reported metrics or scores.

Each input row has an `id`. Output only the grouping as `{canonical_name: [ids]}`. All metadata is resolved from the IDs programmatically — do NOT repeat descriptions, papers, or snippets.

**Canonical name:** community-standard short name of the instrument (e.g. "MMLU", "HumanEval", "HELM Math"). Name the instrument only — never the metric ("MMLU Accuracy" → "MMLU"). Include a subset qualifier when the input row is about a specific subset. For human evaluations, use a descriptive label that captures the method.

"""
    + _SHARED_MERGE_PRINCIPLE
    + """

**Instrument-specific notes:** acronym↔full-name pairs ("MMLU" ≡ "Massive Multitask Language Understanding") merge; procedural rephrasings of the same evaluation method merge. But subsets, distribution-shift variants, and different experimental conditions are *different* instruments — keep them separate (e.g. "MMLU Math" ≠ "MMLU"; "ImageNet-A" ≠ "ImageNet"; "User preference study" ≠ "Expert annotation evaluation").

**Output format:**
```json
{"groups": {"MMLU": [0, 4], "HumanEval": [2], "User preference study": [6, 9]}, "ungrouped": [1, 3, 5]}
```
`ungrouped` lists IDs that don't merge with anything else. Every input ID must appear exactly once.

**Input rows:**
{measurements_json}

Return only the JSON object."""
)

AGGREGATE_BEHAVIORS_PROMPT = (
    """Deduplicate behaviors (observable tasks, outputs, performance outcomes, and non-task observable phenomena like hallucination, sycophancy, memorization — not latent constructs, not measurement instruments) by grouping rows that name the **same observable behavior** under different wording.

Each input row has an `id`. Output only the grouping as `{canonical_name: [ids]}`. All metadata is resolved from the IDs programmatically — do NOT repeat definitions, papers, or snippets.

**Canonical name:** concise, community-standard noun phrase, sentence case (e.g. "Code generation", "Question answering", "Hallucination").

"""
    + _SHARED_MERGE_PRINCIPLE
    + """

**Behavior-specific notes:** the *core action* is what makes a behavior distinctive — predicting, generating, classifying, retrieving, refusing, etc. are different behaviors even when applied to the same target. Specific task instances aren't the same as their generic umbrella ("Moving a sliding door" ≠ "Task completion"). Different methods/strategies for the same outcome are different behaviors.

**Output format:**
```json
{"groups": {"Code generation": [0, 4], "Question answering": [2]}, "ungrouped": [1, 3, 5]}
```
`ungrouped` lists IDs that don't merge with anything else. Every input ID must appear exactly once.

**Input rows:**
{behaviors_json}

Return only the JSON object."""
)


def _unclustered_rows_to_groups(
    unclustered: Any,
    node_type: str,
) -> List[Dict[str, Any]]:
    """Normalize AGGREGATE_* `unclustered` entries to the same shape as `groups`."""
    if not unclustered or not isinstance(unclustered, list):
        return []
    out: List[Dict[str, Any]] = []
    for u in unclustered:
        if not isinstance(u, dict):
            continue
        paper = u.get("paper") or ""
        papers = [paper] if paper else []
        if node_type == "constructs":
            nm = (u.get("name") or "").strip()
            if not nm:
                continue
            desc = u.get("definition", "") or ""
            out.append(
                {
                    "canonical_name": nm,
                    "unified_definition": desc,
                    "original_names": [nm],
                    "papers": papers,
                }
            )
        elif node_type == "measurements":
            nm = (u.get("name") or "").strip()
            if not nm:
                continue
            desc = u.get("description", "") or ""
            out.append(
                {
                    "canonical_name": nm,
                    "unified_description": desc,
                    "original_names": [nm],
                    "papers": papers,
                }
            )
        else:
            nm = (u.get("name") or "").strip()
            if not nm:
                continue
            desc = u.get("description", "") or ""
            out.append(
                {
                    "canonical_name": nm,
                    "unified_definition": desc,
                    "original_names": [nm],
                    "papers": papers,
                }
            )
    return out


def merge_aggregate_llm_groups(
    result: Any, node_type: str
) -> List[Dict[str, Any]]:
    """Combine `groups` and `unclustered` from an AGGREGATE_* LLM JSON object."""
    if not isinstance(result, dict):
        return []
    # Use explicit key presence check (not `or`-chain) so an intentional
    # empty list like {"groups": []} is respected rather than falling
    # through to alternative keys.
    groups_list: List[Dict[str, Any]] = []
    for key in (
        "groups",
        "group",
        "Group",
        "GROUPS",
        "data",
        "items",
        "results",
    ):
        if key in result and isinstance(result[key], list):
            groups_list = list(result[key])
            break
    groups_list.extend(
        _unclustered_rows_to_groups(result.get("unclustered"), node_type)
    )
    return groups_list


def build_aggregate_grouping_prompt(
    node_type: str,
    nodes_json: str,
    existing_mapping_json: str = "",
) -> str:
    """Full user prompt for one AGGREGATE_* grouping call.

    When *existing_mapping_json* is non-empty, a preamble is prepended that
    shows the LLM which names already have canonical forms so it can merge
    new names into existing canonical groups (or revise them).
    """
    if node_type == "constructs":
        base = AGGREGATE_CONSTRUCTS_PROMPT.replace(
            "{constructs_json}", nodes_json
        )
    elif node_type == "measurements":
        base = AGGREGATE_MEASUREMENTS_PROMPT.replace(
            "{measurements_json}", nodes_json
        )
    elif node_type == "behaviors":
        base = AGGREGATE_BEHAVIORS_PROMPT.replace(
            "{behaviors_json}", nodes_json
        )
    else:
        raise ValueError(
            f"Unknown node_type for aggregate grouping: {node_type}"
        )

    if existing_mapping_json:
        mapping_ctx = (
            "\n\n**Existing name mapping (original → canonical) from prior runs.**\n"
            "Use these as a starting point: prefer reusing these canonical names when "
            "a node clearly refers to the same concept.  You may revise or merge "
            "canonical names if the evidence warrants it.\n\n"
            f"```json\n{existing_mapping_json}\n```\n"
        )
        base = mapping_ctx + "\n" + base

    return base


def build_aggregate_relationships_prompt(
    relationships_json: str,
    construct_groups_json: str,
    measurement_groups_json: str,
    behavior_groups_json: str,
    name_mapping_json: str,
) -> str:
    """
    Full user prompt for relationship aggregation. Uses str.format; JSON payloads are passed
    as format arguments (braces inside those strings are literal, not template fields).
    """
    return AGGREGATE_RELATIONSHIPS_PROMPT.format(
        construct_groups_json=construct_groups_json,
        measurement_groups_json=measurement_groups_json,
        behavior_groups_json=behavior_groups_json,
        name_mapping_json=name_mapping_json,
        relationships_json=relationships_json,
    )


# -----------------------------
# Consensus / canonical definition synthesis (per node)
# -----------------------------
#
# Intended use:
# - Provide a single node (canonical_name + type) and ALL extracted definition snippets for that node
#   (ideally with paper titles).
# - The model should synthesize a consensus definition, explicitly noting disagreements / variants.
# - Designed for Together AI (OpenAI-compatible chat/completions) but works with most LLMs.
#
# Expected input variables:
# - {canonical_name}: string
# - {node_type}: one of "construct", "measurement", "behavior"
# - {definitions_json}: JSON string for a list of objects:
#     [{"text": "...", "paper": "..."}, ...]
#
# Expected output: plain text only (no JSON, no markdown).
# The output should be directly stored into each node's `canonical_definition` field.
CONSENSUS_DEFINITION_TEXT_PROMPT = """You are an expert scientific editor and ontology curator.

Your task: write a high-quality CONSENSUS DEFINITION (plain text) for a single node in an AI nomological network, based ONLY on the provided extracted definition snippets from papers.

Node:
- canonical_name: {canonical_name}
- type: {node_type}

Definition snippets (JSON):
{definitions_json}

Requirements:
1) Produce ONE consensus definition that is:
   - faithful to the snippets
   - precise but readable
   - avoids paper-specific experimental details (tables, hyperparameters) unless they are part of the definition itself
2) Keep as much detail about the *specifics* of definitions and *differences* between sources as is useful—include concrete distinctions, scope, and how authors disagree or agree—without being unnecessarily long. Prefer 1–3 sentences when that suffices; use more only when needed to capture important specifics.
3) If snippets show disagreement, incorporate it clearly by qualifying the definition (e.g., “often operationalized as…”, “some papers define this more narrowly as…”) so the reader sees what varies; do not collapse real differences into vague wording.
4) If the snippets are too sparse, low-quality, or contradictory to form a consensus, output exactly: N/A
5) Do NOT invent facts. Do NOT add external knowledge. Use only the supplied snippets.
6) Prefer canonical names when referring to the node; do not introduce new names.

Output rules:
- Output MUST be a single plain-text definition (or exactly N/A).
- Do NOT output JSON.
- Do NOT output bullet points.
- Do NOT include any prefix like \"Consensus Definition:\".
"""

# Measurement-instrument-focused variant:
# Summarize the instrument itself (what it tests, format, procedure),
# and avoid metric/score boilerplate (accuracy %, EM, etc.) unless it is definitional.
CONSENSUS_DEFINITION_TEXT_PROMPT_MEASUREMENT = """You are an expert scientific editor and evaluation-methods curator.

Your task: write a high-quality CONSENSUS DEFINITION (plain text) for a single MEASUREMENT INSTRUMENT node in an AI nomological network, based ONLY on the provided extracted definition snippets from papers. Measurement instruments include benchmarks, datasets, user studies, surveys, human evaluation protocols, and other named evaluation procedures.

Node:
- canonical_name: {canonical_name}
- type: measurement instrument

Definition snippets (JSON):
{definitions_json}

Requirements:
1) Produce ONE consensus definition that focuses on the *measurement instrument itself*:
   - what instrument the name refers to (benchmark, dataset, user study, survey, human evaluation, etc.)
   - what procedure or task format it uses (e.g., multiple-choice QA, code generation, Likert-scale ratings, pairwise preference judgments, expert annotation, etc.)
   - what capability or construct it is intended to assess
2) De-emphasize metrics and reporting conventions:
   - do NOT define the instrument as “Accuracy (%)” / “score” / “EM/F1” etc.
   - do NOT include metric suffixes as part of the meaning of the instrument name
   - mention the metric only if it is genuinely definitional (rare)
3) Keep as much useful detail as possible about scope and variants (e.g., subsets, formats, participant populations, common task framing), without being unnecessarily long. Prefer 1–3 sentences when that suffices; use more only when needed to capture important specifics.
4) If snippets disagree about what exactly the instrument measures or how it is framed, incorporate that clearly (e.g., “some papers frame it as…”, “often used as…”), so the reader can see what varies.
5) If the snippets are too sparse, low-quality, or contradictory to form a consensus, output exactly: N/A
6) Do NOT invent facts. Do NOT add external knowledge. Use only the supplied snippets.
7) Prefer canonical names; do not introduce new names.

Output rules:
- Output MUST be a single plain-text definition (or exactly N/A).
- Do NOT output JSON.
- Do NOT output bullet points.
- Do NOT include any prefix like \"Consensus Definition:\".
"""

# Behavior/Task-focused variant:
# Summarize the observable behavior/task itself (what the model does), not the latent construct.
CONSENSUS_DEFINITION_TEXT_PROMPT_BEHAVIOR = """You are an expert scientific editor and behavior/task ontology curator.

Your task: write a high-quality CONSENSUS DEFINITION (plain text) for a single BEHAVIOR/TASK node in an AI nomological network, based ONLY on the provided extracted snippets from papers.

Node:
- canonical_name: {canonical_name}
- type: behavior

Snippets (JSON):
{definitions_json}

Requirements:
1) Produce ONE consensus definition that focuses on the *observable behavior/task itself*:
   - what is the task/behavior (what the system is doing or expected to do)
   - typical input/output format when it is described (if present in snippets)
   - what capability/trait it is commonly used to reflect (if present), without redefining it as the construct
2) Keep as much useful detail as possible about scope, variants, and contexts in which it appears, without being unnecessarily long. Prefer 1–3 sentences when that suffices; use more only when needed to capture important specifics.
3) If snippets disagree (e.g., some treat it as a benchmark task while others treat it as real-world behavior), incorporate that clearly by qualifying the definition (e.g., “often operationalized as…”, “some papers frame it as…”).
4) If the snippets are too sparse, low-quality, or contradictory to form a consensus, output exactly: N/A
5) Do NOT invent facts. Do NOT add external knowledge. Use only the supplied snippets.
6) Prefer canonical names; do not introduce new names.

Output rules:
- Output MUST be a single plain-text definition (or exactly N/A).
- Do NOT output JSON.
- Do NOT output bullet points.
- Do NOT include any prefix like \"Consensus Definition:\".
"""

CREATE_UNIFIED_NETWORK_PROMPT = """You are a research assistant creating a unified nomological network from aggregated constructs, measurement instruments, behaviors, and relationships across multiple papers.

Your task is to synthesize all the information into a coherent, well-structured nomological network that represents the collective knowledge from all papers.

**Instructions:**
1. Review all aggregated constructs, measurement instruments, behaviors, and relationships
2. Create a unified network structure that:
   - Includes all canonical constructs, measurement instruments, and behaviors
   - Preserves all relationships with their evidence
   - Organizes the network hierarchically where appropriate
   - Highlights the most frequently mentioned relationships
3. Ensure the network is logically consistent and well-organized

**Output Format:**
Return a JSON object matching the nomological network structure:
{
  "constructs": [
    {
      "name": "Canonical Construct Name",
      "description": "Unified definition",
      "paper_count": 5,
      "papers": ["Paper1", "Paper2", ...]
    }
  ],
  "measurements": [
    {
      "name": "Canonical Measurement Name",
      "description": "Unified description",
      "paper_count": 3,
      "papers": ["Paper1", "Paper3", ...]
    }
  ],
  "behaviors": [
    {
      "name": "Canonical Behavior Name",
      "description": "Unified description",
      "paper_count": 2,
      "papers": ["Paper2", "Paper4"]
    }
  ],
  "relationships": [
    {
      "source": "Construct Name",
      "target": "Measurement Name",
      "type": "related",
      "evidence": ["Aggregated quoted evidence from multiple papers"],
      "paper_count": 4,
      "papers": ["Paper1", "Paper2", "Paper3", "Paper4"]
    }
  ]
}

**Aggregated data:**
{aggregated_data_json}

Return only the JSON object, no additional text."""


MERGE_GROUPS_PROMPT = (
    """You are merging groups of {node_type} that were extracted from many academic papers and grouped in separate batches. Your job is to identify groups that refer to the same concept and merge them.

Each input group has an `id`. Output only the merge mapping as `{{canonical_name: [ids]}}`. All metadata (definitions, papers, snippets) is resolved from the IDs programmatically — do NOT repeat them.

**Canonical name:** concise, community-standard noun phrase, sentence case. For measurement instruments, include subset qualifier when applicable.

"""
    + _SHARED_MERGE_PRINCIPLE
    + """

**Output format:**
```json
{{"groups": {{"Reasoning": [0, 3, 7], "Mathematical reasoning": [1, 9], "MMLU": [2, 5]}}, "ungrouped": [4, 6]}}
```
`groups` maps each canonical name to the list of input IDs that merge under it. `ungrouped` lists IDs that don't merge with anything else. Every input ID must appear exactly once across groups + ungrouped. A single-member group (e.g. `"Foo": [12]`) is fine when you want to pick the canonical name for it.

**Input groups:**
{groups_json}

Return only the JSON object."""
)


AGGREGATE_RELATIONSHIPS_PROMPT = """You are a research assistant harmonizing relationships between constructs, measurement instruments, and behaviors extracted from multiple academic papers. Your goal is to deduplicate relationships that describe the same connection under different wordings, resolving them to canonical forms.

**Faithfulness:** Do not invent relationships or nodes. Only map and consolidate what appears in the input relationships and canonical groups.

Given relationships from different papers, your task is to:
1. Map source and target names to their canonical names using the provided harmonized groups
2. Deduplicate relationships (same canonical source-target-type pairs expressed differently)
3. Consolidate evidence from multiple papers for each canonical relationship

There are three types of relationships allowed: `related`, `causal`, and `correlation` - related is basically NOT causal or correlated, but related and important to capture.

**Context - Canonical Groups:**

**Constructs:**
{construct_groups_json}

**Measurement Instruments:**
{measurement_groups_json}

**Behaviors:**
{behavior_groups_json}

**Name Mapping (original -> canonical):**
{name_mapping_json}

**Relationships to aggregate (JSON array):**
{relationships_json}

**Instructions:**
1. For each relationship, map the source and target to canonical names using:
   - First check the name_mapping dictionary (direct mapping)
   - If not found in mapping, search through the groups lists to find which canonical name it belongs to
   - Use the canonical_name from the matching group
2. If multiple relationships have the same canonical source-target-type combination, consolidate them:
   - Combine all evidence into a list
   - List all papers that mention this relationship
   - Count how many papers support this relationship
3. Preserve unique relationships (different canonical source-target-type combinations)

**Allowed relationship `type` values (exactly one):** `related`, `causes`, `correlates`. Preserve the type from the input when mapping to canonical names; if unclear, use `related`.

**Output Format (JSON):**
{{
  "relationships": [
    {{
      "source": "Canonical Construct Name",
      "target": "Canonical Measurement Name",
      "type": "related",
      "evidence": [
        "Quoted evidence from Paper1 (p. 5)",
        "Quoted evidence from Paper2 (Sec. 3)"
      ],
      "papers": ["Paper1", "Paper2"],
      "paper_count": 2
    }},
    {{
      "source": "MMLU",
      "target": "Jailbreak robustness",
      "type": "correlates",
      "evidence": ["Association reported in Paper3 (Table 2)."],
      "papers": ["Paper3"],
      "paper_count": 1
    }}
  ]
}}

Return only the JSON object, no additional text."""

# ---------------------------------------------------------------------------
# Definition characterization prompt (batched)
# ---------------------------------------------------------------------------
CHARACTERIZE_ENTITIES_PROMPT = """You are characterizing one entity from a nomological network of LLM research. You receive:
- its **canonical name** and **type** (construct, measurement instrument, or behavior/task)
- every **original definition** extracted from different papers (with paper titles)
- every **source snippet** (verbatim quotes from papers)
- every **relationship** this entity participates in, with evidence quotes

**STRICT SCOPE — use ONLY the data provided in this prompt.** Do not draw on prior knowledge about the field, the entity, the benchmarks, or the papers. Every claim in your output must be supported by a definition, snippet, or relationship evidence that appears in the input for this entity. Do NOT add historical context, well-known facts, or general intuition that isn't present. If the provided data is sparse, the characterization should be short and faithful — do not pad it with outside knowledge.

Your task: write a rich **summary of use** (4-8 sentences) for this entity that reads as a mini literature review — synthesizing how the field defines, operationalizes, and relates to this concept **strictly as represented in the provided data**.

**What to emphasize (this is the heart of the characterization):**
- **Agreement and disagreement across papers.** Say which framings are most common and which are minority or contested. Use language like "the prevailing usage is…", "a smaller line of work treats it as…", "most papers operationalize it as…, though some define it as…", "almost all papers in this set…", "only a few authors…".
- **What is most vs least commonly said** about the entity — frequency-based framing wins over absolute claims.

**Type-specific emphases:**
- **For constructs (latent traits)**: explicitly describe how the field **operationalizes and measures** the construct — name the specific measurement instruments and behaviors that are used as evidence for it, drawing from the relationships in the input. Make the operationalization explicit; do not leave it abstract.
- **For behaviors (observable tasks/phenomena)**: explicitly describe how the field **operationalizes and measures** the behavior — what benchmarks/datasets/evaluation procedures are used to elicit and score it, drawing from the relationships in the input.
- **For measurement instruments (benchmarks, datasets, evaluation procedures)**: explicitly describe **what the instrument is stated to measure** — name the constructs and the behaviors it is positioned to assess, drawing from the relationships in the input. Be specific about the connection ("papers use it to measure …", "it is reported as evaluating …").

**Causal vs. associative language — be conservative:**
- **Default to associative language** for entities of the same kind: "is related to", "co-occurs with", "is studied alongside", "is contrasted with". Use these for construct↔construct or behavior↔behavior pairings unless the input papers very clearly and prevalently state a directional/causal claim.
- **Construct → behavior causal claims** (e.g., "X drives Y", "X causes Y") are appropriate only when the input papers state this strongly and across multiple papers. If only one or a few papers say it, frame it as "some papers argue…" or "is reported to influence…".
- **Measurement instruments → constructs/behaviors**: it is appropriate (and expected) to use directional measurement language such as "measures", "is used to assess", "evaluates", "operationalizes". This is how the field talks about instruments and you should reflect that clearly.

**Writing style:**
- Write as a field synthesis, NOT as a dictionary definition. Use language like "most commonly described as…", "some authors define it as…, though the prevailing usage is…", "across the surveyed work, the dominant framing is…".
- **Tone: descriptive and neutral — HARD CONSTRAINT.** NEVER use the words "crucial", "important", "essential", "significant", or "key" — even when paraphrasing a paper. Replace with frequency-based alternatives: "commonly", "widely", "frequently", "prevalent", "a recurring theme", "a popular instrument". If a paper says something is "crucial", paraphrase as "widely discussed" or "commonly targeted".
- Weave in **specific evidence**: quote or paraphrase findings from the source snippets when they illuminate how the concept is used (e.g. "As one study notes, '…' (Paper Title)").
- For entities with only one source paper, still provide a faithful description from all available data; do not pretend a single-paper concept is well-established.
- Do NOT start with "X is…" as a flat definition. Start with how the field treats the concept.

Be precise and grounded in the evidence. Do not invent information not present in the inputs. If you cannot support a claim with something from the provided definitions/snippets/relationships, do not make the claim.

**Output format — JSON object with one key (the entity's canonical name) mapped to its characterization string:**
```json
{{
  "Canonical Name": "Characterization text..."
}}
```

Return ONLY the JSON object.

**Entity to characterize:**
{entities_json}

---

**Self-check before returning (do this silently — only emit the final JSON):**
1. Re-read every sentence of your draft characterization.
2. For each claim, locate the specific definition, snippet, or relationship in the input that supports it. If you cannot point to one, REMOVE the claim or rewrite it to match what the data actually says.
3. Confirm you did not import outside knowledge — no historical context, no well-known facts about the field/benchmark/concept that aren't in the input, no general intuition, no statistics or numbers that aren't present.
4. Confirm frequency-based language is used wherever you describe how common a framing is (no "crucial", "important", "essential", "significant", "key").
5. Confirm causal/directional language is only used (a) measurement instruments → what they measure, or (b) construct → behavior claims that are stated strongly across multiple input papers. Otherwise use associative language ("is related to", "co-occurs with").
Then return the final JSON."""
