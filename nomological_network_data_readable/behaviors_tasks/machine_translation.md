# Machine translation
**Type:** Behavior  
**Referenced in:** 218 papers  
**Also known as:** Translation, Code transpilation, Classical Chinese to modern Chinese translation, Modern Chinese to classical Chinese translation, Ancient poetry translation, Ancient poetry to English translation, Zero-shot translation, Legal translation, Back-translation, Code translation, Context-dependent translation, Document translation, Transcreation, Speech translation, Transliteration, Concise translation, Monotonic translation, Self-translation, Pronoun translation, Proper noun translation, Multi-step translation, Language translation, Text translation, Dictionary-based translation, Gender-neutral translation, Lyrics translation, Speech-to-text translation, Text-only translation, Backtranslation, Domain-specific translation, Cross-lingual generation, Multi-domain translation, Cascaded speech translation, Code-switched translation, End-to-end speech translation, Explicit translation, Back translation, Spoken-only language translation, Paragraph-level translation, Pseudo-document translation, Sentence-level translation, Sentence translation, Forward translation, Loanword translation, Off-target translation, Braille-to-text translation, Gendered translation, Over-translation, Under-translation, Classical Chinese poetry translation, Cross-cultural translation, Multi-hop translation, Single-hop translation, Plain-text translation, Translation generation  

## State of the Field

Across the provided literature, machine translation is most commonly defined as the task of converting text from a source language to a target language. This behavior is operationalized and measured using a wide array of benchmarks, with the WMT series (e.g., WMT14, WMT19) and the FLORES family (e.g., FLORES-200, Flores-101) appearing as the most frequent instruments for evaluation across numerous language pairs. The task is examined at multiple granularities, including sentence-level, paragraph-level, and document-level translation. The concept is also extended to various modalities and domains, with specific sub-tasks defined for speech, code, legal texts, and even lyrics, each with its own set of challenges. Beyond these broad categories, a number of papers investigate more specific phenomena such as `Context-dependent translation`, `Pronoun translation`, and translation errors like `Over-translation` and `Under-translation`. Different processes are also described, including `Zero-shot translation` for unseen language pairs and `Back-translation`, which is used for data augmentation or as an adversarial attack. Some studies report that `Chain-of-thought reasoning` can produce more accurate translations, especially for multi-hop tasks. Finally, machine translation is studied alongside related concepts like `Stereotyping`, particularly in the context of `Gendered translation`.

## Sources

