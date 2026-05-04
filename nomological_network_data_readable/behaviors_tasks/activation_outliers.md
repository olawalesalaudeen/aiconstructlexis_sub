# Activation outliers
**Type:** Behavior  
**Referenced in:** 3 papers  
**Also known as:** Outlier activations in hidden states  

## State of the Field

Across the provided literature, "activation outliers" are consistently characterized as the observable phenomenon of abnormally large values appearing in a model's internal activation tensors. These values are described as being "orders of magnitude larger" than others and are located in specific parts of the model, such as the "hidden states," "layer outputs," and "down-projection inputs." The papers agree that these outliers manifest in "speciﬁc feature channels" or "specific sequence and feature dimensions." One study notes that these outliers can be consistent "across all token positions." The phenomenon is operationalized by identifying activation values that exceed a defined threshold relative to the mean activation. One paper frames activation outliers as one of three types of systematic outliers, alongside weight and attention outliers.

## Sources

**[Systematic Outliers in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e23bee2df5fc72018d9d74d875d7cf3-Paper-Conference.pdf)**
> The observable phenomenon of abnormally large values appearing in the activation tensors of a model, specifically in layer outputs and down-projection inputs.

**[From Attention to Activation: Unraveling the Enigmas of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/556c2ff2ca01492f14f52d079bdc55f3-Paper-Conference.pdf) (as "Outlier activations in hidden states")**
> The occurrence of activation values in specific feature channels of a Transformer's hidden states that are orders of magnitude larger than other values.
