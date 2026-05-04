# Harmfulness detection
**Type:** Behavior  
**Referenced in:** 13 papers  
**Also known as:** Harmful request discrimination, Unsafe intent identification, Problematic turn detection, Violent communication detection, Risk identification, Offensive content detection, Toxic content detection, Harmful prompt detection  

## State of the Field

Across the provided literature, harmfulness detection is predominantly framed as a classification task where a model judges an input as either harmful or safe. The definitions vary in scope, encompassing the identification of content that is "dangerous," "conflict-inducing," "violent," "offensive," or "toxic," with the most common operationalization being a binary classification of prompts. This behavior is measured using a wide array of benchmarks, including AdvBench, ToxicChat, Harmbench, and MultiJail. While most definitions focus on classifying the content itself, a smaller set of papers frame it as identifying "unsafe intent" or assessing "potential safety risks," linking the behavior to the related construct of Safety awareness. The task is not limited to text; some work focuses on "detecting harmful prompts across languages and modalities," using benchmarks like HADES and MM-SafetyBench for image-text combinations and AIAH for audio. In practice, this behavior is implemented through automated tools, such as "Meta’s Llama-Guard series" and the "Rewire API," to filter content, with performance commonly evaluated by classification accuracy.

## Sources

**[RED: Unleashing Token-Level Rewards from Holistic Feedback via Reward Redistribution](https://aclanthology.org/2025.emnlp-main.253.pdf) (as "Harmful request discrimination")**
> The model's explicit judgment of whether a user input constitutes a harmful or dangerous request, typically expressed in structured safety assessments.

**[From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.261.pdf) (as "Unsafe intent identification")**
> The observable process of a model recognizing and articulating the potentially harmful or risky nature of a user's request.

**[A Good Plan is Hard to Find: Aligning Models with Preferences is Misaligned with What Helps Users](https://aclanthology.org/2025.emnlp-main.586.pdf) (as "Problematic turn detection")**
> Classifying whether a conversational turn is harmful or conflict-inducing based on linguistic and contextual cues.

**[2025.emnlp-main.586.checklist](https://aclanthology.org/attachments/2025.emnlp-main.586.checklist.pdf) (as "Violent communication detection")**
> Identifying or classifying communication that is violent in nature.

**[Skip-Thinking: Chunk-wise Chain-of-Thought Distillation Enable Smaller Language Models to Reason Better and Faster](https://aclanthology.org/2025.emnlp-main.611.pdf)**
> Classifying a prompt as harmful or safe.

**[Improving Clustering with Positive Pairs Generated fromLLM-Driven Labels](https://aclanthology.org/2025.emnlp-main.614.pdf) (as "Harmful content detection")**
> The model's observable behavior of classifying input text as safe or unsafe based on the presence of harmful content.

**[TheLLMAlready Knows: EstimatingLLM-Perceived Question Difficulty via Hidden Representations](https://aclanthology.org/2025.emnlp-main.62.pdf) (as "Risk identification")**
> The model's observable output when classifying whether a given interaction is safe or unsafe, or assigning it to a specific risk category.

**[Data-Efficient Hate Speech Detection via Cross-Lingual Nearest Neighbor Retrieval with Limited Labeled Data](https://aclanthology.org/2025.emnlp-main.1508.pdf) (as "Offensive content detection")**
> The task of identifying harmful, inappropriate, or offensive content in text.

**[Diagram-Driven Course Questions Generation](https://aclanthology.org/2025.emnlp-main.306.pdf) (as "Toxic content detection")**
> Identifying and filtering out biased, discriminatory, or violent material in generated dialogues using automated tools like Rewire API.

**[PakBBQ: A Culturally Adapted Bias Benchmark forQA](https://aclanthology.org/2025.emnlp-main.819.pdf) (as "Harmful prompt detection")**
> The observable behavior of classifying an input prompt as harmful or benign based on its content, regardless of language or modality.

## Relationships

### Harmfulness detection →
- **ToxicChat** (measurements) — *measured_by*
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)
- **AdvBench** (measurements) — *measured_by*
  > “Dunsafe dataset comprises harmful instructions derived from established benchmarks, including ADVBENCH”
  - [PakBBQ: A Culturally Adapted Bias Benchmark forQA](https://aclanthology.org/2025.emnlp-main.819.pdf)
- **OpenAI moderation API** (measurements) — *measured_by*
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)
- **Harmbench** (measurements) — *measured_by*
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)
- **WildGuardMix** (measurements) — *measured_by*
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)
- **XSTEST** (measurements) — *measured_by*
  - [Language Models Largely Exhibit Human-like Constituent Ordering Preferences](https://aclanthology.org/2025.naacl-long.127.pdf)
- **MultiJail** (measurements) — *measured_by*
  > Table 3 compares the accuracy of detecting harmful prompts for text benchmarks. Table 3(A) shows results for multilingual benchmarks, where OMNIGUARD ... achieves new state-of-the-art performance for 3 benchmarks: MultiJail, RTP-LX, and AyaRedTeaming.
  - [PakBBQ: A Culturally Adapted Bias Benchmark forQA](https://aclanthology.org/2025.emnlp-main.819.pdf)
- **HADES** (measurements) — *measured_by*
  > Hades and Safebench consist of images and text queries where the text itself is harmful.
  - [PakBBQ: A Culturally Adapted Bias Benchmark forQA](https://aclanthology.org/2025.emnlp-main.819.pdf)
- **SafeBench** (measurements) — *measured_by*
  > Hades and Safebench consist of images and text queries where the text itself is harmful.
  - [PakBBQ: A Culturally Adapted Bias Benchmark forQA](https://aclanthology.org/2025.emnlp-main.819.pdf)
- **MM-SafetyBench** (measurements) — *measured_by*
  > MM-safetybench, RTVLM, and VLSBench consist of an image and a query where the text query is seemingly benign, but when combined with the respective image, it is harmful
  - [PakBBQ: A Culturally Adapted Bias Benchmark forQA](https://aclanthology.org/2025.emnlp-main.819.pdf)
- **VLSBench** (measurements) — *measured_by*
  > MM-safetybench, RTVLM, and VLSBench consist of an image and a query where the text query is seemingly benign, but when combined with the respective image, it is harmful
  - [PakBBQ: A Culturally Adapted Bias Benchmark forQA](https://aclanthology.org/2025.emnlp-main.819.pdf)
- **AIAH** (measurements) — *measured_by*
  > Table 5 shows the accuracy of detecting harmful queries in audio. OMNIGUARD is able to detect harmful audio inputs with high accuracy across all benchmarks.
  - [PakBBQ: A Culturally Adapted Bias Benchmark forQA](https://aclanthology.org/2025.emnlp-main.819.pdf)

### Associated with
- **Safety awareness** (constructs)
  > “we define two security evaluation metrics: Safety Awareness, measured by accuracy on the binary classification task, and Risk Resistance, measured by accuracy on the 11-class risk identification task”
  - [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.261.pdf)
