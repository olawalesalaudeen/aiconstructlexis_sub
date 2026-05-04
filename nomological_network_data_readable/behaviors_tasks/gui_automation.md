# GUI automation
**Type:** Behavior  
**Referenced in:** 11 papers  
**Also known as:** GUI control, Clicking, Dragging, Scrolling, GUI interaction, UI control, GUI navigation, Pixel-level operation, On-device control, Mobile device control, Computer interaction  

## State of the Field

Across the surveyed literature, GUI automation is predominantly characterized as the behavior of an agent interacting with a graphical user interface to accomplish tasks. While several terms are used, including 'GUI control,' 'UI control,' and 'GUI interaction,' they consistently describe an agent manipulating graphical elements like windows, buttons, and forms. This behavior is operationalized through a sequence of low-level actions, where agents perceive the device state from visual inputs like screenshots and generate actions such as clicking, typing, and scrolling. Several papers define these actions precisely, such as 'clicking' by specifying coordinates or 'dragging' with start and end points, with one source describing this as performing "pixel-level operations" equivalent to using a mouse. The application context varies, with some work focusing on enterprise software and general desktop environments, while other papers specifically address 'on-device control' for mobile applications. The performance of this behavior is measured by benchmarks, with the provided data identifying `AitW` as one such instrument. GUI automation is studied in relation to `Action prediction` and is suggested by one paper to be an outcome of `Code generation`.

## Sources

**[Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://proceedings.neurips.cc/paper_files/paper/2024/file/c2f71567cd53464161cab3336e8fc865-Paper-Datasets_and_Benchmarks_Track.pdf) (as "GUI control")**
> The observable action of interacting with graphical user interfaces, including navigating web pages, clicking buttons, and filling in forms, to manage enterprise software systems.

**[VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf)**
> Performing end-to-end computer interface tasks by navigating software and executing interface actions to achieve a goal state.

**[VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Clicking")**
> The action of identifying and specifying the coordinates of a target UI element to be clicked.

**[VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Dragging")**
> The action of identifying and specifying both the start and end coordinates for a drag-and-drop operation on a UI element.

**[VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Scrolling")**
> The action of determining whether a target UI element is currently visible and, if not, deciding the direction to scroll (up or down).

**[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf) (as "GUI interaction")**
> Interacting with a computer system by manipulating graphical elements like windows, icons, and buttons using a mouse and keyboard.

**[On the Effects of Data Scale on UI Control Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/a79f3ef3b445fd4659f44648f7ea8ffd-Paper-Datasets_and_Benchmarks_Track.pdf) (as "UI control")**
> The observable behavior of an agent interacting with a digital device's user interface to accomplish tasks specified in natural language.

**[Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf) (as "GUI navigation")**
> Selecting and executing actions on interface elements to complete web or mobile tasks from screenshots and instructions.

**[Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ca0e369689dadb25a5345ba9755ad6f-Paper-Conference.pdf) (as "Pixel-level operation")**
> Executing direct interactions on a GUI such as clicking or typing at specific screen coordinates without relying on underlying code structures.

**[DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9e472cd579c83e2f6aa3459f46aac28-Paper-Conference.pdf) (as "On-device control")**
> The act of operating a mobile device's applications and functionalities to fulfill user requests.

**[What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf) (as "Mobile device control")**
> Completing tasks by operating mobile interfaces and apps through GUI actions.

**[What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf) (as "Computer interaction")**
> Completing tasks through direct interaction with desktop or GUI-based computer interfaces.

## Relationships

### GUI automation →
- **AitW** (measurements) — *measured_by*
  - [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9e472cd579c83e2f6aa3459f46aac28-Paper-Conference.pdf)

### → GUI automation
- **Code generation** (behaviors tasks) — *causes*
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)

### Associated with
- **Action prediction** (behaviors tasks)
  - [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nayak25a/nayak25a.pdf)
