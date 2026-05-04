# Language identification
**Type:** Behavior  
**Referenced in:** 7 papers  
**Also known as:** Language recognition  

## State of the Field

Across the provided literature, Language identification is most commonly defined as the task of predicting or classifying the language of a given text input, such as a sentence. This behavior is frequently operationalized as a classification task, for instance, by using in-context demonstrations where, as one paper notes, "each demonstration is a pair of a sentence and its associated language" ("Rapid Selection and Ordering of In-Context Demonstrations via Prompt Embedding Clustering"). It is often studied alongside other NLP tasks like sentiment classification, part-of-speech tagging, and named entity recognition. A distinct and less common framing, presented in one paper as "language recognition," treats the behavior as a formal decision problem. In this view, a system acts as a recognizer that receives a string and produces a decision to "accept or reject it" as a member of a language ("Training Neural Networks as Recognizers of Formal Languages"). This latter framing is also studied in relation to language modeling.

## Sources

**[Rapid Selection and Ordering of In-Context Demonstrations via Prompt Embedding Clustering](https://proceedings.iclr.cc/paper_files/paper/2025/file/6c2745a8e20271c2e8c7067a2c3c7710-Paper-Conference.pdf)**
> Predicting the language of a sentence from in-context demonstrations.

**[Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf) (as "Language recognition")**
> The observable action of receiving a string as input and producing a decision to accept or reject it as a member of a language.

## Relationships

### Associated with
- **Language modeling** (behaviors tasks)
  - [Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf)
