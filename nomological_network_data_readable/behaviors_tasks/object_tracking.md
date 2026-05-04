# Object tracking
**Type:** Behavior  
**Referenced in:** 7 papers  
**Also known as:** Motion tracking  

## State of the Field

The prevailing definition of object tracking across the surveyed literature is the observable behavior of identifying and following the movement of objects across video frames. This behavior is operationalized in several ways, with one paper treating it as a surrogate task requiring a model to output object identifiers and grid positions in a specific format: "<track> object id1, object grid position1; ..." ("Look, Remember and Reason: Grounded Reasoning in Videos with Language Models"). Other approaches evaluate it using datasets like "Tracking Shuffled Objects," which involves following items based on a sequence of instructions, or as a component of answering "relation questions" about referred objects. The behavior, also referred to as "Motion tracking" in one paper, is measured on benchmarks including MVBench, TempCompass, and VideoMMME. A few papers offer more specific framings, defining it as the process of converting per-frame detections into motion trajectories or as determining where a referred object appears across multiple scenes. For instance, one benchmark specifies sub-tasks like "SCENE-REFERRED OBJECT TRACKING (SOS)" and "TEXT-REFERRED OBJECT TRACKING (TOS)". Some work also discusses the use of "off-the-shelf vision tools" to perform this task.

## Sources

**[Large Language Models as Tool Makers](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed91353f700d113e5d848c7e04a858b0-Paper-Conference.pdf)**
> The observable behavior of identifying and following the movement of specific objects across video frames, often by assigning consistent identifiers and reporting bounding boxes or grid positions.

**[Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf) (as "Motion tracking")**
> Following the movement of entities across video frames.
