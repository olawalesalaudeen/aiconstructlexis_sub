# TREC
**Type:** Measurement  
**Referenced in:** 36 papers  
**Also known as:** Trec  

## State of the Field

Across the provided literature, TREC is predominantly described as a benchmark dataset originating from the Text REtrieval Conference. Its most common application is to measure the behavior of `Text classification`, specifically through a 6-way question classification task. This task requires models to categorize questions into predefined types, which are frequently cited as including "person, location, numeric," "abbreviation," and "entity." While this is the prevailing usage, a smaller line of work frames TREC as a component of the LongBench suite, where it is used to evaluate few-shot learning performance. Additionally, it is sometimes employed for more general natural language understanding (NLU) evaluation. One study also uses the dataset to measure the construct of `Sensitivity`, noting that classes such as "Description, Entity, and Number" exhibit the highest sensitivity scores.

## Sources

**[Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf)**
> A question classification dataset from the Text REtrieval Conference (TREC), where the task is to classify questions into six types.

**[DP-OPT: Make Large Language Model Your Privacy-Preserving Prompt Engineer](https://proceedings.iclr.cc/paper_files/paper/2024/file/fffe5a7804c40465ef2432386850c2c7-Paper-Conference.pdf) (as "Trec")**
> A dataset from the LongBench suite used to evaluate few-shot learning performance.

## Relationships

### → TREC
- **Text classification** (behaviors tasks) — *measured_by*
  > We use eight text classification datasets for ID data: SST-2 (SST; Socher et al., 2013), Subjectivity (SUBJ; Pang & Lee, 2004), AG-News (AGN; Zhang et al., 2015), and TREC (TREC; Li & Roth, 2002), BigPatent (BP; Sharma et al., 2019), AmazonReviews (AR; McAuley et al., 2015), MovieGenre (MG; Maas et al., 2011), 20NewsGroups (NG; Lang, 1995). (Section 4.1)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **Sensitivity** (constructs) — *measured_by*
  > In Figure 3 (bottom), we plot the sensitivity Sτ for each class and prompting strategy (Llama3). Consistently with the example of Section 1, we see that on TREC the classes Description, Entity, and Number are the ones with the highest sensitivity. (Section 5)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.73.pdf)
- **Consistency** (constructs) — *measured_by*
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.73.pdf)
