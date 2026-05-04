# Self-improvement
**Type:** Construct  
**Referenced in:** 35 papers  
**Also known as:** Self-evolution, Continuous improvement, Self-improvement capability, Policy improvement, Iterative reflection capability, Learning from mistakes, Self-Reflection, Self-evaluation, Self-reflection, Experiential learning, Recursive self-improvement, Mistake detection  

## State of the Field

Across the surveyed literature, Self-improvement is predominantly framed as a latent construct representing a model's capacity to autonomously enhance its performance over time, often without external supervision. The construct is consistently operationalized through an iterative cycle of generation, evaluation, and refinement. In this cycle, a model first generates outputs, such as reasoning paths or solutions, and then employs related abilities like "self-reflection," "self-evaluation," or "mistake detection" to analyze its own performance and identify flaws. As one paper notes, this process treats errors not as failures but as "key opportunities to enhance reasoning" (Kill two birds with one stone: generalized and robustAI-generated text detection via dynamic perturbations). The model then updates itself, for example by fine-tuning on its own successful trajectories or by generating corrective feedback from failures, a process also termed "experiential learning." While most definitions focus on improving outputs or reasoning, a smaller subset of work describes a more radical form, "recursive self-improvement" or "self-modification," where an agent dynamically alters its own code. This construct is measured using instruments like StreamBench, a benchmark explicitly designed to "evaluate the continuous improvement of LLM agents," and is also studied in relation to code generation.

## Sources

**[AlphaMath Almost Zero: Process Supervision without Process](https://proceedings.neurips.cc/paper_files/paper/2024/file/30dfe47a3ccbee68cffa0c19ccb1bc00-Paper-Conference.pdf) (as "Self-evolution")**
> The ability of a model to autonomously improve its capabilities and reinforce its knowledge utilization through iterative self-generated training, without external process supervision.

**[CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)**
> The latent capacity of a model to effectively analyze and correct flaws in its own or others' responses, facilitated by critique ability.

**[StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Continuous improvement")**
> The ability of an LLM agent to enhance its performance on a task over time by learning from a continuous sequence of inputs and feedback.

**[Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf) (as "Self-improvement capability")**
> The latent ability of a large language model to improve its performance by generating outputs, verifying them, and then updating itself based on the verified data.

**[Distilling Reinforcement Learning Algorithms for In-Context Model-Based Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c4a7643ab90cd62320df95c873a1c6f-Paper-Conference.pdf) (as "Policy improvement")**
> The latent process of refining a strategy or policy in-context to maximize cumulative rewards based on new information discovered through interaction.

**[Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.309.pdf) (as "Self-reflection")**
> The latent ability of an agent to analyze its own performance, particularly failures, and generate feedback to improve its strategy in subsequent attempts.

**[Kill two birds with one stone: generalized and robustAI-generated text detection via dynamic perturbations](https://aclanthology.org/2025.naacl-long.447.pdf) (as "Learning from mistakes")**
> The model's capacity to improve its reasoning by analyzing and correcting flawed rationales, treating errors as opportunities for self-improvement.

**[S2-MAD: Breaking the Token Barrier to Enhance Multi-Agent Debate Efficiency](https://aclanthology.org/2025.naacl-long.476.pdf) (as "Self-evaluation")**
> The model's capacity to assess the correctness and progress of its own reasoning steps and solutions without relying on external ground truth.

**[DCE-LLM: Dead Code Elimination with Large Language Models](https://aclanthology.org/2025.naacl-long.502.pdf) (as "Iterative reflection capability")**
> The latent ability of a model to effectively refine its responses over multiple cycles of self-evaluation and revision, avoiding degradation due to redundancy, drift, or stubbornness.

**[DCE-LLM: Dead Code Elimination with Large Language Models](https://aclanthology.org/2025.naacl-long.502.pdf) (as "Self-Reflection")**
> A reflection-based evaluation procedure in which the model iteratively revises its own answer using feedback.

**[Towards Comprehensive Argument Analysis in Education: Dataset, Tasks, and Method](https://aclanthology.org/2025.acl-long.697.pdf) (as "Experiential learning")**
> The capacity of a model to reflect on past failures, extract insights, and refine future planning and decision-making through accumulated experience.

**[T-REG: Preference Optimization with Token-Level Reward Regularization](https://aclanthology.org/2025.acl-long.1354.pdf) (as "Recursive self-improvement")**
> The latent ability of an agent to iteratively enhance its own policy and learning algorithm by modifying its code, leading to progressively better performance over time.

**[T-REG: Preference Optimization with Token-Level Reward Regularization](https://aclanthology.org/2025.acl-long.1354.pdf) (as "Self-modification")**
> The agent's ability to dynamically alter its own code and operational logic during execution based on its reasoning and environmental feedback.

**[SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.1313.pdf) (as "Mistake detection")**
> The latent ability to identify incorrect or flawed reasoning steps within a chain of thought, even when the final answer may appear plausible.
