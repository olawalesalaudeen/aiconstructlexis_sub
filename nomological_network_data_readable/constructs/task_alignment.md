# Task alignment
**Type:** Construct  
**Referenced in:** 6 papers  

## State of the Field

The concept of task alignment is framed in two distinct ways across the provided literature. One definition presents it as a model's ability to adapt its outputs to the specific constraints and goals of a new, ad-hoc task, with evaluations mentioned across domains like news articles, emails, and blog posts. A different framing treats task alignment as an internal property, defining it as the degree to which a model's internal representations correspond to a downstream task's requirements, particularly within the deeper layers of a network. In line with this internal perspective, task alignment is operationalized and measured using `Layer-wise probing`. As one study notes, this method can indicate "significant improvements in task alignment, especially within deeper LM layers" (Conspiracy Theories and Where to Find Them onTikTok). The construct is also studied in relation to `Knowledge forgetting`, with one paper proposing that task alignment causes it.

## Sources

**[Aligning Language Models with Demonstrated Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf)**
> The model's ability to adapt its outputs to meet the specific constraints and goals of a new, ad-hoc task.

## Relationships

### Task alignment →
- **Knowledge forgetting** (constructs) — *causes*
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **Layer-wise probing** (measurements) — *measured_by*
  > Layer-wise probing further indicates significant improvements in task alignment, especially within deeper LM layers, highlighting stable generalization even for previously unseen scenarios with increased planning complexity—conditions where baseline methods degrade markedly. (Abstract)
  - [Conspiracy Theories and Where to Find Them onTikTok](https://aclanthology.org/2025.acl-long.409.pdf)

### Associated with
- **In-context learning** (constructs)
  - [Lemmatization ofPolish Multi-word Expressions](https://aclanthology.org/2025.emnlp-main.1127.pdf)
