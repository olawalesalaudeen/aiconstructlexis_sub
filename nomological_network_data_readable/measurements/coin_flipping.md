# Coin flipping
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** CoinFlip, Coin Flipping  

## State of the Field

Coin flipping is predominantly described in the provided literature as a simple benchmark used to measure symbolic reasoning. The task is operationalized in slightly different ways across papers; some describe it as requiring a model to determine the final state of a coin after a sequence of flips, while another source specifies it is a binary task with two possible responses: "Yes or No." While the symbolic reasoning framing is most common, a few alternative characterizations exist. One paper defines the benchmark as a test of a model's ability to reason about "simple probabilistic scenarios." Another source, which identifies it as part of BIG-bench, frames it as a "simple commonsense reasoning task." Across these varied descriptions, it is consistently used to evaluate model capabilities on reasoning tasks.

## Sources

**[Personality Alignment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/25203d1cc8c58381eab578f4fcf9c4f8-Paper-Conference.pdf) (as "Coin Flip")**
> A benchmark designed to test a model's ability to reason about simple probabilistic scenarios.

**[Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf) (as "CoinFlip")**
> A simple symbolic reasoning benchmark task that requires a model to answer 'Yes' or 'No' based on a short problem description.

**[CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf) (as "Coin Flipping")**
> A symbolic reasoning benchmark that requires determining the final state of a coin after a sequence of flips.

## Relationships

### → Coin flipping
- **Symbolic reasoning** (constructs) — *measured_by*
  > CoinFlip (Wei et al., 2022) is a very simple symbolic reasoning task with two responses: Yes or No. (Section 3)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
