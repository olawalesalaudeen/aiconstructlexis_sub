# Expert diversity
**Type:** Construct  
**Referenced in:** 6 papers  

## State of the Field

Across the surveyed literature, expert diversity is consistently defined as the degree of dissimilarity among the individual expert networks within a Mixture-of-Experts (MoE) model. The most prevalent definition frames this dissimilarity in terms of having different parameters, while other work describes it as experts possessing distinct, non-overlapping capabilities, non-redundant knowledge, or unique processing preferences for data. In all provided definitions, this dissimilarity is seen as an indicator of functional specialization. The construct is operationalized in one paper by measuring the "average similarity score between experts," where a lower score indicates greater diversity. Expert diversity is presented as a desirable property to be encouraged and preserved, with methods like "layerwise recurrence" and "router initialization" reported to promote it. The concept appears in discussions of model compression, with one paper stating the goal of "preserving expert diversity and performance," and in the context of model "upcycling." It is associated with more effective data utilization and is said to contribute to a model's overall capacity and generalization.

## Sources

**[Layerwise Recurrent Router for  Mixture-of-Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/250a6c6a7a7216f5dec1364e9a93abf4-Paper-Conference.pdf)**
> The degree to which the different expert networks within a Mixture-of-Experts model have dissimilar parameters, indicating functional specialization.
