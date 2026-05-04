# Query-focused summarization
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, query-focused summarization is consistently defined as the task of generating a summary from one or more documents that is specifically tailored to a user-provided query. The goal is to produce a response that emphasizes information relevant to the query, drawing from the source documents. A specific variant of this task, termed "long context query focused summarization (LCQFS)," is described for scenarios involving long input documents. This variant is further specified by the requirement to "generate a response to the query which cites arbitrary length text spans from the input" ("We Politely Insist: YourLLMMust Learn thePersian Art of Taarof"). The provided data offers one example of how this behavior is operationalized: the "Podcast Transcripts" task is identified as a query-focused summarization task in the paper "StructRAG: Boosting Knowledge Intensive Reasoning of LLMs via Inference-time Hybrid Information Structurization".

## Sources

**[StructRAG: Boosting Knowledge Intensive Reasoning of LLMs via Inference-time Hybrid Information Structurization](https://proceedings.iclr.cc/paper_files/paper/2025/file/5975754c7650dfee0682e06e1fec0522-Paper-Conference.pdf)**
> Generating a summary of one or more documents that is specifically tailored to answer a given query.
