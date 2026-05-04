# Sentiment analysis
**Type:** Behavior  
**Referenced in:** 152 papers  
**Also known as:** Sentiment classification, Binary sentiment classification, Emotional Tone Interpretation, Emotion classification, Sentiment extrapolation, Emotion recognition, Sentiment label generation, Emotional valence scoring, Aspect sentiment quad prediction, Aspect-based sentiment classification, Emotion detection, Embodied emotion recognition, Embodied emotion classification, Sentiment analysis capability, Sentiment  

## State of the Field

Across the surveyed literature, sentiment analysis is overwhelmingly defined as the observable behavior of classifying the sentiment or tone of a text, typically as positive, negative, or neutral. This behavior is most commonly operationalized and measured using text classification benchmarks, with SST-2 and IMDb being the most frequently cited instruments, alongside others such as SST-5, MR, CR, and datasets from the GLUE benchmark. A smaller but consistent body of work expands this concept to "emotion classification" or "emotion detection," which focuses on identifying more specific emotions like joy, sadness, or anger. Some research also explores more fine-grained versions, such as "aspect-based sentiment classification," which identifies sentiment towards a specific entity. While primarily a text-based task, a few papers extend the concept to other modalities, with "Emotional Tone Interpretation" defined for audio and "embodied emotion recognition" for first-person videos. Other minority framings include "sentiment extrapolation," which involves modifying text to have more extreme sentiment, and "sentiment label generation," which treats it as a generative rather than a classification task. Although most papers treat sentiment analysis as an observable task, at least one paper defines a "sentiment analysis capability" as a latent ability of a model to interpret subjective content.

## Sources

**[An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)**
> The task of classifying the sentiment or tone of a given piece of text as positive, negative, or neutral.

**[Achieving Domain-Independent Certified Robustness via Knowledge Continuity](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cc11cda2a2679e8af5c6317aed0af8-Paper-Conference.pdf) (as "Sentiment classification")**
> The task of determining the sentimental tone (e.g., positive, negative) expressed in a piece of text.

**[Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf) (as "Binary sentiment classification")**
> The task of classifying text into one of two sentiment categories, such as positive or negative.

**[MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf) (as "Emotional Tone Interpretation")**
> The task behavior of identifying the emotional atmosphere or tone created by audio elements such as instruments or speech.

**[Implicit In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc034d186280f55370b6aca7a3285a65-Paper-Conference.pdf) (as "Emotion classification")**
> A text classification task focused on identifying and categorizing the emotion (e.g., joy, sadness, anger) expressed in a text.

**[A Checks-and-Balances Framework for Context-Aware Ethical AI Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chang25a/chang25a.pdf) (as "Emotion analysis")**
> The task of identifying and extracting emotional states (e.g., joy, sadness, anger) expressed in a given text.

**[Learning Extrapolative Sequence Transformations from Markov Chains](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hager25a/hager25a.pdf) (as "Sentiment extrapolation")**
> The task of modifying text reviews with sentiment ratings within a given range (e.g., 2-4 stars) to have ratings outside that range (e.g., 1 or 5 stars).

**[Efficient Personalized Adaptation for Physiological Signal Foundation Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ah/wu25ah.pdf) (as "Emotion recognition")**
> Predicting affective state labels from physiological signals, including valence, arousal, and dominance.

