# Language modeling
**Type:** Behavior  
**Referenced in:** 266 papers  
**Also known as:** Masked token prediction, Pre-training performance, Autoregressive token generation, Masked token reconstruction, Autoregressive sequence modeling, Next-token prediction, Next-word prediction, Next-symbol prediction, Audio token prediction, Next-byte prediction, Token prediction, Bigram prediction, In-context n-gram prediction, Masked next-token prediction, Trigram prediction, Unigram prediction, Word prediction, Language modeling ability, Predictive capability, Predictive performance, Language modeling capability, Language modelling capability, Language modeling performance, Source-language modeling  

## State of the Field

Across the surveyed literature, language modeling is predominantly defined as the observable behavior of predicting the next unit in a sequence given the preceding context, with variations specifying this unit as a token, word, symbol, or byte. A secondary framing, found in papers like "From Tokens to Lattices", treats it as the task of predicting masked tokens from bidirectional context. A smaller set of papers conceptualizes it more abstractly as a latent "language modeling ability" or "capability" to generate plausible text. This behavior is most commonly operationalized by measuring perplexity on standard text corpora, with WikiText-2, WikiText-103, and C4 appearing as the most frequent evaluation benchmarks. Performance is also widely assessed through zero-shot accuracy on downstream tasks, including LAMBADA, MMLU, HellaSwag, and WinoGrande. The provided data also details more specific variants, such as "In-context n-gram prediction" and "Audio token prediction". Language modeling is studied alongside text generation, with one paper framing it as the process of "aligning model distribution with that of human language" (EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING), and is also connected to long-context processing and factual recall.

## Sources

**[ESPACE: Dimensionality Reduction of Activations for Model Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6591cc41be737e9ba4cc487ac8082d-Paper-Conference.pdf)**
> Predicting or scoring text sequences as a language model, as reflected here by perplexity evaluation.

**[From Tokens to Lattices: Emergent Lattice Structures in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf) (as "Masked token prediction")**
> The fundamental task of a Masked Language Model, which involves predicting a masked token based on its surrounding bidirectional context.

**[Mix-LN: Unleashing the Power of Deeper Layers by Combining Pre-LN and Post-LN](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3d637987f36563fa45f943f8eadc2d0-Paper-Conference.pdf) (as "Pre-training performance")**
> The observable quality of the model's language modeling capabilities during the initial pre-training phase.

**[Flash Inference: Near Linear Time Inference for Long Convolution Sequence Models and Beyond](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c818dd40651b420873af70b8a790e3f-Paper-Conference.pdf) (as "Autoregressive token generation")**
> The process of generating a sequence of tokens one at a time, where each new token is conditioned on the sequence of previously generated tokens.

**[Masked Diffusion Models are Secretly Time-Agnostic Masked Models and Exploit Inaccurate Categorical Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e3b203e72c4e058de26d02a92a81844-Paper-Conference.pdf) (as "Masked token reconstruction")**
> Predicting original tokens at positions that were randomly masked in the input sequence.

**[Towards Understanding the Universality of Transformers for Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/d846c59be138a704e800f36e7fcb696a-Paper-Conference.pdf) (as "Autoregressive sequence modeling")**
> Using prior tokens in a sequence to estimate the next state when the sequence follows a recursive dependence on the previous state.

**[Understanding Factual Recall in Transformers via Associative Memories](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bf9f909c24c8879d1b7f86fa50a9e49-Paper-Conference.pdf) (as "Next-token prediction")**
> The task of predicting the next token in a sequence given the preceding tokens.

