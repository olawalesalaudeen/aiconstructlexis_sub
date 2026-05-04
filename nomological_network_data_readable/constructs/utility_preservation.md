# Utility preservation
**Type:** Construct  
**Referenced in:** 11 papers  
**Also known as:** General capability preservation, Model performance preservation, Capabilities preservation, Capability preservation  

## State of the Field

Across the surveyed literature, utility preservation is a construct referring to a model's ability to maintain its general performance and core capabilities after undergoing a targeted intervention. While the core idea is consistent, its specific framing varies by context, appearing as 'utility preservation' in machine unlearning, 'capability preservation' in alignment and steering, 'model performance preservation' in pruning, and 'text quality preservation' in watermarking. The prevailing goal described across these applications is to ensure that modifications—such as removing data, aligning for safety, or editing knowledge—do not degrade the model's performance on general, downstream tasks or data not intended for the intervention. The field operationalizes this construct using a variety of measurement instruments, with papers reporting the use of general-purpose benchmarks like GLUE and metrics like perplexity. More specialized evaluations are also employed, such as the MUSE benchmark, which explicitly measures performance on a 'retain set' using a knowledge memorization metric. One paper on alignment suggests that a small KL divergence between the modified and original models implies that capabilities are preserved. Utility preservation is sometimes presented in a tradeoff with other goals; for instance, one paper on model steering notes a 'tradeoff between model control and capabilities preservation'. It is also used as a dependent measure to evaluate other properties, such as the scalability of unlearning algorithms.

## Sources

**[MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)**
> The extent to which an unlearned model maintains its general performance on data not intended for removal.

**[Theoretical guarantees on the best-of-n alignment policy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beirami25a/beirami25a.pdf) (as "Capability preservation")**
> The extent to which an aligned model retains the core abilities and knowledge of the original reference model from which it was derived.

**[DLP: Dynamic Layerwise Pruning in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25l/chen25l.pdf) (as "Model performance preservation")**
> The ability of a pruned model to retain its original language modeling and downstream task performance despite high sparsity.

**[BiMark: Unbiased Multilayer Watermarking for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25u/feng25u.pdf) (as "Text quality preservation")**
> The degree to which a watermarking method maintains the fluency, coherence, and functional utility of the original language model's output, such that downstream performance is not degraded.

**[Reinforced Lifelong Editing for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25an/li25an.pdf) (as "General capability preservation")**
> The ability of a model editing method to maintain the LLM's performance on general downstream tasks while performing targeted knowledge updates.

**[AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf) (as "Capabilities preservation")**
> The extent to which a steering intervention avoids degrading the model's underlying general abilities while controlling a target concept.

## Relationships

### Utility preservation →
- **MUSE** (measurements) — *measured_by*
  > We address this issue by proposing MUSE, a comprehensive machine unlearning evaluation benchmark that enumerates six diverse desirable properties for unlearned models: (1) no verbatim memorization, (2) no knowledge memorization, (3) no privacy leakage, (4) utility preservation on data not intended for removal, (5) scalability with respect to the size of removal requests, and (6) sustainability over sequential unlearning requests. (Section 1)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **Knowledge memorization** (constructs) — *measured_by*
  > To quantify this, we evaluate the unlearned model’s performance on the retain set using the knowledge memorization metric KnowMem(funlearn, Dretain). (Section 3.1)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **GLUE** (measurements) — *measured_by*
  > For General Capability, we measure that using the average of six GLUE metrics in Section 4.5. (Figure 3 caption)
  - [Reinforced Lifelong Editing for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25an/li25an.pdf)

### → Utility preservation
- **Scalability** (constructs) — *measured_by*
  > The performance of GA, NPO, and their regularized variants, measured by utility preservation, degrades with larger forget set sizes (a) and sequential unlearning requests (b). (Figure 6)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)

### Associated with
- **Knowledge forgetting** (constructs)
  - [Communication Makes Perfect: Persuasion Dataset Construction via Multi-LLMCommunication](https://aclanthology.org/2025.naacl-long.204.pdf)
