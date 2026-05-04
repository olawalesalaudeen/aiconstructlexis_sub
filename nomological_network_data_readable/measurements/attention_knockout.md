# Attention knockout
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Attention knockout is described in the provided literature as a method for analyzing transformer models, framed as both a "mechanistic interpretability method" and a "reverse engineering method." The technique operates by disabling parts of the attention mechanism to understand their function. One paper describes this as disabling entire attention heads, while another provides a more granular view of blocking attention between specific token positions. The shared goal across these descriptions is to assess the contribution of these components to "information flow" and overall model behavior. In practice, it is used to "identify critical information flow points" and to validate research conclusions, sometimes alongside other interpretability techniques such as activation patching.

## Sources

**[Diversity Explains Inference Scaling Laws: Through a Case Study of MinimumBayes Risk Decoding](https://aclanthology.org/2025.acl-long.1411.pdf)**
> A mechanistic interpretability method that disables attention heads to assess their contribution to information flow and model behavior.
