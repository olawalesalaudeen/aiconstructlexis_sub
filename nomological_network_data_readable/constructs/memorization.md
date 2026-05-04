# Memorization
**Type:** Construct  
**Referenced in:** 166 papers  
**Also known as:** Working memory, Memorization capacity, Recitation, Memorability, Memorisation, Memory capacity, Long-context memory, Episodic memory, Semantic memory, Inadvertent memorization, Long-term memorization, Memorization propensity, Factual memory, Effective remembrance, Training data regurgitation, Verbatim Reproduction, Verbatim text extraction, Plagiarism, Code reproduction, Quotation reproduction, Text reproduction, Context parroting, Verbatim regurgitation, Memorability simulation, Training data leakage, Verbatim recall, Secret canary recovery, Exact sequence reproduction, Literal copying  

## State of the Field

Memorization is prevalently characterized as a model's latent ability to store and reproduce content from its training data, often verbatim or near-verbatim. The most common framing places it in opposition to generalization, with numerous papers investigating whether model performance stems from genuine ability or simply recalling training examples, as one study asks: "Are the model’s results stemming from genuine ability or just memorization of the training data?" (DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks). While frequently viewed as a failure of generalization, a smaller line of work considers it a potentially "valuable behavior" for storing "useful patterns and association rules" (Scaling Laws for Associative Memories). The construct is operationalized by observing behaviors such as "verbatim regurgitation," "training data leakage," and "plagiarism." Researchers measure these behaviors using a range of instruments, including MMLU for factual knowledge, The Pile for extractable training samples, and the Dolos tool for detecting code plagiarism. Across the literature, memorization is frequently linked to undesirable outcomes; it is reported to cause privacy leakage and overfitting, and is studied alongside data contamination. A subset of papers also employs analogies to human cognition, defining related concepts like "working memory" for in-context information manipulation and "episodic memory" for recalling past interactions. The propensity for memorization is associated with model properties, with some papers noting that "larger models... are more likely to memorize" (Detecting Pretraining Data from Large Language Models).

## Sources

**[AutomaTikZ: Text-Guided Synthesis of Scientific Vector Graphics with TikZ](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7641940c7dd9e5de58c20e39586eb64-Paper-Conference.pdf)**
> The latent ability of an LLM to encode and retain information from a context in compressed form, analogous to human memory encoding, allowing for reconstruction or task performance based on partial or compressed representations.

**[In-context Autoencoder for Context Compression in a Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2024/file/0b276510ec2d3f6613a8b60c41ff0438-Paper-Conference.pdf) (as "Working memory")**
> An analogy for the LLM's capacity to hold and manipulate information within its context window to perform tasks, akin to the cognitive science concept.

**[Algorithmic Capabilities of Random Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/bccdd196d798a51a4961989984a9ed4a-Paper-Conference.pdf) (as "Memorization capacity")**
> The extent to which a model can store arbitrary input-output associations in its trainable parameters.

**[Recite, Reconstruct, Recollect: Memorization in LMs as a Multifaceted Phenomenon](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbd87a328be4c7e43aa0b900a0ebf79a-Paper-Conference.pdf) (as "Recitation")**
> A type of memorization characterized by the verbatim reproduction of sequences that are highly duplicated in the training corpus.

**[Teaching Human Behavior Improves Content Understanding Abilities Of VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0d8e47e50fa0ef219c61d6fb9f2a4b3-Paper-Conference.pdf) (as "Memorability")**
> The property of media content that determines its likelihood of being remembered by viewers, inferred from human behavior signals.

