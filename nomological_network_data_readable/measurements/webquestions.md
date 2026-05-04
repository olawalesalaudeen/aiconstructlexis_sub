# WebQuestions
**Type:** Measurement  
**Referenced in:** 35 papers  
**Also known as:** WebQuestion, WebQS, WebQ, WebQs, Webquestions, Web Questions, WQA, web_questions  

## State of the Field

Across the provided literature, WebQuestions is consistently characterized as a benchmark for open-domain question answering (ODQA). The dataset is most frequently used to measure this capability, with several papers also using it to evaluate factual recall and, in one case, multi-hop question answering. A distinct line of work adapts the dataset to assess spoken question answering. Other framings describe it as a tool for evaluating "world knowledge retention" or "closed-book fact recall". The dataset's questions are consistently described as originating from web queries, such as the Google Suggest API, with answers being entities from the Freebase knowledge database. Operationally, it is employed in various few-shot settings, including zero-shot, 1-shot, and 5-shot evaluations, sometimes using an "exact match" metric. The benchmark appears under several names, including WebQ, WebQS, and WQA, but its core function remains centered on testing a model's ability to answer factual questions.

## Sources

**[BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)**
> An open-domain question answering dataset used to examine more generic QA performance.

**[Towards Green AI in Fine-tuning Large Language Models via Adaptive Backpropagation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b054fadf1ccd80b37d465f6082629934-Paper-Conference.pdf) (as "WebQuestion")**
> A generative question answering dataset used to evaluate models on open-domain QA tasks, referenced in the appendix for additional experiments.

**[CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf) (as "WebQS")**
> A question-answering benchmark used to evaluate world knowledge retention.

**[Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf) (as "WebQ")**
> The WebQuestions (WebQ) dataset, an open-domain question answering benchmark where questions are sourced from the web and answers are entities in Freebase.

**[Theory, Analysis, and Best Practices for Sigmoid Self-Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/a43b459e9fab3a703148ba0c83b8a442-Paper-Conference.pdf) (as "WebQs")**
> The WebQuestions dataset, which consists of questions from Google Search that can be answered using Freebase, testing open-domain question answering.

**[Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf) (as "Webquestions")**
> A question-answering dataset of questions from web users, used as an unseen evaluation task.

**[Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf) (as "Web Questions")**
> A dataset for spoken question answering that contains questions sourced from the web, requiring the model to provide factual answers.

**[Chain-of-Action: Faithful and Multimodal Question Answering through Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a0b1082fc7823c4c68abcab4fa850e9c-Paper-Conference.pdf) (as "WQA")**
> Web-based QA benchmark used to evaluate question answering over web information.

**[Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf) (as "web_questions")**
> Question answering dataset consisting of factual questions extracted from web queries, used to evaluate in-context learning performance.

## Relationships

### → WebQuestions
- **Open-domain question answering** (behaviors tasks) — *measured_by*
  > Moreover, in order to examine ToG on more generic tasks, we also prepare one open-domain QA dataset: WebQuestions (Berant et al., 2013);
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
- **Spoken question answering** (behaviors tasks) — *measured_by*
  > Spoken Question Answering ... We evaluate our model on 3 datasets in D´efossez et al. (2024): Web Questions (Berant et al., 2013), Llama Questions (Nachmani et al., 2024), and TriviaQA (Joshi et al., 2017).
  - [Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM](https://proceedings.iclr.cc/paper_files/paper/2024/file/e393677793767624f2821cec8bdd02f1-Paper-Conference.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
- **Knowledge recall** (behaviors tasks) — *measured_by*
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Aligning Spoken Dialogue Models from User Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25t/wu25t.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > The questions used for constructing our training data are sourced from the ASQA (Stelmakh et al., 2022), WebQuestions (Berant et al., 2013), and Natural Questions (Kwiatkowski et al., 2019) training splits. (Section 4.1.1)
  - [KS-Lottery: Finding Certified Lottery Tickets for Multilingual Transfer in Large Language Models](https://aclanthology.org/2025.naacl-long.459.pdf)
- **Knowledge graph question answering** (behaviors tasks) — *measured_by*
  - [PreP-OCR: A Complete Pipeline for Document Image Restoration and EnhancedOCRAccuracy](https://aclanthology.org/2025.acl-long.750.pdf)
- **QuALITY** (measurements) — *measured_by*
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
- **Factual recall** (behaviors tasks) — *measured_by*
  > We consider nine varied downstream tasks: ... (f) fact recall (WebQuestions (Berant et al., 2013), Natural Questions (Kwiatkowski et al., 2019))
  - [Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks](https://aclanthology.org/2025.naacl-long.618.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [Beyond One-Size-Fits-All: Tailored Benchmarks for Efficient Evaluation](https://aclanthology.org/2025.acl-long.760.pdf)
- **Multi-hop question answering** (behaviors tasks) — *measured_by*
  > We conduct experiments on five multi-hop QA datasets: HotPotQA (Yang et al., 2018), 2WikiMultiHopQA (2Wiki) (Ho et al., 2020), MuSiQue (Trivedi et al., 2022), Bamboogle (Press et al., 2023) and WebQuestions (WebQA) (Berant et al., 2013). (Section 4.1)
  - [LoGU: Long-form Generation with Uncertainty Expressions](https://aclanthology.org/2025.acl-long.929.pdf)
