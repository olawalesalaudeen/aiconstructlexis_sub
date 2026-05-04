# Parameter extraction
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Contextual parameter identification, Parameter resolution, Parameterization, Clinical entity extraction  

## State of the Field

Across the provided literature, parameter extraction is most commonly described as the observable task of identifying and extracting specific values from natural language to serve as arguments for a function or API call. This prevailing usage is seen in definitions of the behavior as parsing queries for "input arguments for the generated code" ("Structuring Radiology Reports: ChallengingLLMs with Lightweight Models") or filling in "missing API parameter values from dialogue context" ("Do Large Language Models Truly Grasp Addition? A Rule-Focused Diagnostic Using Two-Integer Arithmetic"). A smaller set of papers applies this concept to specialized domains. For example, one study frames it as "Clinical entity extraction," which involves identifying patient attributes like "lab values, vital signs, or symptoms" from clinical notes ("Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment"). Another paper defines it as "Contextual parameter identification" in legal scenarios, focusing on extracting elements like "sender, subject, [and] recipient" ("TracSum: A New Benchmark for Aspect-Based Summarization with Sentence-Level Traceability in Medical Domain"). While the terminology varies, including "parameterization" and "parameter resolution," the core action of identifying and assigning values is consistent. This behavior is measured using methods such as "parameter resolution accuracy," precision in identifying variables, and multiple-choice questions about specific parameters.

## Sources

**[TracSum: A New Benchmark for Aspect-Based Summarization with Sentence-Level Traceability in Medical Domain](https://aclanthology.org/2025.emnlp-main.44.pdf) (as "Contextual parameter identification")**
> Correctly identifying elements of information flow such as sender, subject, recipient, and information type in a legal scenario based on contextual cues.

**[Structuring Radiology Reports: ChallengingLLMs with Lightweight Models](https://aclanthology.org/2025.emnlp-main.393.pdf)**
> The observable task of identifying and extracting specific values from a natural language query to serve as arguments for a function call.

**[Do Large Language Models Truly Grasp Addition? A Rule-Focused Diagnostic Using Two-Integer Arithmetic](https://aclanthology.org/2025.emnlp-main.682.pdf) (as "Parameter resolution")**
> The model fills in missing API parameter values from dialogue context or user replies.

**[Towards a Holistic and Automated Evaluation Framework for Multi-Level Comprehension ofLLMs in Book-Length Contexts](https://aclanthology.org/2025.emnlp-main.1242.pdf) (as "Parameterization")**
> The observable action of identifying and assigning correct values to the parameters required by a selected function.

**[Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment](https://aclanthology.org/2025.emnlp-main.1302.pdf) (as "Clinical entity extraction")**
> Identifying relevant patient attributes, such as lab values, vital signs, or symptoms, from clinical notes.
