# SPIDER-DK
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** Spider-DK  

## State of the Field

Across the provided literature, SPIDER-DK is consistently described as a variant of the SPIDER benchmark used to evaluate the Text-to-SQL task. Its defining feature, mentioned in all sources, is the incorporation of challenges that require domain knowledge. Papers state that it introduces these challenges by incorporating domain knowledge directly into the questions, which necessitates "domain knowledge reasoning to correctly generate the SQL query" (ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL). This modification is intended to make the underlying task more challenging. One paper situates SPIDER-DK as one of several benchmarks "derived from Spider," alongside Spider-Realistic and Spider-Syn (EPO: Explicit Policy Optimization for Strategic Reasoning inLLMs via Reinforcement Learning). The same work distinguishes it from these other variants by noting that while they might remove column names or use synonyms, SPIDER-DK's specific function is to "incorporate domain knowledge."

## Sources

**[ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)**
> A robust variant of the SPIDER benchmark that introduces challenges requiring domain knowledge reasoning to correctly generate the SQL query.

**[EPO: Explicit Policy Optimization for Strategic Reasoning inLLMs via Reinforcement Learning](https://aclanthology.org/2025.acl-long.748.pdf) (as "Spider-DK")**
> A variant of the Spider benchmark that incorporates domain knowledge into the questions, making the Text-to-SQL task more challenging.