**[How new data permeates LLM knowledge and how to dilute it](https://proceedings.iclr.cc/paper_files/paper/2025/file/0f85efb1e7545dc35a1b5e4d45aaf3c2-Paper-Conference.pdf) (as "Next-word prediction")**
> The task of predicting the next token in a sequence given the preceding tokens.

**[Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf) (as "Next-symbol prediction")**
> The observable task of predicting, for each position in a sequence, the set of all valid symbols that could legally appear next according to the rules of a given formal language.

**[HALL-E: Hierarchical Neural Codec Language Model for Minute-Long Zero-Shot Text-to-Speech Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/e32aefe039c94b95505b243e4cff8aa2-Paper-Conference.pdf) (as "Audio token prediction")**
> Predicting discrete audio-token sequences from text and/or prompt audio in an autoregressive or non-autoregressive manner.

**[Exact Byte-Level Probabilities from Tokenized Language Models for FIM-Tasks and Model Ensembles](https://proceedings.iclr.cc/paper_files/paper/2025/file/5ed5c3c846f684a54975ad7a2525199f-Paper-Conference.pdf) (as "Next-byte prediction")**
> The task of predicting the next byte in a sequence given the preceding bytes.

**[Relaxed Recursive Transformers: Effective Parameter Sharing with Layer-wise LoRA](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d6a55225cebbdc16fbb0e45c5bdf2b-Paper-Conference.pdf) (as "Token prediction")**
> Producing the next token from intermediate or final hidden states during language modeling or early-exit inference.

**[Learning In-context $n$-grams with Transformers: Sub-$n$-grams Are Near-Stationary Points](https://raw.githubusercontent.com/mlresearch/v267/main/assets/varre25a/varre25a.pdf) (as "In-context n-gram prediction")**
> The task of predicting the next token in a sequence based on an n-gram language model derived from the context of that same sequence.

**[Learning In-context $n$-grams with Transformers: Sub-$n$-grams Are Near-Stationary Points](https://raw.githubusercontent.com/mlresearch/v267/main/assets/varre25a/varre25a.pdf) (as "Unigram prediction")**
> The observable behavior of predicting the next token based solely on its overall frequency in the sequence, ignoring contextual dependencies.

**[Learning In-context $n$-grams with Transformers: Sub-$n$-grams Are Near-Stationary Points](https://raw.githubusercontent.com/mlresearch/v267/main/assets/varre25a/varre25a.pdf) (as "Bigram prediction")**
> The observable behavior of predicting the next token based on the immediately preceding token, capturing first-order sequential dependencies.

**[Learning In-context $n$-grams with Transformers: Sub-$n$-grams Are Near-Stationary Points](https://raw.githubusercontent.com/mlresearch/v267/main/assets/varre25a/varre25a.pdf) (as "Trigram prediction")**
> The observable behavior of predicting the next token based on the two preceding tokens, capturing second-order sequential dependencies.

**[Generative Audio Language Modeling with Continuous-valued Tokens and Masked Next-Token Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25n/yang25n.pdf) (as "Masked next-token prediction")**
> A training task where a model performs next-token prediction on a sequence from which a random subset of past tokens has been dropped or masked.

**[Simple Yet Effective: An Information-Theoretic Approach to Multi-LLMUncertainty Quantification](https://aclanthology.org/2025.emnlp-main.1552.pdf) (as "Word prediction")**
> The observable behavior of predicting a missing word in a sentence, either the final word or a randomly selected non-final word, based on context.

**[SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf) (as "Predictive performance")**
> The overall ability of a language model to make accurate predictions, as measured by metrics like perplexity and zero-shot task accuracy.

**[Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf) (as "Language modeling ability")**
> The model's core capability to understand and generate plausible, meaningful text, which should be preserved during debiasing interventions.

**[Language Modeling Is Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/3cbf627fa24fb6cb576e04e689b9428b-Paper-Conference.pdf) (as "Predictive capability")**
> The latent ability of a model to accurately predict the next symbol in a sequence based on prior context, reflecting its underlying probabilistic modeling strength.

**[AmoebaLLM: Constructing Any-Shape Large Language Models for Efficient and Instant Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f11e548311c7fd3f33596a4d1dd41f0-Paper-Conference.pdf) (as "Language modeling capability")**
> The fundamental ability of a model to understand and generate plausible sequences of text, which can be recovered more easily than factual knowledge during fine-tuning.

**[Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf) (as "Language modelling capability")**
> The latent ability of the model to predict and generate coherent language sequences, often inferred from probability distributions over tokens.

**[Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf) (as "Language modeling performance")**
> The overall proficiency of a model in predicting the next token in a sequence, measured across various standard language benchmarks.

**[Demystifying optimized prompts in language models](https://aclanthology.org/2025.emnlp-main.148.pdf) (as "Source-language modeling")**
> The latent ability of the decoder to understand and represent the source language effectively, whether derived from speech or text, which supports improved translation and transcription.

## Relationships

### Language modeling →
- **WikiText-2** (measurements) — *measured_by*
  > “we assess the performance of pruned models by calculating the perplexity of language generation experiments on separate validation sets derived from WikiText2”
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **WikiText-103** (measurements) — *measured_by*
  > To evaluate the performance of the model’s pre-training task, we measure perplexity on the Wikipedia 103 corpus (Merity et al., 2016) available through HuggingFace. (Section 2.4)
  - [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
- **C4** (measurements) — *measured_by*
  > We evaluate quantized model performance by two metrics. Firstly, we measure perplexity, measured on the WikiText2 (Merity et al., 2016), Penn Treebank (Marcus et al., 1994) and C4 (Raffel et al., 2020) datasets. (Section 5)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **Penn Treebank (PTB)** (measurements) — *measured_by*
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **LAMBADA** (measurements) — *measured_by*
  > On LAMBADA, we report ... suffix accuracy by masking all tokens of the last word and predicting all of them in a single forward pass
  - [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf)
- **WikiText** (measurements) — *measured_by*
  > Following previous works on LLM compression (Xiao et al., 2023; Frantar & Alistarh, 2023), we evaluate the perplexity on the held-out WikiText (Merity et al., 2016) validation set. (Section 4)
  - [A Simple and Effective Pruning Approach for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/14c856c7a41297804de4c4890e846b25-Paper-Conference.pdf)
- **PG-19** (measurements) — *measured_by*
  > We evaluate HiP on the PG19 (Rae et al., 2019) datasets. (Section 5.2, under the heading 'LANGUAGE MODELING PERFORMANCE EVALUATION')
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  > “for several other zero-shot tasks, we use the open-source tool lm-evaluation-harness (version 0.4.4) (Gao et al., 2024) for assessment.”
  - [Test-Time Training on Nearest Neighbors for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f02f1185b97518ab5bd7ebde466992d3-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  > “we evaluate the quantized models on zero-shot commonsense reasoning (CSR) ability... Besides common sense abilities, we also evaluate multi-task generalization ability with five-shot setting (in-context learning) on MMLU”
  - [LQ-LoRA: Low-rank plus Quantized Matrix Decomposition for Efficient Language Model Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/d97a16cb83d74195b76e0bf1e85bf072-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  > We conducted experiments on a series of language modeling and understanding tasks, including PiQA (Bisk et al., 2020), ARC-easy (ARC-e), ARC-challenge (ARC-c) (Clark et al., 2018), HellaSwag (Hella.) (Zellers et al., 2019), Winogrande (Wino.) (Sakaguchi et al., 2019) and MMLU (Li et al., 2023). The results are reported in Table 2 and all evaluations were done using lm-evaluation-harness (Gao et al., 2024). (Section 4.2)
  - [Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf)
- **The Pile** (measurements) — *measured_by*
  > "Our experiments involved training on a dataset tokenized with the LLaMA tokenizer (Touvron et al., 2023), comprising 56GB of raw data sourced from 91 files sampled from The Pile (Gao et al., 2020)."
  - [MiCEval: Unveiling Multimodal Chain of Thought’s Quality via Image Description and Reasoning Steps](https://aclanthology.org/2025.naacl-long.505.pdf)
- **OpenWebText** (measurements) — *measured_by*
  > We use two text datasets: 1) Text8 (Mahoney, 2006), a relatively small-scale, character-level text modeling benchmark extracted from English Wikipedia, and 2) OpenWebText, an open-source replica of the unreleased WebText (Gokaslan & Cohen, 2019) dataset used to train GPT-2.
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  > We conducted experiments on a series of language modeling and understanding tasks, including PiQA (Bisk et al., 2020), ARC-easy (ARC-e), ARC-challenge (ARC-c) (Clark et al., 2018), HellaSwag (Hella.) (Zellers et al., 2019), Winogrande (Wino.) (Sakaguchi et al., 2019) and MMLU (Li et al., 2023). The results are reported in Table 2 and all evaluations were done using lm-evaluation-harness (Gao et al., 2024). (Section 4.2)
  - [Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  > We conducted experiments on a series of language modeling and understanding tasks, including PiQA (Bisk et al., 2020), ARC-easy (ARC-e), ARC-challenge (ARC-c) (Clark et al., 2018), HellaSwag (Hella.) (Zellers et al., 2019), Winogrande (Wino.) (Sakaguchi et al., 2019) and MMLU (Li et al., 2023). The results are reported in Table 2 and all evaluations were done using lm-evaluation-harness (Gao et al., 2024). (Section 4.2)
  - [KV Shifting Attention Enhances Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ac/xu25ac.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  > We conducted experiments on a series of language modeling and understanding tasks, including PiQA (Bisk et al., 2020), ARC-easy (ARC-e), ARC-challenge (ARC-c) (Clark et al., 2018), HellaSwag (Hella.) (Zellers et al., 2019), Winogrande (Wino.) (Sakaguchi et al., 2019) and MMLU (Li et al., 2023). The results are reported in Table 2 and all evaluations were done using lm-evaluation-harness (Gao et al., 2024). (Section 4.2)
  - [Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf)
- **Proof-pile** (measurements) — *measured_by*
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
- **GLUE** (measurements) — *measured_by*
  > To further assess preservation of language modeling capability, we also evaluated on downstream tasks: MLMs on GLUE tasks... (Section 3.3).
  - [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf)
- **lm1b** (measurements) — *measured_by*
  > We also ran experiments with WikiText (Merity et al., 2016), and lm1b (Chelba et al., 2014) and observed similar results. (Section 5)
  - [Selective Attention Improves Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf)
- **DCLM** (measurements) — *measured_by*
  > We also report the LM’s language modeling loss on a subset of DCLM (Li et al., 2024), a high-quality corpus curated with complex pipelines and human heuristics, to verify that models trained on D′ retain diversity and long-tail knowledge coverage. (Section 3.1)
  - [MiniPLM: Knowledge Distillation for Pre-training Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea05e4fc0299c27648c9985266abad47-Paper-Conference.pdf)
- **StereoSet** (measurements) — *measured_by*
  > LMS is used to evaluate the language modeling abilities of models. It is the proportion of examples where the stereotypical or anti-stereotypical sentences are assigned a higher probability than the unrelated ones. (Section 4.4)
  - [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf)
- **Books3** (measurements) — *measured_by*
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
- **Wikipedia** (measurements) — *measured_by*
  - [Understanding Transformers via N-Gram Statistics](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1c446eebd9a317dd0e96b16908c821a-Paper-Conference.pdf)
- **GovReport** (measurements) — *measured_by*
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
- **TinyStories** (measurements) — *measured_by*
  - [Understanding Transformers via N-Gram Statistics](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1c446eebd9a317dd0e96b16908c821a-Paper-Conference.pdf)
- **SlimPajama** (measurements) — *measured_by*
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **RedPajama** (measurements) — *measured_by*
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
- **Alpaca instruction dataset** (measurements) — *measured_by*
  - [Beware of Calibration Data for Pruning Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ede933e10afa991a10b6f36b6522129-Paper-Conference.pdf)
- **Text8** (measurements) — *measured_by*
  > We use two text datasets: 1) Text8 (Mahoney, 2006), a relatively small-scale, character-level text modeling benchmark extracted from English Wikipedia, and 2) OpenWebText, an open-source replica of the unreleased WebText (Gokaslan & Cohen, 2019) dataset used to train GPT-2.
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **BabiStories** (measurements) — *measured_by*
  > The TINYSTORIES work of Eldan & Li (2023) shows how to study large language modeling questions using small language models... we leverage... to generate a new corpus of tiny stories dubbed BABISTORIES.
  - [Memory Mosaics](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c3ac496e6fe7be0c2c2b95014e2210-Paper-Conference.pdf)
- **RedPajama V2** (measurements) — *measured_by*
  > “We use the RedPajama-V2 dataset (Computer, 2023), which is a large-scale collection of text data designed for training language models.”
  - [No Need to Talk: Asynchronous Mixture of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ae2d3297891cad0c56dd12d60ff7dde-Paper-Conference.pdf)
- **BLiMP** (measurements) — *measured_by*
  > "All models were evaluated on a common evaluation measure: BLiMP (Warstadt et al., 2020)."
  - [TopoNets: High performing vision and language models with brain-like topography](https://proceedings.iclr.cc/paper_files/paper/2025/file/6191ab7080c840f67eaf5dff7d5edfcb-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  > To validate the performance of different models, we used some benchmarks for the 3B and 19B models that were trained more tokens, including Lambada(Paperno et al., 2016), Winogrande(Sakaguchi et al., 2021), Hellaswag(Zellers et al., 2019), ARC(Clark et al., 2018), CMMLU(Li et al., 2023a), MMLU(Hendrycks et al.), Math(Hendrycks et al., 2021). (Section 4.1)
  - [KV Shifting Attention Enhances Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ac/xu25ac.pdf)
- **CodeParrot** (measurements) — *measured_by*
  > Language modeling, for which we evaluate perplexity on PG19 (Rae et al., 2020), Proof-Pile (Zhangir Azerbayev), and CodeParrot (CodeParrot) (Section 3.1)
  - [MorphMark: Flexible Adaptive Watermarking for Large Language Models](https://aclanthology.org/2025.acl-long.241.pdf)
- **CMMLU** (measurements) — *measured_by*
  - [KV Shifting Attention Enhances Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ac/xu25ac.pdf)
- **MATH** (measurements) — *measured_by*
  > To validate the performance of different models, we used some benchmarks for the 3B and 19B models that were trained more tokens, including Lambada(Paperno et al., 2016), Winogrande(Sakaguchi et al., 2021), Hellaswag(Zellers et al., 2019), ARC(Clark et al., 2018), CMMLU(Li et al., 2023a), MMLU(Hendrycks et al.), Math(Hendrycks et al., 2021). (Section 4.1)
  - [KV Shifting Attention Enhances Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ac/xu25ac.pdf)
- **Open LLM Leaderboard 2** (measurements) — *measured_by*
  - [xLSTM 7B: A Recurrent LLM for Fast and Efficient Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beck25b/beck25b.pdf)
- **RTE** (measurements) — *measured_by*
  - [ProbingLLMWorld Models: Enhancing Guesstimation with Wisdom of Crowds Decoding](https://aclanthology.org/2025.emnlp-main.235.pdf)

### → Language modeling
- **In-context learning** (constructs) — *causes*
  - [Linking In-context Learning in Transformers to Human Episodic Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ba385c3ea3bb417ac6d6a33e24411bc-Paper-Conference.pdf)
- **Expressive power** (constructs) — *causes*
  - [Over-Tokenized Transformer: Vocabulary is Generally Worth Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25bb/huang25bb.pdf)

### Associated with
- **Length generalization** (constructs)
  > We propose a new theoretical framework to study length generalization for the next-token prediction task, as performed by decoder-only transformers. (Abstract)
  - [The Role of Sparsity for Length Generalization in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/golowich25a/golowich25a.pdf)
- **Text generation quality** (constructs)
  > While we believe that perplexity measurements and generation quality are strongly related, this is a hypothesis we aim to investigate in future work. (Section 6)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **Code generation** (behaviors tasks)
  - [Test-Time Training on Nearest Neighbors for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f02f1185b97518ab5bd7ebde466992d3-Paper-Conference.pdf)
- **Long-context processing** (constructs)
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
- **Text generation** (behaviors tasks)
  > “in language generation, x is a sequence of tokens t1 · · · tk, y is the next token tk+1”
  - [Portable Reward Tuning: Towards Reusable Fine-Tuning across Different Pretrained Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chijiwa25a/chijiwa25a.pdf)
- **Mathematical reasoning** (constructs)
  - [Position Coupling: Improving Length Generalization of Arithmetic Transformers Using Task Structure](https://proceedings.neurips.cc/paper_files/paper/2024/file/27aa3a0e6d63db269977bb2df5607cb8-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [DREAM: Improving Video-Text Retrieval Through Relevance-Based Augmentation Using Large Foundation Models](https://aclanthology.org/2025.naacl-long.157.pdf)
- **Sequence modeling** (constructs)
  - [Longhorn: State Space Models are Amortized Online Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee0e45ff4de76cbfdf07015a7839f339-Paper-Conference.pdf)
- **Expressive power** (constructs)
  > In this paper, we propose a kernel interpretation for the autoregressive setting. We introduce a framework to rigorously analyze the expressivity of deep Transformers in next-token prediction. (Section 1)
  - [Towards Understanding the Universality of Transformers for Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/d846c59be138a704e800f36e7fcb696a-Paper-Conference.pdf)
- **In-context reasoning** (constructs)
  - [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf)
- **Factual recall** (behaviors tasks)
  - [Understanding Factual Recall in Transformers via Associative Memories](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bf9f909c24c8879d1b7f86fa50a9e49-Paper-Conference.pdf)
- **Language identification** (behaviors tasks)
  - [Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf)
- **Multimodal alignment** (constructs)
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
- **Masked language modeling** (behaviors tasks)
  - [Enhancing Efficiency and Exploration in Reinforcement Learning forLLMs](https://aclanthology.org/2025.emnlp-main.76.pdf)