**[A Benchmark for Learning to Translate a New Language from One Grammar Book](https://proceedings.iclr.cc/paper_files/paper/2024/file/52d63f9e4b81f866bf69fb3c834aad47-Paper-Conference.pdf)**
> Translating text from one language to another, evaluated as both a held-in and generation task.

**[CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf) (as "Translation")**
> The task of converting text from a source language to a target language.

**[Verified Code Transpilation with LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/48bb60a0c0aebb4142bf314bd1a5c6a0-Paper-Conference.pdf) (as "Code transpilation")**
> The observable task of automatically transforming source code from one programming language to another.

**[WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Classical Chinese to modern Chinese translation")**
> The task of translating a given text from classical Chinese into modern Chinese.

**[WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Modern Chinese to classical Chinese translation")**
> The task of translating a given text from modern Chinese into classical Chinese.

**[WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Ancient poetry translation")**
> The task of translating ancient poetry into modern Chinese while preserving its meaning and sentiment.

**[WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Ancient poetry to English translation")**
> The task of translating ancient Chinese poetry into English.

**[Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf) (as "Zero-shot translation")**
> Translating text from a source language to a target language without any explicit training examples for that language pair.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Legal translation")**
> Translating legal texts between Chinese and English.

**[DPIC: Decoupling Prompt and Intrinsic Characteristics for LLM Generated Text Detection](https://proceedings.neurips.cc/paper_files/paper/2024/file/1d35af80e775e342f4cd3792e4405837-Paper-Conference.pdf) (as "Back-translation")**
> The task of translating a text to another language and then back to the original, used as an adversarial attack to test detector robustness.

**[IaC-Eval: A Code Generation Benchmark for Cloud Infrastructure-as-Code Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/f26b29298ae8acd94bd7e839688e329b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Code translation")**
> The observable task of converting a program from one programming language to another while preserving its functionality.

**[DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/285149554f6fbed6e2f9ec72d131bd23-Paper-Conference.pdf) (as "Context-dependent translation")**
> The task of translating ambiguous words or phrases that require surrounding text or discourse context for correct interpretation.

**[DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/285149554f6fbed6e2f9ec72d131bd23-Paper-Conference.pdf) (as "Document translation")**
> Generating a target language version of a source document, often sentence-by-sentence.

**[Mufu:  Multilingual Fused Learning for Low-Resource Translation with LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/b44ae90136013a8d0e2d24f6015b6097-Paper-Conference.pdf) (as "Transliteration")**
> The observable behavior of converting text from one writing system (script) into another, based on phonetic similarity.

**[Dynamic-SUPERB Phase-2: A Collaboratively Expanding Benchmark for Measuring the Capabilities of Spoken Language Models with 180 Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce1a7774429d5c06cc744ff4260a8e9f-Paper-Conference.pdf) (as "Speech translation")**
> Translating spoken language into another language.

**[Measuring And Improving Persuasiveness Of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf) (as "Transcreation")**
> The observable task of adapting a persuasive message for a new audience or context while maintaining the original message's core intent and persuasive goal.

**[Language Imbalance Driven Rewarding for Multilingual Self-improving](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cdee7247c410907b32fcbc12a605823-Paper-Conference.pdf) (as "Self-translation")**
> The task of a model translating its own generated responses from one language to another.

**[SimulPL: Aligning Human Preferences in Simultaneous Machine Translation](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5111676c19e5945473acf20ad7026f-Paper-Conference.pdf) (as "Monotonic translation")**
> The behavior of generating a translation where the target word order largely follows the source word order, minimizing reordering.

**[SimulPL: Aligning Human Preferences in Simultaneous Machine Translation](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5111676c19e5945473acf20ad7026f-Paper-Conference.pdf) (as "Concise translation")**
> The behavior of producing translations that are shorter than a literal rendering and focus on essential information points.

**[DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/285149554f6fbed6e2f9ec72d131bd23-Paper-Conference.pdf) (as "Pronoun translation")**
> The observable task of correctly translating pronouns, which often requires resolving coreferences using document-level context.

**[DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/285149554f6fbed6e2f9ec72d131bd23-Paper-Conference.pdf) (as "Proper noun translation")**
> The specific sub-task of translating named entities such as people, locations, and organizations from a source to a target language.

**[On the Power of Context-Enhanced Learning in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25p/zhu25p.pdf) (as "Multi-step translation")**
> The observable process of transforming an input string through a sequence of d translation steps, each involving a circular shift and a bijective mapping defined by a phrasebook, resulting in a final output string.

**[On Exact Bit-level Reversible Transformers Without Changing Architecture](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ao/zhang25ao.pdf) (as "Language translation")**
> Translating text from one language to another, specifically English to French in the paper's experiment.

**[Can We Predict Performance of Large Models across Vision-Language Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25y/zhao25y.pdf) (as "Text translation")**
> The task of translating text found within an image from one language to another.

**[Towards General-Domain Word Sense Disambiguation: Distilling Large Language Model into Compact Disambiguator](https://aclanthology.org/2025.emnlp-main.46.pdf) (as "Dictionary-based translation")**
> Producing translated text by incorporating external bilingual dictionaries into the prompt to guide word-level mappings during generation.

**[Astra: Efficient Transformer Architecture and Contrastive Dynamics Learning for Embodied Instruction Following](https://aclanthology.org/2025.emnlp-main.689.pdf) (as "Lyrics translation")**
> Producing translated lyric text from source lyrics, often under constraints of meaning, rhythm, and singability.

**[PRIM: Towards Practical In-Image Multilingual Machine Translation](https://aclanthology.org/2025.emnlp-main.692.pdf) (as "Gender-neutral translation")**
> The task of translating text into a target language using unmarked forms that do not specify gender, especially when the source text is ambiguous or refers to unspecified individuals.

**[Think and Recall: Layer-Level Prompting for Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.734.pdf) (as "Speech-to-text translation")**
> The task of transcribing spoken audio from a source language into written text in a different target language.

**[Measuring Risk of Bias in Biomedical Reports: TheRoBBRBenchmark](https://aclanthology.org/2025.emnlp-main.161.pdf) (as "Text-only translation")**
> Producing a translated output using only the source text as input, without any visual context.

**[MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation](https://aclanthology.org/2025.emnlp-main.80.pdf) (as "Backtranslation")**
> The process of converting buggy code into a natural language representation that captures its underlying logic and intent.

**[Large Language Models Do Multi-Label Classification Differently](https://aclanthology.org/2025.emnlp-main.127.pdf) (as "Domain-specific translation")**
> Translating text from a specialized domain into another language.

**[LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing](https://aclanthology.org/2025.emnlp-main.328.pdf) (as "Cross-lingual generation")**
> Producing text in a target language based on input in a different source language, such as translating from Arabic to English or vice versa.

**[JOLT-SQL: Joint Loss Tuning of Text-to-SQLwith Confusion-aware Noisy Schema Sampling](https://aclanthology.org/2025.emnlp-main.309.pdf) (as "Multi-domain translation")**
> Translating text between languages while correctly handling words whose meanings vary across different domains such as law, science, or news.

**[ReEvalMed: Rethinking Medical Report Evaluation by Aligning Metrics with Real-World Clinical Judgment](https://aclanthology.org/2025.emnlp-main.599.pdf) (as "Cascaded speech translation")**
> Translating speech by first transcribing it to text using ASR and then applying machine translation to the transcribed text.

**[ReEvalMed: Rethinking Medical Report Evaluation by Aligning Metrics with Real-World Clinical Judgment](https://aclanthology.org/2025.emnlp-main.599.pdf) (as "Code-switched translation")**
> The observable behavior of translating sentences where terms from a foreign language (e.g., English) are retained within the source text of another language.

**[ReEvalMed: Rethinking Medical Report Evaluation by Aligning Metrics with Real-World Clinical Judgment](https://aclanthology.org/2025.emnlp-main.599.pdf) (as "End-to-end speech translation")**
> Directly translating speech in one language to text in another without an intermediate transcription step.

**[Mind the Gap: HowBabyLMs Learn Filler-Gap Dependencies](https://aclanthology.org/2025.emnlp-main.762.pdf) (as "Explicit translation")**
> Translating an English word or answer into a specified target language when directly prompted to do so.

**[UltraIF: Advancing Instruction Following from the Wild](https://aclanthology.org/2025.emnlp-main.946.pdf) (as "Back translation")**
> The process of translating a text from a source language to a target language and then back to the source language to create a paraphrased version.

**[Discourse-Driven Code-Switching: Analyzing the Role of Content and Communicative Function inSpanish-English Bilingual Speech](https://aclanthology.org/2025.emnlp-main.1195.pdf) (as "Spoken-only language translation")**
> The observable task of generating a translation in a written high-resource language from an input sentence that is represented using the International Phonetic Alphabet (IPA) from a spoken-only language.

**[UnpackingLet Alone: Human-Scale Models Generalize to a Rare Construction in Form but not Meaning](https://aclanthology.org/2025.emnlp-main.1400.pdf) (as "Paragraph-level translation")**
> Translating entire paragraphs of text, which requires maintaining context and coherence beyond individual sentences.

**[MessIRve: A Large-ScaleSpanish Information Retrieval Dataset](https://aclanthology.org/2025.emnlp-main.1413.pdf) (as "Pseudo-document translation")**
> An observable task where a long document is split into fixed-size chunks of sentences, which are then translated as single units.

**[UnpackingLet Alone: Human-Scale Models Generalize to a Rare Construction in Form but not Meaning](https://aclanthology.org/2025.emnlp-main.1400.pdf) (as "Sentence-level translation")**
> Translating text one sentence at a time, often without access to the broader document context.

**[MessIRve: A Large-ScaleSpanish Information Retrieval Dataset](https://aclanthology.org/2025.emnlp-main.1413.pdf) (as "Sentence translation")**
> Translating individual sentences in isolation, without leveraging or preserving inter-sentential context.

**[Linguistic Neuron Overlap Patterns to Facilitate Cross-lingual Transfer on Low-resource Languages](https://aclanthology.org/2025.emnlp-main.1408.pdf) (as "Forward translation")**
> A data augmentation technique where monolingual data in a source language is translated by a model to create synthetic parallel data.

**[Attacking Misinformation Detection Using Adversarial Examples Generated by Language Models](https://aclanthology.org/2025.emnlp-main.1406.pdf) (as "Loanword translation")**
> The observable act of translating a loanword from the source language into its correct target-language equivalent, respecting orthographic and phonological norms.

**[MessIRve: A Large-ScaleSpanish Information Retrieval Dataset](https://aclanthology.org/2025.emnlp-main.1413.pdf) (as "Off-target translation")**
> Generating output in a language different from the intended target, such as producing English or another African language when translating into a specific African language.

**[ORPP: Self-Optimizing Role-playing Prompts to Enhance Language Model Capabilities](https://aclanthology.org/2025.emnlp-main.1454.pdf) (as "Braille-to-text translation")**
> The observable task of converting a sequence of Braille symbols into its corresponding plain text representation.

**[Africa Health Check: Probing Cultural Bias in MedicalLLMs](https://aclanthology.org/2025.emnlp-main.1640.pdf) (as "Gendered translation")**
> The observable act of assigning a masculine or feminine grammatical form to an occupation in translation when the source term is gender-ambiguous.

**[DetectingLLMHallucination Through Layer-wise Information Deficiency: Analysis of Ambiguous Prompts and Unanswerable Questions](https://aclanthology.org/2025.emnlp-main.1645.pdf) (as "Over-translation")**
> The observable behavior where the model generates content not present in the source text, such as hallucinated or redundant sentences.

**[DetectingLLMHallucination Through Layer-wise Information Deficiency: Analysis of Ambiguous Prompts and Unanswerable Questions](https://aclanthology.org/2025.emnlp-main.1645.pdf) (as "Under-translation")**
> The observable behavior where content from the source text is missing in the model's translation output.

**[Language Models Identify Ambiguities and Exploit Loopholes](https://aclanthology.org/2025.emnlp-main.1678.pdf) (as "Classical Chinese poetry translation")**
> Producing English translations of classical Chinese poems while preserving meaning, rhyme, structure, and aesthetic qualities.

**[Word Salad Chopper: Reasoning Models Waste A Ton Of Decoding Budget On Useless Repetitions, Self-Knowingly](https://aclanthology.org/2025.emnlp-main.1706.pdf) (as "Cross-cultural translation")**
> The task of translating text from a source language to a target language while also adapting culture-specific entities to ensure relevance and comprehension for the target audience.

**[DIWALI- Diversity and Inclusivity aWare cuLture specific Items forIndia: Dataset and Assessment ofLLMs for Cultural Text Adaptation inIndian Context](https://aclanthology.org/2025.emnlp-main.1707.pdf) (as "Multi-hop translation")**
> Given a source text and intermediate bilingual dictionaries, the model translates across multiple synthetic languages.

**[DIWALI- Diversity and Inclusivity aWare cuLture specific Items forIndia: Dataset and Assessment ofLLMs for Cultural Text Adaptation inIndian Context](https://aclanthology.org/2025.emnlp-main.1707.pdf) (as "Single-hop translation")**
> Given a source text in one synthetic language, the model translates it into another language using a direct bilingual dictionary.

**[Multilinguality Does not Make Sense: Investigating Factors Behind Zero-Shot Cross-Lingual Transfer in Sense-Aware Tasks](https://aclanthology.org/2025.emnlp-main.1774.pdf) (as "Literal translation")**
> Translating text word-for-word or phrase-by-phrase without adapting to natural expression in the target language, often resulting in less fluent output.

**[Can a Single Model Master Both Multi-turn Conversations and Tool Use?CoALM: A Unified Conversational Agentic Language Model](https://aclanthology.org/2025.acl-long.606.pdf) (as "Plain-text translation")**
> Translating the textual content of a document image after removing non-textual elements like formulas and tables, focusing on linguistic accuracy.

**[Limited Generalizability in Argument Mining: State-Of-The-Art Models Learn Datasets, Not Arguments](https://aclanthology.org/2025.acl-long.1165.pdf) (as "Translation generation")**
> The observable task of producing a target language text given a source language text as input.

## Relationships

### Machine translation →
- **FLORES-200** (measurements) — *measured_by*
  > We utilize the Flores-200 (Team, 2022) Assamese-to-English translation dataset for low-resource translation. (Section 4.1)
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
- **FLORES** (measurements) — *measured_by*
  > We also test eng–npi and gug translation, low-resource languages with an established evaluation set, FLORES (Costa-jussà et al., 2024) and likely a low data weight in LLMs; while not unseen, these experiments broaden our results to seen low-resource languages more generally. (Section 3.1)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **Flores-101** (measurements) — *measured_by*
  > We perform the same interventions on the Flores-101 dataset (Goyal et al., 2022), which provides aligned translations across 101 languages. We present a selection of qualitative examples in Figure 7. (Section 4.3)
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
- **WMT14 en-de** (measurements) — *measured_by*
  > To evaluate GKD beyond summarization, we consider the task on translating English to German using WMT14 en-de (Bojar et al., 2014). (Section 4.2).
  - [When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2ad28981782bb62f025d2893791b629-Paper-Conference.pdf)
- **WMT14** (measurements) — *measured_by*
  > we select real-world datasets for various tasks, including ... WMT’14 De-En (Bojar et al., 2014) for translation (Section 6)
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **CoVoST 2** (measurements) — *measured_by*
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
- **WMT16** (measurements) — *measured_by*
  > We distill the pre-trained mBART students for the downstream task of translation from English to Romanian using the WMT16 dataset (Bojar et al., 2016). (Section 3.2)
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **IWSLT 2017** (measurements) — *measured_by*
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
- **Opus-100** (measurements) — *measured_by*
  - [Error Norm Truncation: Robust Training in the Presence of Data Noise for Text Generation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf)
- **IWSLT2017** (measurements) — *measured_by*
  - [Improving Language Model Distillation through Hidden State Matching](https://proceedings.iclr.cc/paper_files/paper/2025/file/2fb462e23667ad5e6471a4e9af8e4774-Paper-Conference.pdf)
- **WMT19** (measurements) — *measured_by*
  > We use WMT14 (Bojar et al., 2014), IWSLT14 (Cettolo et al., 2014), afroMT (Reid et al., 2021), IWSLT17 (Cettolo et al., 2017), WMT18 (Bojar et al., 2018), and WMT19 (Barrault et al., 2019) for machine translation (Section 4.1)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **WMT** (measurements) — *measured_by*
  > "We supervised ﬁne-tune these models on three tasks: WMT EN→DE translation (Bojar et al., 2014), CNN/DM summarization (Hermann et al., 2015), and XSum abstractive summarization"
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
- **XNLI** (measurements) — *measured_by*
  - [Heads up! Large Language Models Can Perform Tasks Without Your Instruction via Selective Attention Head Masking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25l/han25l.pdf)
- **Spec-Bench** (measurements) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
- **COMETKIWI** (measurements) — *measured_by*
  - [Reranking Laws for Language Generation: A Communication-Theoretic Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/c8b2f897e45770595656a79a9ad91e89-Paper-Conference.pdf)
- **WMT18** (measurements) — *measured_by*
  > We use WMT14 (Bojar et al., 2014), IWSLT14 (Cettolo et al., 2014), afroMT (Reid et al., 2021), IWSLT17 (Cettolo et al., 2017), WMT18 (Bojar et al., 2018), and WMT19 (Barrault et al., 2019) for machine translation (Section 4.1)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **MQM** (measurements) — *measured_by*
  - [Learning from others’ mistakes: Finetuning machine translation models with span-level error annotations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25p/zhang25p.pdf)
- **FLEURS-ASL** (measurements) — *measured_by*
  - [Examining and Adapting Time for Multilingual Classification via Mixture of Temporal Experts](https://aclanthology.org/2025.naacl-long.314.pdf)
- **WMT23** (measurements) — *measured_by*
  - [LAuReL: Learned Augmented Residual Layer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/menghani25a/menghani25a.pdf)
- **MuST-C** (measurements) — *measured_by*
  - [Crowdsource, Crawl, or Generate? CreatingSEA-VL, a Multicultural Vision-Language Dataset forSoutheastAsia](https://aclanthology.org/2025.acl-long.917.pdf)
- **HumanEval-X** (measurements) — *measured_by*
  - [PAK-UCB Contextual Bandit: An Online Learning Approach to Prompt-Aware Selection of Generative Models and LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25m/hu25m.pdf)
- **NTREX-128** (measurements) — *measured_by*
  > We include a diverse set of test examples, ranging from documents (Federmann et al., 2022)... (Section 3.2)
  - [AFRIDOC-MT: Document-levelMTCorpus forAfrican Languages](https://aclanthology.org/2025.emnlp-main.1414.pdf)
- **FLEURS** (measurements) — *measured_by*
  - [TokenSkip: Controllable Chain-of-Thought Compression inLLMs](https://aclanthology.org/2025.emnlp-main.166.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Language Models Identify Ambiguities and Exploit Loopholes](https://aclanthology.org/2025.emnlp-main.1678.pdf)
- **WMT24++** (measurements) — *measured_by*
  > We evaluated all our original baseline models on WMT24(de, cs, zh, ru) and also included a few-shot prompting on base model as an additional baseline for comparison with our proposed method. (Section 5)
  - [Paired by the Teacher: Turning Unpaired Data into High-Fidelity Pairs for Low-Resource Text Generation](https://aclanthology.org/2025.emnlp-main.1031.pdf)

### → Machine translation
- **Knowledge transferability** (constructs) — *measured_by*
  - [Mutual-Taught](https://aclanthology.org/2025.acl-long.795.pdf)
- **Chain-of-thought reasoning** (constructs) — *causes*
  > This indicates that the reasoning-based approach of LLMs can generate more accurate translations across multiple domains. (Section 3.1)
  - [DIWALI- Diversity and Inclusivity aWare cuLture specific Items forIndia: Dataset and Assessment ofLLMs for Cultural Text Adaptation inIndian Context](https://aclanthology.org/2025.emnlp-main.1707.pdf)

### Associated with
- **Text generation** (behaviors tasks)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Instruction following** (constructs)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **Speech recognition** (behaviors tasks)
  - [ReEvalMed: Rethinking Medical Report Evaluation by Aligning Metrics with Real-World Clinical Judgment](https://aclanthology.org/2025.emnlp-main.599.pdf)
- **Adaptability** (constructs)
  - [HICode: Hierarchical Inductive Coding withLLMs](https://aclanthology.org/2025.emnlp-main.1581.pdf)
- **Naturalness** (constructs)
  > Early frameworks propose strategies ranging from literal translation to complete adaptation, guided by the “Pentathlon Principle” (singability, sense, naturalness, rhythm, and rhyme). (Section 2)
  - [Astra: Efficient Transformer Architecture and Contrastive Dynamics Learning for Embodied Instruction Following](https://aclanthology.org/2025.emnlp-main.689.pdf)
- **Stereotyping** (constructs)
  > Machine Translation systems have become indispensable tools for cross-linguistic communication, yet they frequently exhibit gender biases that reinforce societal stereotypes (Blodgett et al., 2020; Menis-Mastromichalakis et al., 2025). (Section 1)
  - [Africa Health Check: Probing Cultural Bias in MedicalLLMs](https://aclanthology.org/2025.emnlp-main.1640.pdf)