**[VisCGEC: Benchmarking the VisualChinese Grammatical Error Correction](https://aclanthology.org/2025.naacl-long.262.pdf) (as "Memorisation")**
> The extent to which a model has stored and can recall specific instances from its training data, rather than generating novel responses based on generalized knowledge.

**[ConstraintLLM: A Neuro-Symbolic Framework for Industrial-Level Constraint Programming](https://aclanthology.org/2025.emnlp-main.810.pdf) (as "Memory")**
> The ability to retain, manage, and recall past observations, actions, and experiences to inform current and future decision-making.

**[Step Guided Reasoning: Improving Mathematical Reasoning using Guidance Generation and Step Reasoning](https://aclanthology.org/2025.emnlp-main.1069.pdf) (as "Memory capacity")**
> The amount of historical conversational information a model can retain and access over long-term interactions, reflecting the breadth and persistence of stored knowledge.

**[ProbingLLMWorld Models: Enhancing Guesstimation with Wisdom of Crowds Decoding](https://aclanthology.org/2025.emnlp-main.235.pdf) (as "Long-context memory")**
> The ability of a model to effectively recall, process, and utilize information from very long input sequences.

**[Case-Based Decision-Theoretic Decoding with Quality Memories](https://aclanthology.org/2025.emnlp-main.1711.pdf) (as "Episodic memory")**
> The latent ability of an LLM to recall specific past user interactions or events, analogous to human autobiographical memory, used to inform contextually relevant responses.

**[Case-Based Decision-Theoretic Decoding with Quality Memories](https://aclanthology.org/2025.emnlp-main.1711.pdf) (as "Semantic memory")**
> The latent ability of an LLM to encode and utilize abstract, generalized knowledge about a user’s beliefs and preferences, derived from long-term engagement patterns.

**[Understanding Input Selectivity in Mamba: Impact on Approximation Power, Memorization, and Associative Recall Capacity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ab/huang25ab.pdf) (as "Long-term memorization")**
> The capacity of a model to retain information from earlier in a sequence over long durations, despite potential exponential decay in sensitivity to past inputs.

**[Watch Out Your Album! On the Inadvertent Privacy Memorization in Multi-Modal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ju25a/ju25a.pdf) (as "Inadvertent memorization")**
> The latent tendency of MLLMs to encode private, task-irrelevant information into their parameters due to spurious correlations formed during mini-batch training, even when such information provides no benefit for the downstream task.

**[Underestimated Privacy Risks for Minority Populations in Large Language Model Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25d/wei25d.pdf) (as "Memorization propensity")**
> The latent tendency of a model to strongly encode and retain specific training data points, especially those that are rare or outlier-like, making them harder to unlearn.

**[Understanding and Improving Length Generalization in Recurrent Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/buitrago25a/buitrago25a.pdf) (as "Effective remembrance")**
> The degree to which a model's output at a given position is influenced by tokens from earlier parts of the context.

**[From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf) (as "Factual memory")**
> The latent ability of a model to accurately recall and retrieve specific, isolated pieces of knowledge, such as entity attributes or simple facts.

**[Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf) (as "Verbatim Reproduction")**
> Generating exact substrings present in the training data, indicating potential copyright infringement.

**[Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf) (as "Training data regurgitation")**
> Reproducing training examples or their targets in model outputs when prompted with related context.

**[Follow My Instruction and Spill the Beans: Scalable Data Extraction from Retrieval-Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/79cafa874121a3435d8a54f454b646b4-Paper-Conference.pdf) (as "Verbatim text extraction")**
> Producing retrieved datastore text nearly unchanged in the model output.

**[MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://proceedings.iclr.cc/paper_files/paper/2025/file/7e3767db483c942b883eb4f8cfb74e31-Paper-Conference.pdf) (as "Plagiarism")**
> The act of submitting code that is highly similar to existing public solutions, such as those found in public Kaggle notebooks.

**[Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf) (as "Code reproduction")**
> Generating code or configuration text that matches existing online code snippets.

**[Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf) (as "Quotation reproduction")**
> The act of generating verbatim quotations from sources like interviews or movies, sometimes with incorrect or missing attribution.

**[Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf) (as "Text reproduction")**
> Producing output that contains verbatim substrings found in existing web text or training-data proxies.

**[Mitigating Memorization in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e50ff94d174465348f15c45760f58f9f-Paper-Conference.pdf) (as "Verbatim regurgitation")**
> The observable act of a language model generating text that is an exact, word-for-word copy of a sequence from its training data.

**[Zero-shot forecasting of chaotic systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea4d65c59073e8faf79222654d25fbe2-Paper-Conference.pdf) (as "Context parroting")**
> An observable mechanism where the model's forecast is generated by repeating or closely mimicking subsequences from the provided input context.

**[Teaching Human Behavior Improves Content Understanding Abilities Of VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0d8e47e50fa0ef219c61d6fb9f2a4b3-Paper-Conference.pdf) (as "Memorability simulation")**
> The task of predicting how memorable a given image or video will be to human viewers, often quantified as a memorability score.

**[Minerva: A Programmable Memory Test Benchmark for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xia25c/xia25c.pdf) (as "Verbatim recall")**
> Reproducing the entire memory content as a verbatim copy.

**[Trustworthy Machine Learning through Data-Specific Indistinguishability](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25h/xiao25h.pdf) (as "Secret canary recovery")**
> The task of a model generating specific secret digits (a 'canary') that were inserted into the training data, when prompted with the prefix of the secret phrase.

**[Trustworthy Machine Learning through Data-Specific Indistinguishability](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25h/xiao25h.pdf) (as "Exact sequence reproduction")**
> The task of a model exactly generating a specific number of subsequent tokens from a training example when prompted with a preceding sequence of tokens from that same example.

**[Interpreting the Repeated Token Phenomenon in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yona25a/yona25a.pdf) (as "Training data leakage")**
> The model outputs verbatim or paraphrased segments of its training data when triggered by repeated tokens or cluster-based inputs, indicating unintended memorization exposure.

**[Position: Iterative Online-Offline Joint Optimization is Needed to Manage Complex LLM Copyright Risks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25i/pan25i.pdf) (as "Literal copying")**
> The act of a model generating content that is a verbatim or near-verbatim copy of copyrighted material.

## Relationships

### Memorization →
- **Generalization** (constructs) — *causes*
  > Recent advances in grokking have demonstrated that neural networks can transition from memorizing to perfectly generalizing once they detect underlying logical patterns – yet these studies have primarily used small, synthetic tasks. (Abstract)
  - [DARG: Dynamic Evaluation of Large Language Models via Adaptive Reasoning Graph](https://proceedings.neurips.cc/paper_files/paper/2024/file/f5198bc255e1d5f959edd6d1d1a86fab-Paper-Conference.pdf)
- **Privacy leakage** (behaviors tasks) — *causes*
  > Based on prior research on LLMs’ ability to memorize training data (Carlini et al., 2021; Nasr et al., 2023; Kassem et al., 2024), we examine how PII embedded in training data from other aligned mergers can be extracted in model merging scenarios. (Section 1)
  - [Proactive Privacy Amnesia for Large Language Models: Safeguarding PII with Negligible Impact on Model Utility](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c234d9c7e738a793947e0282c36eb95-Paper-Conference.pdf)
- **Overfitting** (constructs) — *causes*
  > This result suggests that some of the reason for overﬁtting is due to partial memorization of the test set. (Section 5.4)
  - [A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://proceedings.neurips.cc/paper_files/paper/2024/file/53384f2090c6a5cac952c598fd67992f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AUXDATASET** (measurements) — *measured_by*
  > We thus call a subsequence of a generation memorized if (as in Deﬁnition 1) a 50-token-length subsequence exactly appears in AUXDATASET. (Section 3)
  - [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf)
- **Dolos** (measurements) — *measured_by*
  > To prevent plagiarism, we use the source code plagiarism detection tool Dolos (Maertens et al., 2024) to compare the agent’s submitted code against the top 50 associated notebooks from the relevant Kaggle competition.
  - [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://proceedings.iclr.cc/paper_files/paper/2025/file/7e3767db483c942b883eb4f8cfb74e31-Paper-Conference.pdf)
- **SUN** (measurements) — *measured_by*
  - [Teaching Human Behavior Improves Content Understanding Abilities Of VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0d8e47e50fa0ef219c61d6fb9f2a4b3-Paper-Conference.pdf)
- **In-context learning** (constructs) — *causes*
  - [Toward Understanding In-context vs. In-weight Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ae338b3fe6624798efa80b6581924028-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  > Memorization was evaluated using a subset of the MMLU benchmark focused on factual knowledge domains
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
- **LIMA** (measurements) — *measured_by*
  > Finally, we explore RLHF memorization on different task domains by studying memorization on natural language datasets, LIMA (Zhou et al., 2024) and Anthropic HH (Bai et al., 2022). (Section 5.5)
  - [Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf)
- **Anthropic HH (RLHF)** (measurements) — *measured_by*
  - [Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf)
- **Privacy vulnerability** (constructs) — *causes*
  - [DocMIA: Document-Level Membership Inference Attacks against DocVQA Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/231a8daf4f64935d0c7c6586f290b24f-Paper-Conference.pdf)
- **The Pile** (measurements) — *measured_by*
  > This dataset contains all 32-extractable samples from the Pile, verified by referencing the training data (Gao et al., 2020).
  - [Recite, Reconstruct, Recollect: Memorization in LMs as a Multifaceted Phenomenon](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbd87a328be4c7e43aa0b900a0ebf79a-Paper-Conference.pdf)
- **Natural Questions** (measurements) — *measured_by*
  - [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf)
- **PopQA** (measurements) — *measured_by*
  - [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf)
- **LongMemEval** (measurements) — *measured_by*
  - [ProbingLLMWorld Models: Enhancing Guesstimation with Wisdom of Crowds Decoding](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **HELMET** (measurements) — *measured_by*
  - [ProbingLLMWorld Models: Enhancing Guesstimation with Wisdom of Crowds Decoding](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **G-Eval** (measurements) — *measured_by*
  - [Step Guided Reasoning: Improving Mathematical Reasoning using Guidance Generation and Step Reasoning](https://aclanthology.org/2025.emnlp-main.1069.pdf)

### → Memorization
- **BookMIA** (measurements) — *measured_by*
  > We use the BookMIA dataset (Shi et al., 2023), which consists of text excerpts from books published in 2023 (after the knowledge cutoff of the models we study) as examples of unseen text, and passages from popular books as memorized examples (Chang et al., 2023). (Section 4.1)
  - [Towards Efficient and Multifaceted Computer-assisted Pronunciation Training Leveraging Hierarchical Selective State Space Model and Decoupled Cross-entropy Loss](https://aclanthology.org/2025.naacl-long.99.pdf)
- **Length generalization** (constructs) — *measured_by*
  - [Understanding and Improving Length Generalization in Recurrent Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/buitrago25a/buitrago25a.pdf)

### Associated with
- **Generalization** (constructs)
  > Disentangling the effects of generalization and test set memorization is critical to our understanding of language model performance, but this is becoming increasingly difficult as the pretraining datasets are rarely public for many of the LMs deployed today. (Section 1)
  - [AutomaTikZ: Text-Guided Synthesis of Scientific Vector Graphics with TikZ](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7641940c7dd9e5de58c20e39586eb64-Paper-Conference.pdf)
- **Data contamination** (constructs)
  > This post-cutoff performance degradation provides evidence of contamination and/or memorization of pre-cutoff problems from Codeforces and Project Euler by GPT-3.5-Turbo and GPT-4. (Section 5.1)
  - [To the Cutoff... and Beyond? A Longitudinal Perspective on LLM Data Contamination](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d04d97593c8c33d415337f408ed0e1b-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs)
  > However, the ability to recover from or correct errors in the reasoning process is generally poor across most models. This can be attributed to data memorization and potential contamination in training datasets, where models may have encountered similar/same problems before.
  - [Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5f30296296d2ae402ebbd09aaa9c12-Paper-Conference.pdf)
- **Text generation** (behaviors tasks)
  > we observe that LISA is much better than LoRA at memorization-centered tasks, such as Writing or depicting image details, while this gap is much smaller in reasoning-centered tasks like Code or Math (Section 5).
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **MATH** (measurements)
  > “we saw no clear signs of our models memorizing MATH problems.”
  - [Llemma: An Open Language Model for Mathematics](https://proceedings.iclr.cc/paper_files/paper/2024/file/b225f5c7cd13615e9558c3931fa4e66f-Paper-Conference.pdf)
- **Verbatim memorization** (constructs)
  - [Proving Test Set Contamination in Black-Box Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/46e624c244cff669223d488defd4e835-Paper-Conference.pdf)
- **Grokking** (constructs)
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
- **Out-of-distribution generalization** (constructs)
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
- **Data leakage** (constructs)
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)
- **Knowledge recall** (behaviors tasks)
  - [Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/11715d433f6f8b9106baae0df023deb3-Paper-Conference.pdf)
- **Image generation** (behaviors tasks)
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **Instruction generation** (behaviors tasks)
  - [Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/be06e3802e9411381feece79b4d960c1-Paper-Conference.pdf)
- **Visual perception** (constructs)
  - [Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf)
- **Unlearning** (constructs)
  - [Towards Effective Evaluations and Comparisons for LLM Unlearning Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/3a91841d2bcc0b13a3d0d5d60c9f0581-Paper-Conference.pdf)
- **In-context learning** (constructs)
  - [Zero-shot forecasting of chaotic systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea4d65c59073e8faf79222654d25fbe2-Paper-Conference.pdf)
- **Pre-training data detection** (behaviors tasks)
  > A common view is that the effectiveness of TDD is closely tied to the level of training-data memorization or overfitting exhibited by the target model during training (Yeom et al., 2018; Long et al., 2018).
  - [Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)
- **Parametric knowledge** (constructs)
  - [Toward Understanding In-context vs. In-weight Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ae338b3fe6624798efa80b6581924028-Paper-Conference.pdf)
- **Privacy** (constructs)
  - [Follow My Instruction and Spill the Beans: Scalable Data Extraction from Retrieval-Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/79cafa874121a3435d8a54f454b646b4-Paper-Conference.pdf)
- **Scalability** (constructs)
  > we propose a simple statistical ansatz based on memorization to study scaling laws in the context of inference. (Abstract)
  - [A Simple Model of Inference Scaling Laws](https://raw.githubusercontent.com/mlresearch/v267/main/assets/levi25a/levi25a.pdf)
- **Unlearning efficacy** (constructs)
  - [Underestimated Privacy Risks for Minority Populations in Large Language Model Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25d/wei25d.pdf)
- **Factual question answering** (behaviors tasks)
  - [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf)
- **Chain-of-thought reasoning** (constructs)
  > Paper title: Diagnosing Memorization in Chain-of-Thought Reasoning, One Token at a Time
  - [2025.emnlp-main.157.checklist](https://aclanthology.org/attachments/2025.emnlp-main.157.checklist.pdf)
