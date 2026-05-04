# Zero-shot relation extraction (zsRE)
**Type:** Measurement  
**Referenced in:** 34 papers  
**Also known as:** ZSRE, zsRE, ZsRE, Zero-Shot RE  

## State of the Field

Across the provided literature, Zero-shot relation extraction (zsRE) is most prevalently used as a benchmark to evaluate knowledge editing in language models. In this context, papers use it to assess performance on tasks such as factual editing, knowledge insertion, and modification, with multiple sources referring to it as a "widely adopted" or "popular" model editing dataset. The instrument is frequently described as a question-answering benchmark derived from Wikipedia, containing either "short question-answer pairs" or instances with "a factual statement and a paraphrased prompt" (Grounding Fallacies Misrepresenting Scientific Publications in Evidence). Several papers explicitly state that while now common for editing, zsRE was "originally developed for zero-shot relation extraction" (Precise Localization of Memories...). A smaller set of studies continues to use it for this original purpose, which involves evaluating a model's ability to identify relations it has not been explicitly trained on. In this capacity, it is also used to measure the broader capability of Information extraction. In knowledge editing evaluations, it is frequently used alongside the CounterFact dataset.

## Sources

**[BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf) (as "ZSRE")**
> A dataset for zero-shot relation extraction, used to evaluate a model's ability to identify relations it has not been explicitly trained on.

**[Can Sensitive Information Be Deleted From LLMs? Objectives for Defending Against Extraction Attacks](https://proceedings.iclr.cc/paper_files/paper/2024/file/c652e5f62fd1f5acbbf0d6413a1113e7-Paper-Conference.pdf) (as "zsRE")**
> A question-answer benchmark derived from Wikipedia that is used here to test factual editing and extraction of specific answers.

**[Precise Localization of Memories: A Fine-grained Neuron-level Knowledge Editing Technique for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/01db36a646c07c64dd39a92b4eceb417-Paper-Conference.pdf) (as "ZsRE")**
> A dataset for knowledge editing evaluation, originally developed for zero-shot relation extraction, used here for knowledge insertion and modification tasks.

**[RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf) (as "Zero-Shot RE")**
> A zero-shot relation extraction benchmark used to test relation prediction without task-specific training.

## Relationships

### → Zero-shot relation extraction (zsRE)
- **Information extraction** (behaviors tasks) — *measured_by*
  - [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf)
