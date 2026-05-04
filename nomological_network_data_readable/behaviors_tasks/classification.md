# Classification
**Type:** Behavior  
**Referenced in:** 57 papers  
**Also known as:** Label inference, Event categorization, Label path prediction, Personality prediction, Multi-class categorization, Emotion detection, Emotion recognition, Emotional state extraction, Speech emotion recognition, Emotion label generation  

## State of the Field

Across the surveyed literature, Classification is predominantly defined as the task of assigning a label from a predefined set to a given input. This behavior is frequently operationalized as a text-to-text mapping where output classes are encoded as strings, with one paper noting the process involves scoring each choice and returning the one with the highest score. While the core concept involves a "small fixed output space," which is often contrasted with generation tasks, its application is broad, encompassing inputs like text, images, and audio for speech emotion recognition. The provided papers describe many specific instances, including multi-label emotion recognition, personality prediction from demographic data, and hierarchical label path prediction for documents. A less common framing treats classification as determining if a model's response meets a certain criterion, such as safety. The performance of this behavior is commonly measured using accuracy metrics on a range of benchmarks, including MELD, GoEmotions, ARC-Challenge, MMLU-Pro, MixEval, and Waste-Bench.

## Sources

**[AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf)**
> Assigning a label from a predefined set based on input context, treated as a text-to-text mapping in this work.

**[MuHBoost: Multi-Label Boosting For Practical Longitudinal Human Behavior Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca2963d1cfb25e93362e86fb427a9524-Paper-Conference.pdf) (as "Label inference")**
> Inferring one or more labels for an unseen sample from its natural-language description.

**[Position:LLMs Can be Good Tutors inEnglish Education](https://aclanthology.org/2025.emnlp-main.886.pdf) (as "Event categorization")**
> The observable task of selecting the most probable event category from a predefined hierarchical classification system based on given meteorological data.

**[Evaluating and Aligning Human Economic Risk Preferences inLLMs](https://aclanthology.org/2025.emnlp-main.918.pdf) (as "Label path prediction")**
> Generating a complete path of labels from root to leaf in a hierarchical taxonomy for a given input document.

**[MultiLogicNMR(er): A Benchmark and Neural-Symbolic Framework for Non-monotonic Reasoning with Multiple Extensions](https://aclanthology.org/2025.emnlp-main.928.pdf) (as "Personality prediction")**
> Inferring MBTI-related cognitive-process labels or personality types from demographic descriptions.

**[Program of Thoughts for Financial Reasoning: Leveraging Dynamic In-Context Examples and Generative Retrieval](https://aclanthology.org/2025.emnlp-main.1578.pdf) (as "Multi-class categorization")**
> The task of classifying multiple waste items within a single complex scene into more than one category.

**[Reimagining Safety Alignment with An Image](https://aclanthology.org/2025.emnlp-main.486.pdf) (as "Emotion detection")**
> Identifying specific emotions expressed in text, such as anger, joy, or fear, often used in social media analysis.

**[REARANK: Reasoning Re-ranking Agent via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.126.pdf) (as "Emotion recognition")**
> The task of identifying and classifying human emotions expressed in text.

**[TS-CLIP: Time Series Understanding byCLIP](https://aclanthology.org/2025.emnlp-main.232.pdf) (as "Emotional state extraction")**
> The observable task of identifying and labeling a user's emotions from their utterances in a dialogue history.

**[CalligraphicOCRforChinese Calligraphy Recognition](https://aclanthology.org/2025.emnlp-main.246.pdf) (as "Speech emotion recognition")**
> Identifying the emotional state expressed in human speech from audio input, often in dialogue contexts.

**[CROP: Contextual Region-Oriented Visual Token Pruning](https://aclanthology.org/2025.emnlp-main.493.pdf) (as "Emotion label generation")**
> Producing free-text descriptions of the emotions a narrative character is feeling based on a given sentence.

## Relationships

### Classification →
- **MELD** (measurements) — *measured_by*
  > Speech Emotion Recognition (SER): We incorporate MELD (Poria et al., 2019), a multimodal multi-party dataset containing over 1,400 dialogues and 13,000 utterances... (Section 3.1)
  - [Crowdsource, Crawl, or Generate? CreatingSEA-VL, a Multicultural Vision-Language Dataset forSoutheastAsia](https://aclanthology.org/2025.acl-long.917.pdf)
- **IEMOCAP** (measurements) — *measured_by*
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
- **SuperGLUE** (measurements) — *measured_by*
  - [BAdam: A Memory Efficient Full Parameter Optimization Method for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2c570b0f9938c7a58a612e5b00af9cc0-Paper-Conference.pdf)
- **GoEmotions** (measurements) — *measured_by*
  - [Beyond the Score: Uncertainty-CalibratedLLMs for Automated Essay Assessment](https://aclanthology.org/2025.emnlp-main.993.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  > The classification benchmarks include ARC-Challenge (Clark et al., 2018), MMLU-Pro (Wang et al., 2024), and MixEval (Ni et al., 2024). (Section 5.2)
  - [A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf)
- **MMLU-Pro** (measurements) — *measured_by*
  > The classification benchmarks include ARC-Challenge (Clark et al., 2018), MMLU-Pro (Wang et al., 2024), and MixEval (Ni et al., 2024). (Section 5.2)
  - [A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf)
- **MixEval** (measurements) — *measured_by*
  > The classification benchmarks include ARC-Challenge (Clark et al., 2018), MMLU-Pro (Wang et al., 2024), and MixEval (Ni et al., 2024). (Section 5.2)
  - [A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf)
- **SemEval 2018 Task 1 E-c** (measurements) — *measured_by*
  - [Beyond the Score: Uncertainty-CalibratedLLMs for Automated Essay Assessment](https://aclanthology.org/2025.emnlp-main.993.pdf)
- **Waste-Bench** (measurements) — *measured_by*
  > “These questions cover diverse categories related to real-world waste classification scenarios, including individual classification of waste classes, multi-class classification, shapes of objects, and colors.”
  - [Program of Thoughts for Financial Reasoning: Leveraging Dynamic In-Context Examples and Generative Retrieval](https://aclanthology.org/2025.emnlp-main.1578.pdf)

### Associated with
- **Time series classification** (behaviors tasks)
  - [Efficient Personalized Adaptation for Physiological Signal Foundation Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ah/wu25ah.pdf)
