# Solution generation
**Type:** Behavior  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, solution generation is consistently defined as the observable task or behavior of a large language model producing one or more candidate solutions in response to a given problem. The operationalization of this behavior commonly involves prompting a model to produce multiple outputs for a single problem. For instance, one paper describes generating 'N candidate solutions' ("Generative Verifiers: Reward Modeling as Next-Token Prediction"), while another details a process of generating '100 diverse candidate solutions using 10 open-source models' to collect a varied set of responses ("Whisper-UT: A Unified Translation Framework for Speech and Text"). This behavior is often framed as an initial step in a larger workflow. As an example, one study positions solution generation as a process that is subsequently followed by a verification stage, where a reward model ranks the generated solutions. The same work also discusses the possibility of 'unifying solution generation with verification' within a single training paradigm.

## Sources

**[Generative Verifiers: Reward Modeling as Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/214308a2d5e3f83ef9ad2739e1cbc46d-Paper-Conference.pdf)**
> The observable task of an LLM producing a candidate solution in response to a given problem.
