# DecodingTrust
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** Decoding Trust  

## State of the Field

Across the provided literature, DecodingTrust is predominantly characterized as a benchmark dataset designed to evaluate the trustworthiness and safety of Large Language Models. One paper also describes it as a "public leaderboard that integrates a massive amount of new test data" for ranking LLMs on these attributes. The benchmark is used to operationalize and measure several distinct constructs. For instance, it is used to assess `Stereotyping`, with one study specifying its use of the "‘stereotypes’ partition for demographic groups corresponding to race (black/white)" ("Certifying Counterfactual Bias in LLMs"). Another documented application is the evaluation of `Privacy leakage`, where its "Enron email extraction task" is specifically cited as a method for assessing data leakage. The provided data also indicates that DecodingTrust is used to measure `Faithfulness`, rounding out its application as a tool for evaluating various properties of LLMs.

## Sources

**[Certifying Counterfactual Bias in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c6decac1477fbcc2cbf12d314ce0133-Paper-Conference.pdf) (as "Decoding Trust")**
> A benchmark dataset used to evaluate LLM properties, including stereotype bias against demographic groups, here using the stereotypes partition.

**[IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d3a9e085540c65dd3e5731361f9320e-Paper-Conference.pdf)**
> A benchmark dataset designed to evaluate the trustworthiness of LLMs, including tasks related to privacy, such as the Enron email extraction task used to assess data leakage.

## Relationships

### → DecodingTrust
- **Stereotyping** (constructs) — *measured_by*
  - [ALI-Agent: Assessing LLMs'  Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf)
- **Trustworthiness** (constructs) — *measured_by*
  - [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf)
- **Privacy leakage** (behaviors tasks) — *measured_by*
  - [IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d3a9e085540c65dd3e5731361f9320e-Paper-Conference.pdf)
