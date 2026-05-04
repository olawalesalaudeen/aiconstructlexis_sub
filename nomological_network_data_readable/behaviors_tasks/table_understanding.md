# Table understanding
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Table detection, Table structure recognition, Table querying  

## State of the Field

Across the provided literature, Table understanding is characterized as a multifaceted behavior encompassing several distinct tasks rather than a single, unified concept. The most prevalent framing is table question answering, defined as answering questions by extracting and comparing information from a table, which, as one paper notes, "may be updated with new entries" ("Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models"). A more granular perspective, offered in "TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy", breaks the behavior down into visual and structural components: table detection (locating tables in a document), table structure recognition (parsing rows and columns), and table querying (parsing a table at a given location). To operationalize and measure this behavior, researchers employ a wide variety of benchmarks. The most frequently used instruments in this set are WikiTQ and FeTaQA, followed by TabFact. Other datasets such as WikiSQL, BiRdQA, BIG-Bench, HiTab, and FinQA are also used to evaluate table understanding, and one paper operationalizes it via code generation. The behavior is also studied in relation to concepts like table and chart reasoning, task decomposition, and semantic reasoning.

## Sources

**[Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf) (as "Table question answering")**
> Answering questions by extracting and comparing information from a table, optionally integrating additional natural-language updates.

**[TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d97fe65d7a1dc12a05642d9fa4cd578-Paper-Conference.pdf) (as "Table detection")**
> The task of identifying and outputting the bounding box coordinates of all tables within a document image.

**[TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d97fe65d7a1dc12a05642d9fa4cd578-Paper-Conference.pdf) (as "Table structure recognition")**
> The task of parsing the internal structure of a given table image into its constituent elements, such as rows, columns, and cells, and their relationships.

**[TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d97fe65d7a1dc12a05642d9fa4cd578-Paper-Conference.pdf) (as "Table querying")**
> The task of parsing the structure of a table from an entire document image, given a specific location (bounding box) for the table.

## Relationships

### Table understanding →
- **Code generation** (behaviors tasks) — *measured_by*
  - [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf)

### Associated with
- **Table reasoning** (constructs)
  - [TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d97fe65d7a1dc12a05642d9fa4cd578-Paper-Conference.pdf)
