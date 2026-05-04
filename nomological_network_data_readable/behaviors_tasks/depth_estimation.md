# Depth estimation
**Type:** Behavior  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, depth estimation is consistently defined as the task of predicting the distance of objects or points in a scene from a camera's viewpoint, based on a 2D image. The primary output of this behavior is a 'depth map,' which visually represents these relative distances. The operationalization of this task is described in a few ways. One paper details a module that takes an image as input and produces a depth map using an 'Inferno colormap,' where 'the closer the warmer the color' ("Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models"). Another study mentions the use of a specific model, Depth-Anything-V2, to perform the estimation ("ZooProbe: A Data Engine for Evaluating, Exploring, and Evolving Large-scale Training Data for Multimodal LLMs"). Both sources frame this as a process that takes an image as input and generates a representation of spatial depth.

## Sources

**[Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)**
> Producing a depth map from an image to indicate relative distances of objects from the camera.