**[Efficient Beam Search for Large Language Models Using Trie-Based Decoding](https://aclanthology.org/2025.emnlp-main.749.pdf) (as "Sentiment label generation")**
> The task of producing the text of a sentiment label (e.g., "Positive") as a generative output rather than selecting from a fixed set of classes.

**[Cardiverse: HarnessingLLMs for Novel Card Game Prototyping](https://aclanthology.org/2025.emnlp-main.1512.pdf) (as "Emotional valence scoring")**
> Assigning a continuous numerical score to a text input that represents its emotional valence, typically on a scale from negative to positive.

**[Lemmatization ofPolish Multi-word Expressions](https://aclanthology.org/2025.emnlp-main.1127.pdf) (as "Aspect sentiment quad prediction")**
> The task of structuring opinions into fine-grained quadruples consisting of a category, aspect, opinion, and polarity.

**[Real-time Ad Retrieval viaLLM-generative Commercial Intention for Sponsored Search Advertising](https://aclanthology.org/2025.emnlp-main.1474.pdf) (as "Aspect-based sentiment classification")**
> The task of identifying the sentiment expressed towards a specific aspect or entity within a text.

**[Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf) (as "Emotion detection")**
> The task of identifying and classifying specific emotions expressed in a text.

**[$E^3$: Exploring Embodied Emotion Through A Large-Scale Egocentric Video Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/d611d5c0251d9680f869c5d2c46c6fcd-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Embodied emotion recognition")**
> A classification task to predict the overall positive or negative emotional tendency of a first-person view video.

**[$E^3$: Exploring Embodied Emotion Through A Large-Scale Egocentric Video Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/d611d5c0251d9680f869c5d2c46c6fcd-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Embodied emotion classification")**
> A closed-set question-answering task to identify the specific emotion category (out of eight) for a specified person in a first-person view video.

**[Data-Efficient Selection via Grammatical Complexity in Continual Pre-training of Domain-SpecificLLMs](https://aclanthology.org/2025.emnlp-main.1122.pdf) (as "Sentiment analysis capability")**
> The latent ability of a model to understand, interpret, and classify subjective content such as opinions, emotions, and attitudes expressed in text across various dimensions including polarity, emotion, sarcasm, and stance.

**[Unveiling Internal Reasoning Modes inLLMs: A Deep Dive into Latent Reasoning vs. Factual Shortcuts with Attribute Rate Ratio](https://aclanthology.org/2025.emnlp-main.112.pdf) (as "Sentiment")**
> The underlying emotional or affective tone (e.g., positive or negative) that a model's generated text is intended to convey.

## Relationships

### Sentiment analysis →
- **SST-2** (measurements) — *measured_by*
  > “Fine-tuning pre-trained language models (LMs) is a crucial step in a wide range of natural language processing tasks, including text classification and sentiment analysis”
  - [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf)
- **IMDb** (measurements) — *measured_by*
  > we train a CNN-LSTM model with 2.7 million parameters on the IMDB (Maas et al., 2011) for binary classification of positive or negative reviews.
  - [Achieving Domain-Independent Certified Robustness via Knowledge Continuity](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cc11cda2a2679e8af5c6317aed0af8-Paper-Conference.pdf)
- **SST-5** (measurements) — *measured_by*
  > We select five datasets spanning diverse domains: ... sst5 (Socher et al., 2013) for sentiment classification; (Section 4.1.1)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
- **MR** (measurements) — *measured_by*
  - [Fooling theLVLMJudges: Visual Biases inLVLM-Based Evaluation](https://aclanthology.org/2025.emnlp-main.1183.pdf)
- **CR** (measurements) — *measured_by*
  - [Synthetic Socratic Debates: Examining Persona Effects on Moral Decision and Persuasion Dynamics](https://aclanthology.org/2025.emnlp-main.832.pdf)
- **GLUE-X** (measurements) — *measured_by*
  > In particular, we consider 7 classical NLU tasks: Sentiment Analysis (SA), Natural Language Inference (NLI), Paraphrasing, Question-Answering NLI (QNLI), Textual Entailment, Textual Similarity, and Linguistic Acceptability (Grammar). (Section 3.1)
  - [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf)
- **Financial Phrase Bank** (measurements) — *measured_by*
  - [Order-Independence Without Fine Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/85529bc995777a74072ef63c05bedd30-Paper-Conference.pdf)
- **GLUE** (measurements) — *measured_by*
  > We finetune the pretrained RoBERTa-base model (Liu et al., 2019) on the GLUE benchmark, a widely used suite for evaluating NLP models across various tasks, including sentiment analysis and question answering (Wang et al., 2019). (Section 4.2)
  - [Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models](https://aclanthology.org/2025.naacl-long.71.pdf)
- **GoEmotions** (measurements) — *measured_by*
  - [Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf)
- **FiQA** (measurements) — *measured_by*
  > In the financial domain, we consider (1) the sentiment analysis task FiQA (Xie et al., 2023) where LLMs predict sentiments categorized as ’positive’, ’neutral’, or ’negative’ in financial texts.
  - [Teaching LLMs How to Learn with Contextual Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb0494e5ce9351cb120c3a35328dffef-Paper-Conference.pdf)
- **SENTIBENCH** (measurements) — *measured_by*
  > We conduct experiments across multiple model series (Llama-3, Qwen-3, and Gemma-3) and evaluate their sentiment analysis capabilities using SENTIBENCH (Zhang et al., 2025).
  - [Lemmatization ofPolish Multi-word Expressions](https://aclanthology.org/2025.emnlp-main.1127.pdf)

### → Sentiment analysis
- **Compositionality** (constructs) — *measured_by*
  > Two tasks that assess different aspects of compositional generalisation are used in the paper: Inverse Dictionary Modelling (IDM) for word-level composition and Sentiment Classification (SC) for phrase-level structure. (Section 4.1)
  - [ASTRA: A Negotiation Agent with Adaptive and Strategic Reasoning via Tool-integrated Action for Dynamic Offer Optimization](https://aclanthology.org/2025.emnlp-main.822.pdf)

### Associated with
- **Reasoning** (constructs)
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
