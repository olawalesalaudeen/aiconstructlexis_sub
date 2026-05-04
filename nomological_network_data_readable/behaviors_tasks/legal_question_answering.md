# Legal question answering
**Type:** Behavior  
**Referenced in:** 7 papers  
**Also known as:** Legal open-ended question answering, Legal compliance question answering  

## State of the Field

Across the surveyed literature, legal question answering is characterized as a domain-specific generation task. The definitions provided, however, reveal multiple distinct framings of this behavior. The most common definition describes it as answering questions based on legal knowledge, with one paper specifying this knowledge relates to international citizenship. A different conceptualization presents it as a more open-ended task requiring models to respond to "actual legal scenarios" using "understanding, analysis, and judgment" ("LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models"). A third, more constrained framing treats it as a classification problem of legal compliance, where the goal is to determine if a case is "permitted, prohibited, or not applicable" under regulations like GDPR or HIPAA. In terms of operationalization, the provided data offers one specific example of how this behavior is measured, with one study using the "International Citizenship Questions sub-task in LegalBench" ("BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts"). The expected outputs from models vary accordingly with these different framings, ranging from generated analytical responses to discrete compliance classifications.

## Sources

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Legal open-ended question answering")**
> Responding to questions that arise in actual legal scenarios, requiring understanding, analysis, and judgment.

**[BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)**
> The observable task of answering questions based on legal knowledge, specifically related to international citizenship.

**[TracSum: A New Benchmark for Aspect-Based Summarization with Sentence-Level Traceability in Medical Domain](https://aclanthology.org/2025.emnlp-main.44.pdf) (as "Legal compliance question answering")**
> Producing correct classifications of whether a given legal case is permitted, prohibited, or not applicable under specific regulations such as GDPR, HIPAA, or EU AI Act.
