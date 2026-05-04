# Cross-domain generalization
**Type:** Construct  
**Referenced in:** 27 papers  
**Also known as:** Generalization to unseen targets, Domain transfer, Cross-domain generalizability, Domain generalization, Cross-domain transfer, Cross-domain adaptability, Out-of-domain generalization  

## State of the Field

Across the surveyed literature, cross-domain generalization is consistently described as a model's ability to transfer knowledge and maintain performance when applied to a new domain, topic, or data distribution not seen during training. While the terminology varies—including "domain transfer," "out-of-domain generalization," and "cross-domain adaptability"—the central idea involves performance on unseen targets, with some definitions specifically highlighting the transfer of "reasoning performance across fundamentally different task domains" (Think, Verbalize, then Speak). This capability is often framed as a challenge, as models are reported to "struggle with unseen targets" (RoT), and domain-specific training "may come at the cost of broader generalization" (Think, Verbalize, then Speak). To measure this construct, researchers operationalize it through evaluation on a range of benchmarks, including ALFWorld, AndroidControl, CrossNER, GLUE-X, LEMON, VATEX, and VirtualHome. The evaluation procedures frequently involve a stark difference between training and test sets, such as using a "leave-one-out setup" where a model is tested on a held-out domain (FIRE) or assessing performance on websites or topics explicitly excluded from the training data. Cross-domain generalization is studied alongside multilingual generalization. Some work suggests it is influenced by other capabilities; for instance, one paper reports that schema linking contributes to improving it, while another links it to reasoning.

## Sources

**[MixLoRA-DSI: Dynamically Expandable Mixture-of-LoRAExperts for Rehearsal-Free Generative Retrieval over Dynamic Corpora](https://aclanthology.org/2025.emnlp-main.21.pdf) (as "Domain transfer")**
> The capability of a model trained on a set of source domains or topics to perform effectively on a different target domain or topic.

**[RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.30.pdf) (as "Generalization to unseen targets")**
> The model's ability to accurately detect stances toward targets not encountered during training, reflecting adaptability to novel topics in social media discourse.

**[CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.37.pdf)**
> The ability of a model to transfer knowledge and performance from one domain or prompt distribution to another, particularly when training and test prompts differ significantly.

**[Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech](https://aclanthology.org/2025.emnlp-main.727.pdf) (as "Cross-domain generalizability")**
> The capacity of a model to maintain or transfer reasoning performance across fundamentally different task domains after specialized training.

**[FIRE: Flexible Integration of Data Quality Ratings for Effective Pretraining](https://aclanthology.org/2025.emnlp-main.736.pdf) (as "Domain generalization")**
> The degree to which a model's learned preferences and concept importance generalize across different domains, capturing both shared patterns and domain-specific deviations.

**[FilBench: CanLLMs Understand and GenerateFilipino?](https://aclanthology.org/2025.emnlp-main.128.pdf) (as "Cross-domain transfer")**
> The ability of a model to apply knowledge learned in one specific domain to perform tasks in a different, unseen domain.

**[FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.513.pdf) (as "Cross-domain adaptability")**
> The model's inherent capability to transfer knowledge and maintain performance across different recommendation contexts and platforms, such as e-commerce, games, and social media.

**[IIET: Efficient Numerical Transformer via Implicit Iterative Euler Method](https://aclanthology.org/2025.emnlp-main.454.pdf) (as "Out-of-domain generalization")**
> The ability to transfer web-agent performance to websites or query settings not seen during training.

## Relationships

### Cross-domain generalization →
- **GLUE-X** (measurements) — *measured_by*
  - [The MaleCEOand the Female Assistant: Evaluation and Mitigation of Gender Biases in Text-To-Image Generation of Dual Subjects](https://aclanthology.org/2025.acl-long.450.pdf)
- **AndroidControl** (measurements) — *measured_by*
  - [On the Effects of Data Scale on UI Control Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/a79f3ef3b445fd4659f44648f7ea8ffd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VATEX** (measurements) — *measured_by*
  - [Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf)
- **CrossNER** (measurements) — *measured_by*
  - [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.540.pdf)
- **LEMON** (measurements) — *measured_by*
  - [Opt-Out: Investigating Entity-Level Unlearning for Large Language Models via Optimal Transport](https://aclanthology.org/2025.acl-long.1372.pdf)
- **VirtualHome** (measurements) — *measured_by*
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)
- **ALFWorld** (measurements) — *measured_by*
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)

### → Cross-domain generalization
- **General reasoning** (constructs) — *causes*
  - [Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech](https://aclanthology.org/2025.emnlp-main.727.pdf)
- **Schema linking** (behaviors tasks) — *causes*
  > Schema-linking is widely recognized as key to improving generalization by adaptively associating queries with database items. (Section 1)
  - [Playpen: An Environment for Exploring Learning From Dialogue Game Feedback](https://aclanthology.org/2025.emnlp-main.1518.pdf)

### Associated with
- **Zero-shot generalization** (constructs)
  - [FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.513.pdf)
