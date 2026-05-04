# Open-vocabulary semantic segmentation
**Type:** Behavior  
**Referenced in:** 3 papers  
**Also known as:** Open-vocabulary segmentation  

## State of the Field

Across the provided sources, open-vocabulary semantic segmentation is consistently framed as an evaluation task. The definitions describe it as the process of assigning semantic labels to pixels or segmenting objects based on a list of candidate classes without prior training on those specific classes. This behavior is operationalized using established datasets; one paper specifies evaluating models on the ADE20K and PASCAL Context datasets. Performance on this task is measured with metrics such as mean IoU (mIoU) and mean pixel accuracy (mAcc). Another source reinforces its use as a benchmark, referring to it by the abbreviation 'OVS' in an evaluation context.

## Sources

**[FineCLIP: Self-distilled Region-based CLIP for Better Fine-grained Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/3122aaa22b2fe83f9cead1a696f65ceb-Paper-Conference.pdf)**
> Assigning semantic labels to pixels in an open-vocabulary setting.

**[Leveraging Hallucinations to Reduce Manual Prompt Dependency in Promptable Segmentation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c1e1ad233411e25b54bb5df3a0576c2c-Paper-Conference.pdf) (as "Open-vocabulary segmentation")**
> The observable task of segmenting objects based on a list of candidate classes without prior training on those specific classes.
