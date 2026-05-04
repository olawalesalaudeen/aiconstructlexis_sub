# Information retrieval and recall
**Type:** Construct  
**Referenced in:** 25 papers  
**Also known as:** Association recall, Associative recall capacity, Factual recall, Knowledge recall, Recall, Statistical recall, Factual knowledge retrieval, Fact recall, Information retrieval and localization, Retrievability, Associative memory retrieval, Causal retrieval, In-context retrieval, Information retrieval, Information retrieval capability, Parametric knowledge retrieval, Retrieval, Task vector retrieval, Knowledge retrieval, Long-context retrieval, Retrieval capability, Retrieval performance  

## State of the Field

The most prevalent usage of "Information retrieval and recall" in the provided literature describes a model's ability to access, locate, and utilize stored information. This construct is commonly conceptualized along a primary axis concerning the source of information: many definitions frame it as retrieving factual or world knowledge stored within the model's parameters from pre-training (e.g., "parametric knowledge retrieval," "factual recall"), while an equally common framing focuses on locating information within the current input sequence (e.g., "in-context retrieval," "long-context retrieval"). A smaller set of papers defines it in the context of retrieval-augmented systems that access an external document corpus. The construct is operationalized through tasks such as question-answering that requires world knowledge, locating specific facts in long documents as in Needle-in-a-Haystack tests, and recovering associated tokens from a sequence. Some work offers more specialized definitions, such as "associative recall," the capacity to retrieve information based on contextual cues, or "causal retrieval," which involves retrieving past context to minimize future prediction loss. A distinct and less common line of work uses "recall" in a statistical sense, defining it as the model's coverage of a data distribution for generating diverse outputs. Another minority framing, "statistical recall," contrasts the concept with genuine reasoning, describing it as the mere reproduction of patterns from training data. Across these varied definitions, the core concept consistently revolves around accessing information, with distinctions arising from whether the source is internal parameters, the immediate context, or an external database.

## Sources

**[Provable In-Context Vector Arithmetic via Retrieving Task Concepts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25a/bu25a.pdf) (as "Factual knowledge retrieval")**
> The model's ability to access and retrieve stored factual information when prompted.

**[Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf) (as "Knowledge recall")**
> The model's ability to retrieve and use stored factual information or world knowledge to inform its responses in tasks like general visual question answering.

**[Mechanistic Unlearning: Robust Knowledge Unlearning and Editing via Mechanistic Localization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25k/guo25k.pdf) (as "Factual recall")**
> The latent ability of a model to retrieve and express specific factual associations.

**[Understanding Input Selectivity in Mamba: Impact on Approximation Power, Memorization, and Associative Recall Capacity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ab/huang25ab.pdf) (as "Associative recall capacity")**
> The ability of a model to retrieve stored information based on contextual cues, such as recovering a value given a key or predicting the successor of a previously seen token.

**[NoLiMa: Long-Context Evaluation Beyond Literal Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/modarressi25a/modarressi25a.pdf) (as "Association recall")**
> The fundamental ability to recall previously seen information based on associative links present in the input context.

**[Improving Diversity in Language Models: When Temperature Fails, Change the Loss](https://raw.githubusercontent.com/mlresearch/v267/main/assets/verine25a/verine25a.pdf) (as "Recall")**
> The degree to which the model covers the true data distribution, reflecting its ability to generate diverse and representative outputs that align with plausible language patterns.

**[RE-IMAGINE: Symbolic Benchmark Synthesis for Reasoning Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25n/xu25n.pdf) (as "Statistical recall")**
> The degree to which a model's performance relies on recognizing and reproducing patterns from its training data rather than engaging in systematic reasoning.

**[Position: Enough of Scaling LLMs! Lets Focus on Downscaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25c/goel25c.pdf) (as "Fact recall")**
> The ability of a model to store and retrieve factual information from its parameters.

**[Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf) (as "In-context retrieval")**
> The latent ability to precisely locate and extract relevant information from earlier in the input sequence, particularly for mapping contextual cues to specific outputs such as answer labels.

**[Provable In-Context Vector Arithmetic via Retrieving Task Concepts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25a/bu25a.pdf) (as "Task vector retrieval")**
> The latent ability of a transformer to extract a high-level task concept vector from demonstration pairs during in-context learning, enabling generalization across queries within the same task.

**[Attention-Level Speculation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cai25g/cai25g.pdf) (as "Information retrieval")**
> The latent ability to locate and extract specific, relevant pieces of information from a large body of text.

**[PhantomWiki: On-Demand Datasets for Reasoning and Retrieval Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gong25d/gong25d.pdf) (as "Retrieval")**
> The latent ability to access and utilize relevant information from a large external document corpus, especially when the full corpus exceeds the model's context window.

**[Efficient Length-Generalizable Attention via Causal Retrieval for Long-Context Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25v/hu25v.pdf) (as "Causal retrieval")**
> The latent ability to retrieve past contextual chunks that are most useful for predicting future chunks, trained end-to-end via gradient propagation through relevance scores.

**[Massive Values in Self-Attention Modules are the Key to Contextual Knowledge Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25f/jin25f.pdf) (as "Parametric knowledge retrieval")**
> The latent ability of a model to retrieve factual knowledge that has been encoded during pre-training, independent of the current input context.

**[LOGO — Long cOntext aliGnment via efficient preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25j/tang25j.pdf) (as "Information retrieval capability")**
> The model's underlying ability to accurately locate and identify key, salient pieces of information embedded within a long context.

**[In-Context Learning as Conditioned Associative Memory Retrieval](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25k/wu25k.pdf) (as "Associative memory retrieval")**
> The latent capacity of a model to retrieve stored patterns or knowledge by matching a query to the most relevant memory through similarity-based dynamics, akin to Hopfield network behavior.

**[Minerva: A Programmable Memory Test Benchmark for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xia25c/xia25c.pdf) (as "Information retrieval and localization")**
> The latent ability to locate, search for, and extract relevant information from context memory based on instructions or queries, treating the context as a dynamic memory store.

**[PoisonedEye: Knowledge Poisoning Attack on Retrieval-Augmented Generation based Large Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25da/zhang25da.pdf) (as "Retrievability")**
> The latent property of a poison sample to be successfully retrieved by the system in response to a target query, determined by its embedding proximity to the query.

**[CompAct: Compressed Activations for Memory-EfficientLLMTraining](https://aclanthology.org/2025.naacl-long.72.pdf) (as "Knowledge retrieval")**
> The latent ability to recall factual knowledge stored during pre-training, which is required when contextual information is insufficient for answering a question.

**[CAMIEval: EnhancingNLGEvaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.439.pdf) (as "Retrieval capability")**
> The underlying ability of an LLM to identify and access relevant external documents or facts necessary to answer a query, either directly or through generated search queries.

**[On the Vulnerability of Text Sanitization](https://aclanthology.org/2025.naacl-long.267.pdf) (as "Long-context retrieval")**
> The model's behavior of answering questions based on very long input documents, requiring efficient processing of extensive prefilling contexts.

**[MILU: A Multi-taskIndic Language Understanding Benchmark](https://aclanthology.org/2025.naacl-long.508.pdf) (as "Retrieval performance")**
> The latent ability of a ToD system to retrieve relevant and accurate information from a knowledge store in response to user queries, particularly under varying levels of ambiguity.
