# String manipulation
**Type:** Behavior  
**Referenced in:** 9 papers  
**Also known as:** Unscrambling, Substring identification, Vowel removal, String transformation, Text anonymization, Capitalization, String normalization  

## State of the Field

Across the surveyed literature, string manipulation is predominantly described as the transformation of character or word sequences through a variety of operations. These operations range from fundamental tasks like slicing, concatenation, reversing, and capitalization to more specific actions such as vowel removal and unscrambling randomly permuted words. A smaller set of studies conceptualizes string manipulation as a form of reasoning, where models must infer and apply rules for transformations, as in the "String Transformation" task from "MIRAGE", or select substrings based on semantic conditions. Another framing treats it as an applied process for specific goals, such as text anonymization, which involves modifying text to "remove, obfuscate, or generalize" personal information, or string normalization for data cleaning. In the context of anonymization, this behavior is reported to enable privacy protection and is studied alongside paraphrasing. The performance of models on string manipulation tasks is operationalized and evaluated using measurement instruments like SyGuS and metrics such as exact match.

## Sources

**[StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf)**
> Transforming strings by operations such as slicing, concatenation, reversing, splitting, or reordering characters.

**[A Percolation Model of Emergence: Analyzing Transformers Trained on a Formal Language](https://proceedings.iclr.cc/paper_files/paper/2025/file/5cd2b0a6b7423af6369cbdbbb228e8d0-Paper-Conference.pdf) (as "Unscrambling")**
> The task of reordering a randomly permuted set of words to form a grammatically and semantically valid sentence from the formal language.

**[MrT5: Dynamic Token Merging for Efficient Byte-level Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e9dd32cb9f9bff397f1a7ebd07010f2-Paper-Conference.pdf) (as "Vowel removal")**
> Removing vowels from an input character sequence while copying the remaining characters.

**[MrT5: Dynamic Token Merging for Efficient Byte-level Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e9dd32cb9f9bff397f1a7ebd07010f2-Paper-Conference.pdf) (as "Substring identification")**
> Selecting a substring from an input string that satisfies a semantic matching condition with a definition.

**[MIRAGE: Evaluating and Explaining Inductive Reasoning Process in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b782a3462ee9d566291cff148333ea9b-Paper-Conference.pdf) (as "String transformation")**
> An inductive reasoning task where the model must infer and apply rules to strings of characters, involving operations like concatenation and replication.

**[Language Models are Advanced Anonymizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/f478b2e8ad9ff0756bf5b79fb31c330f-Paper-Conference.pdf) (as "Text anonymization")**
> The observable process of a model modifying a text to remove, obfuscate, or generalize information that could be used to infer an author's personal attributes.

**[Heads up! Large Language Models Can Perform Tasks Without Your Instruction via Selective Attention Head Masking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25l/han25l.pdf) (as "Capitalization")**
> Transforming text to have the first letter capitalized, such as converting 'hello' to 'Hello'.

**[Programming Every Example: Lifting Pre-training Data Quality Like Experts at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25aa/zhou25aa.pdf) (as "String normalization")**
> Replacing noisy or inconsistent string patterns in text with clean, standardized versions.

## Relationships

### String manipulation →
- **SyGuS** (measurements) — *measured_by*
  - [HYSYNTH: Context-Free LLM Approximation for Guiding Program Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/file/1c9c85bae6161d52182d0fe2f3640512-Paper-Conference.pdf)
- **Exact match** (measurements) — *measured_by*
  - [A Percolation Model of Emergence: Analyzing Transformers Trained on a Formal Language](https://proceedings.iclr.cc/paper_files/paper/2025/file/5cd2b0a6b7423af6369cbdbbb228e8d0-Paper-Conference.pdf)
- **Privacy protection** (constructs) — *causes*
  - [Language Models are Advanced Anonymizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/f478b2e8ad9ff0756bf5b79fb31c330f-Paper-Conference.pdf)

### Associated with
- **Paraphrasing** (behaviors tasks)
  - [Language Models are Advanced Anonymizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/f478b2e8ad9ff0756bf5b79fb31c330f-Paper-Conference.pdf)
