# Prompt: Extract Entities (Pass 1)

**Pipeline step:** Extraction — Phase 1  
**Models:** Gemini 2.5 Pro / GPT-5.4 Mini / Qwen 3.5-397B  
**Source:** `misc/prompts.py` → `EXTRACT_ENTITIES_PROMPT`  
**Called from:** `scripts/multi_model_mv.py` → `scripts/batch_majority_vote.py:build_entity_jsonl()`  

---

Your task is to act as a research assistant. Analyze the following academic paper and extract **entities only** (no relationships yet) for a **psychometric-style nomological network** for **Large Language Models (LLMs)**: abstract constructs, measurement instruments (benchmarks, user studies, surveys, and other evaluation procedures), and observable behaviors/tasks. **Faithfulness is more important than coverage**—if you cannot tie an item to a quote from the paper text, **omit** it.

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
- `name`: concise noun-phrase label (2–5 words typical).
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
```json
{
  "constructs": [
    {
      "name": "Spatial reasoning",
      "description": "The latent ability to mentally represent and manipulate spatial relationships between objects.",
      "source_snippets": [
        "\"we evaluate spatial reasoning through block-placement tasks\" (Sec. 3)"
      ]
    },
    {
      "name": "Robustness",
      "description": "The degree to which model performance is stable under input perturbations.",
      "source_snippets": [
        "\"robustness to adversarial rephrasings\" (Abstract)"
      ]
    }
  ],
  "measurements": [
    {
      "name": "BlocksWorld",
      "description": "Planning benchmark requiring multi-step block rearrangement.",
      "source_snippets": [
        "\"evaluated on BlocksWorld\" (Table 1)"
      ]
    },
    {
      "name": "User preference study",
      "description": "Human evaluation in which participants rate or rank model outputs on criteria such as helpfulness and coherence.",
      "source_snippets": [
        "\"we conducted a user study with 50 participants rating outputs\" (Sec. 5)"
      ]
    }
  ],
  "behaviors": [
    {
      "name": "Multi-step planning",
      "description": "Producing a sequence of actions to achieve a goal state from an initial state.",
      "source_snippets": [
        "\"the model generates step-by-step plans\" (Sec. 4)"
      ]
    }
  ]
}
```
