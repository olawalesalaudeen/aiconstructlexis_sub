# SST-2
**Type:** Measurement  
**Referenced in:** 114 papers  
**Also known as:** SST2  

## State of the Field

Across the provided literature, SST-2 is predominantly used as a benchmark to measure sentiment analysis. It is consistently operationalized as a binary text classification task where models must predict whether sentences, typically from movie reviews, have a “positive” or “negative” sentiment. The benchmark is frequently cited as a component of the GLUE collection, where it is used to evaluate broader natural language understanding capabilities. While most papers use SST-2 for standard performance evaluation through fine-tuning or in-context learning, a smaller body of work employs it to assess other model properties. For example, some studies use it to measure adversarial robustness by applying character-level attacks to the data. It is also used to evaluate general downstream task performance in studies on model alignment and safety. Finally, papers utilize it as a source of both in-distribution and out-of-domain data to assess model generalization.

## Sources

**[An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)**
> A sentiment classification benchmark used to evaluate binary sentiment prediction.

**[Shh, don't say that! Domain Certification in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/27befed4547edcb4bdeacef9472cadee-Paper-Conference.pdf) (as "SST2")**
> The Stanford Sentiment Treebank v2, a dataset for sentiment analysis, used here as a source of out-of-domain samples for the Shakespeare task.

## Relationships

### → SST-2
- **Sentiment analysis** (behaviors tasks) — *measured_by*
  > “Fine-tuning pre-trained language models (LMs) is a crucial step in a wide range of natural language processing tasks, including text classification and sentiment analysis”
  - [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf)
- **Text classification** (behaviors tasks) — *measured_by*
  > We use eight text classification datasets for ID data: SST-2 (SST; Socher et al., 2013), Subjectivity (SUBJ; Pang & Lee, 2004), AG-News (AGN; Zhang et al., 2015), and TREC (TREC; Li & Roth, 2002), BigPatent (BP; Sharma et al., 2019), AmazonReviews (AR; McAuley et al., 2015), MovieGenre (MG; Maas et al., 2011), 20NewsGroups (NG; Lang, 1995). (Section 4.1)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **Adversarial robustness** (constructs) — *measured_by*
  > To evaluate whether Evoke can improve LLMs’ robustness, we add typos to the datasets. Specifically, we perform character-level adversarial attacks for each sample. (Section 4.2)
  - [Evoke: Evoking Critical Thinking Abilities in LLMs via Reviewer-Author Prompt Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/1eaa5146756be028ad6fff1efcc8e6bd-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > Together, these benchmarks provide a well-rounded evaluation of language understanding, covering reasoning, sentiment, social context, and word meaning.
  - [LoRA-One: One-Step Full Gradient Could Suffice for Fine-Tuning Large Language Models, Provably and Efficiently](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ax/zhang25ax.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [Improving Dialogue State Tracking through Combinatorial Search for In-Context Examples](https://aclanthology.org/2025.acl-long.1394.pdf)
- **Generalization** (constructs) — *measured_by*
  - [CSR-Bench: BenchmarkingLLMAgents in Deployment of Computer Science Research Repositories](https://aclanthology.org/2025.naacl-long.634.pdf)
- **Out-of-distribution robustness** (constructs) — *measured_by*
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
- **Downstream task performance** (behaviors tasks) — *measured_by*
  > For fine-tuning tasks, we consider four different datasets, i.e., SST2, AGNEWS, GSM8K and AlpacaEval. (Sec. 5.1)
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)

### Associated with
- **GLUE** (measurements)
  > we consider the following five challenging tasks in GLUE dataset (Wang et al., 2018): Sentiment Analysis (SST-2)...
  - [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf)
