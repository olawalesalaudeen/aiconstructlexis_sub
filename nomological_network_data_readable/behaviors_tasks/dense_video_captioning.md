# Dense video captioning
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, dense video captioning is consistently defined as the task of producing multiple, time-localized textual descriptions for a sequence of events within a single video. The expected output involves generating sentences that "Comprehensively describe all the events happened in the video" and explicitly providing the "start and end timestamp for each event" (E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding). This approach is explicitly distinguished from traditional video captioning methods. As one paper notes, the focus is on the "nuanced task of narrating multiple events within a video rather than generating a single overarching description" (Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks). To operationalize and evaluate this behavior, researchers use datasets such as YouCook2 and ActivityNet Captions. The task is also studied in relation to both image captioning and temporal reasoning.

## Sources

**[E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf)**
> Producing timestamped descriptions for multiple events throughout a video.

## Relationships

### Dense video captioning →
- **YouCook2** (measurements) — *measured_by*
  > Dense video caption. We use Youcook2 (Zhou et al., 2018) and ActivityNet Captions (Fabian Caba Heilbron & Niebles, 2015) datasets as the evaluation datasets.
  - [TRACE: Temporal Grounding Video LLM  via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf)
- **ActivityNet Captions** (measurements) — *measured_by*
  > Dense video caption. We use Youcook2 (Zhou et al., 2018) and ActivityNet Captions (Fabian Caba Heilbron & Niebles, 2015) datasets as the evaluation datasets.
  - [TRACE: Temporal Grounding Video LLM  via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf)

### Associated with
- **Dense captioning** (behaviors tasks)
  - [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Temporal reasoning** (constructs)
  - [TRACE: Temporal Grounding Video LLM  via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf)
