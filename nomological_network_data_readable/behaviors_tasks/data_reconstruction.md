# Data reconstruction
**Type:** Behavior  
**Referenced in:** 11 papers  
**Also known as:** Text reconstruction, Audio reconstruction  

## State of the Field

Across the provided literature, data reconstruction is most commonly described as the behavior of regenerating original data—such as text, speech, or audio—from an intermediate or altered representation. A frequent application is as a training objective, where models learn to reconstruct original text from noisy embeddings or pseudo-labeled counterparts, or to regenerate speech signals from learned latent features. In this context, reconstruction performance is also used as a metric to evaluate how much information is preserved in these intermediate representations, as one paper notes that reconstruction metrics "indicate how much information is preserved in the extracted representations" (A Variational Framework for Improving Naturalness in Generative Spoken Language Models). A different line of work frames data reconstruction as an adversarial behavior, where an attacker aims to recover unlearned text by analyzing differences in model weights after an unlearning procedure. The behavior is operationalized and evaluated using datasets for different modalities, including LibriSpeech for speech and FineWeb for text. The quality of the reconstruction, particularly for audio, is assessed using metrics like ViSQOL.

## Sources

**[Textual Unlearning Gives a False Sense of Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25d/du25d.pdf)**
> The observable behavior of generating a close approximation of the original unlearned text by exploiting differences in model weights before and after unlearning.

**[A Variational Framework for Improving Naturalness in Generative Spoken Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25z/chen25z.pdf) (as "Speech reconstruction")**
> The task of regenerating the original speech signal from its intermediate representations, such as semantic tokens and learned variational features.

**[Open-Det: An Efficient Learning Framework for Open-Ended Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25h/cao25h.pdf) (as "Text reconstruction")**
> The training task of regenerating original text from its noisy embedding representation.

**[ALMTokenizer: A Low-bitrate and Semantic-rich Audio Codec Tokenizer for Audio Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25q/yang25q.pdf) (as "Audio reconstruction")**
> Recovering a waveform or perceptually similar audio signal from compressed discrete tokens.

## Relationships

### Data reconstruction →
- **FineWeb** (measurements) — *measured_by*
  - [Improving Dialogue State Tracking through Combinatorial Search for In-Context Examples](https://aclanthology.org/2025.acl-long.1394.pdf)

### → Data reconstruction
- **Information preservation** (constructs) — *measured_by*
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)
