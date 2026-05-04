# Stance detection
**Type:** Behavior  
**Referenced in:** 12 papers  
**Also known as:** Comment stance classification, Stance classification  

## State of the Field

Across the surveyed literature, the prevailing definition of stance detection is the task of identifying and classifying the attitude expressed in a text towards a specific target or topic, with common labels being "favor, against or neutral." A more specific line of work defines the task within social media contexts, focusing on the relationship between texts. For instance, some papers describe it as classifying a reply to a comment as "agree, disagree, or neutral," while another frames it as determining if a comment "supports, denies, or extends" an original post. To operationalize and measure this behavior, researchers use several established benchmarks. The VAST and SemEval datasets are the most frequently cited instruments for evaluating stance detection performance in these papers, while the PStance dataset is also mentioned as a measurement tool for this task.

## Sources

**[ATLANTIS: Weak-to-Strong Learning via Importance Sampling](https://aclanthology.org/2025.acl-long.53.pdf)**
> The observable task of identifying and classifying the attitude (e.g., favor, against, neutral) expressed in a text towards a specific target or topic.

**[WangchanThaiInstruct: An instruction-following Dataset for Culture-Aware, Multitask, and Multi-domain Evaluation inThai](https://aclanthology.org/2025.emnlp-main.176.pdf) (as "Comment stance classification")**
> Determining whether a comment supports, denies, or extends the original post, based on its semantic and pragmatic relationship to the post content.

**[Neural Topic Modeling via Contextual and Graph Information Fusion](https://aclanthology.org/2025.emnlp-main.671.pdf) (as "Stance classification")**
> The observable task of assigning a label (agree, disagree, or neutral) to a reply based on its relationship to a parent comment in a social media context.

## Relationships

### Stance detection →
- **SemEval** (measurements) — *measured_by*
  > We validate the effectiveness of our method through extensive experiments on the SemEval-2016, and VAST datasets, showing that MPVStance outperforms state-of-the-art models in zero-shot, few-shot, and challenging scenarios. (Section 1)
  - [The Power of LLM-Generated Synthetic Data for Stance Detection in Online Political Discussions](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc3ce215c378815ce0be41cb0f65d0b5-Paper-Conference.pdf)
- **VAST** (measurements) — *measured_by*
  > Extensive experiments on the SEM16, VAST, and PStance datasets demonstrate that MPRF outperforms existing models.
  - [ATLANTIS: Weak-to-Strong Learning via Importance Sampling](https://aclanthology.org/2025.acl-long.53.pdf)
- **PStance** (measurements) — *measured_by*
  > Extensive experiments on the SEM16, VAST, and PStance datasets demonstrate that MPRF outperforms existing models.
  - [Mixture of Length and Pruning Experts for Knowledge Graphs Reasoning](https://aclanthology.org/2025.emnlp-main.24.pdf)
