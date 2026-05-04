# Mathematical reasoning
**Type:** Construct  
**Referenced in:** 965 papers  
**Also known as:** Arithmetic reasoning, Math word problem solving, Math problem solving, Arithmetic problem solving, Mathematical problem solving, Mathematical Problem Solving, Multi-digit multiplication, Subtraction, Integer addition, Arithmetic calculation, Modular addition, Multi-digit addition, Arithmetic computation, Binary addition, Modular arithmetic, Digit-wise addition, N-ary addition, Mathematical question answering, Solving nonlinear ordinary differential equations, Polynomial root-finding, Algebraic manipulation, Binary multiplication, Matrix-vector multiplication, Math reasoning, Geometric problem solving, Binary summation, Multi-operand addition, Algebraic question answering, Arithmetic expression evaluation, Integer multiplication, Multi-step math reasoning, Arithmetic solving, Visual math problem solving, Expected value calculation, Present value calculation, Numerical reasoning, Final answer generation, Bitwise arithmetic, Straight-line distance calculation, Median finding, Symbolic expression generation, Numerical addition, Numerical calculation, Linear function evaluation, Element-wise multiplication, Mathematical word problem solving, Problem solving, Numerical computation, Numerical analysis, Mathematical calculation, Arithmetic execution, Three-operand arithmetic solving, Two-integer addition, Carry propagation, Medical calculation, Unit conversion, Number puzzle solving, Symbolic equation solving, Visual equation solving, Free-response math problem solving, Date calculation, Clock-time computation, Weekday understanding, Atom counting, Audio content counting, Counting question answering, Repetition counting, Ring counting, Action counting, String counting, Morphological tag counting, Date arithmetic, Context-based date resolution, Addition, Algebraic reasoning, Arithmetic capability, Geometry reasoning, Mathematical ability, Quantitative reasoning, Mathematical Reasoning, Mathematical capability, Mathematical problem-solving, Mathematical intelligence, Asymptotic reasoning, Numerical RAC, Mathematical understanding, Financial numerical reasoning, Arithmetic ability, Numeric reasoning, Numeracy, Arithmetic computation capability  

## State of the Field

Across the surveyed literature, mathematical reasoning is most commonly characterized as the observable behavior of solving quantitative problems, particularly math word problems that require multiple steps of logical and numerical inference to produce a final answer. The field predominantly operationalizes and measures this behavior through performance on benchmark datasets, with GSM8k and MATH being the most frequently used instruments for evaluation. A wide range of other benchmarks, including SVAMP, AQuA-RAT, and Game of 24, are also used to assess this capability across different problem types and complexities. While word problem solving is the prevailing focus, the concept also covers a broad spectrum of more granular tasks, from basic arithmetic like "integer addition" and "multi-digit multiplication" to specialized computations such as "polynomial root-finding," "object counting," and solving problems in visual contexts. A smaller line of work defines mathematical reasoning as a latent "ability" or "capability," though it is still consistently measured by performance on these observable problem-solving tasks. Several papers report that techniques such as Chain-of-thought reasoning are used to elicit or improve this behavior. The concept is also studied alongside and sometimes correlated with other capabilities like Programming ability and Commonsense knowledge.

## Sources

**[Localized Zeroth-Order Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/9cef1316eaef9bd99da46f63334dc031-Paper-Conference.pdf) (as "Arithmetic reasoning")**
> Solving mathematical word problems that require understanding the text and performing arithmetic calculations.

**[Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf) (as "Math word problem solving")**
> Solving arithmetic word problems and producing the correct numeric answer.

**[D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf) (as "Math problem solving")**
> Solving arithmetic or word problems and producing the numerical answer, often with intermediate calculation steps.

**[Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf) (as "Arithmetic problem solving")**
> Solving numerical word problems or arithmetic questions posed in benchmark format.

**[AlphaMath Almost Zero: Process Supervision without Process](https://proceedings.neurips.cc/paper_files/paper/2024/file/30dfe47a3ccbee68cffa0c19ccb1bc00-Paper-Conference.pdf) (as "Mathematical problem solving")**
> The observable task of receiving a mathematical problem as input and producing a final numerical or symbolic answer as output.

**[Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf) (as "Mathematical Problem Solving")**
> The observable task of solving geometric or mathematical problems presented in visual contexts.

**[Limits of Transformer Language Models on Learning to Compose Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e797d5139ad94fc2dc2080c09119f29-Paper-Conference.pdf) (as "Multi-digit multiplication")**
> Multiplying two multi-digit numbers in base 10 as an explicit output-producing task.

**[Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf) (as "Subtraction")**
> Performing subtraction operations on numerical operands, including anti-symmetric operations.

**[Position Coupling: Improving Length Generalization of Arithmetic Transformers Using Task Structure](https://proceedings.neurips.cc/paper_files/paper/2024/file/27aa3a0e6d63db269977bb2df5607cb8-Paper-Conference.pdf) (as "Integer addition")**
> The task of calculating the sum of two or more integer operands, presented as a sequence of digits.

**[On the Inductive Bias of Stacking Towards Improving Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/837bc5db12f3d394d220815a7687340c-Paper-Conference.pdf) (as "Arithmetic calculation")**
> The observable act of computing the result of a numerical expression.

**[Pre-trained Large Language Models Use Fourier Features to Compute Addition](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cc8dc30e52798b27d37b795cc153310-Paper-Conference.pdf) (as "Modular addition")**
> The observable behavior of computing the remainder of a sum when divided by a modulus, often used to refine an approximate answer.

**[Can Language Models Learn to Skip Steps?](https://proceedings.neurips.cc/paper_files/paper/2024/file/504fa7e518da9d1b53a233ed20a38b46-Paper-Conference.pdf) (as "Multi-digit addition")**
> The arithmetic task of adding two numbers with multiple digits, often performed by generating step-by-step calculations for each digit place.

**[MedCalc-Bench: Evaluating Large Language Models for Medical Calculations](https://proceedings.neurips.cc/paper_files/paper/2024/file/99e81750f3fdfcaf9613db2dbf4bd623-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Arithmetic computation")**
> The observable action of performing mathematical calculations as part of a model's generated output or reasoning chain.

**[DAPE: Data-Adaptive Positional Encoding for Length Extrapolation](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f050fa9f0d898e3f265d515f50ae8f9-Paper-Conference.pdf) (as "Binary addition")**
> Computing the sum of binary numbers.

**[DAPE: Data-Adaptive Positional Encoding for Length Extrapolation](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f050fa9f0d898e3f265d515f50ae8f9-Paper-Conference.pdf) (as "Modular arithmetic")**
> The task of performing arithmetic operations within a system of integers where numbers 'wrap around' upon reaching a certain value, the modulus.

**[G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf) (as "Geometric problem solving")**
> The observable task of receiving a geometric problem, which includes a diagram and text, and producing a final answer, often with a step-by-step solution.

**[Number Cookbook: Number Understanding of Language Models and How to Improve It](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b8ccc9229328bdcedf54b989e7cc330-Paper-Conference.pdf) (as "Digit-wise addition")**
> Performing addition on two numbers digit by digit without carrying over any values.

**[CURIE: Evaluating LLMs on Multitask Scientific Long-Context Understanding and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ae4999aefb509d75d8608e07280922c-Paper-Conference.pdf) (as "Algebraic manipulation")**
> Manipulating symbolic or mathematical expressions to derive or simplify scientific results.

**[Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf) (as "Mathematical question answering")**
> Solving math word problems or math questions in a benchmark setting.

**[SeedLM: Compressing LLM Weights into Seeds of Pseudo-Random Generators](https://proceedings.iclr.cc/paper_files/paper/2025/file/222a2a46018a1e7b55ba48ba11932d04-Paper-Conference.pdf) (as "Matrix-vector multiplication")**
> A core computational operation in neural networks, benchmarked in this study to assess the hardware performance and speed-up achieved by the compression method.

**[HARDMath: A Benchmark Dataset for Challenging Problems in Applied Mathematics](https://proceedings.iclr.cc/paper_files/paper/2025/file/23d64d26abb5a0e9f2014cfcc700f82a-Paper-Conference.pdf) (as "Polynomial root-finding")**
> The task of finding approximate roots for high-order polynomial equations, particularly in different regimes of a small parameter.

**[HARDMath: A Benchmark Dataset for Challenging Problems in Applied Mathematics](https://proceedings.iclr.cc/paper_files/paper/2025/file/23d64d26abb5a0e9f2014cfcc700f82a-Paper-Conference.pdf) (as "Solving nonlinear ordinary differential equations")**
> The task of finding approximate analytical solutions for nonlinear ordinary differential equations (ODEs) in different regimes, such as for small and large values of the independent variable.

**[Looped Transformers for Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/25cc3adf8c85f7c70989cb8a97a691a7-Paper-Conference.pdf) (as "Binary multiplication")**
> The task of performing arithmetic multiplication on two binary numbers.

**[Looped Transformers for Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/25cc3adf8c85f7c70989cb8a97a691a7-Paper-Conference.pdf) (as "Binary summation")**
> The observable task of calculating the sum of a binary string in binary form.

**[Reasoning with Latent Thoughts: On the Power of Looped Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/2676109d49d1eb26d6bc584a8f556305-Paper-Conference.pdf) (as "N-ary addition")**
> Computing the sum of multiple numbers with a specific digit length.

**[As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)**
> Solving math problems that require rigorous logic and stepwise computation.

**[Generalization v.s. Memorization: Tracing Language Models’ Capabilities Back to Pretraining Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf) (as "Math reasoning")**
> Solving grade-school math problems that require intermediate reasoning steps before giving a final answer.

**[Generalizing Reasoning Problems to Longer Lengths](https://proceedings.iclr.cc/paper_files/paper/2025/file/abcbdf504b621b4d1213aa7a5c489f8a-Paper-Conference.pdf) (as "Arithmetic solving")**
> Producing correct arithmetic results for expressions or modular arithmetic problems.

**[Seq-VCR: Preventing  Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf) (as "Integer multiplication")**
> The task of calculating the product of two multi-digit integers and generating the correct numerical result.

**[Seq-VCR: Preventing  Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf) (as "Arithmetic expression evaluation")**
> The task of calculating the value of a mathematical expression containing numbers, operators, and brackets, and generating the final result.

**[Improving Complex Reasoning with Dynamic Prompt Corruption: A Soft Prompt Optimization Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4006ff54a7bbda74c09bad6f7586f5b-Paper-Conference.pdf) (as "Algebraic question answering")**
> The task of answering multiple-choice questions based on algebraic word problems.

**[Improving Complex Reasoning with Dynamic Prompt Corruption: A Soft Prompt Optimization Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4006ff54a7bbda74c09bad6f7586f5b-Paper-Conference.pdf) (as "Multi-step math reasoning")**
> Solving mathematical problems that require multiple intermediate reasoning steps before producing an answer.

**[Arithmetic Transformers Can Length-Generalize in Both Operand Length and Count](https://proceedings.iclr.cc/paper_files/paper/2025/file/c6c29e590e3c62e37e6b39cdd6baf2e8-Paper-Conference.pdf) (as "Multi-operand addition")**
> The task of calculating the sum of multiple integer operands, where both the number of operands and their digit lengths can vary.

**[MAVIS: Mathematical Visual Instruction Tuning with an Automatic Data Engine](https://proceedings.iclr.cc/paper_files/paper/2025/file/db36dcad6baee298a34ffca324b84b09-Paper-Conference.pdf) (as "Visual math problem solving")**
> Solving mathematics questions that require interpreting diagrams or graphs and producing the correct answer.

**[Language Models Trained to do Arithmetic Predict Human Risky and Intertemporal Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3372a60f76e0acce756cb24deead020-Paper-Conference.pdf) (as "Expected value calculation")**
> The observable computational task of determining the average outcome of a probabilistic event by summing the values of each outcome multiplied by its probability.

**[Language Models Trained to do Arithmetic Predict Human Risky and Intertemporal Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3372a60f76e0acce756cb24deead020-Paper-Conference.pdf) (as "Present value calculation")**
> The observable computational task of determining the current worth of a future sum of money or stream of cash flows, given a specified rate of return or discount rate.

**[From Few to Many: Self-Improving Many-Shot Reasoners Through Iterative Optimization and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f22dfaee68dd71f784a82a684b4404bb-Paper-Conference.pdf) (as "Numerical reasoning")**
> Solving problems that require arithmetic or quantitative inference from text.

**[SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.1313.pdf) (as "Final answer generation")**
> The observable output of a numerical answer after performing a series of reasoning steps for a mathematical problem.

**[CRANE: Reasoning with constrained LLM generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/banerjee25a/banerjee25a.pdf) (as "Symbolic expression generation")**
> The task of generating a correct symbolic mathematical expression as a solution to a word problem with symbolic variables.

**[Lower Bounds for Chain-of-Thought Reasoning in Hard-Attention Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bavandpour25a/bavandpour25a.pdf) (as "Median finding")**
> The task of identifying the median value from an input list of N numbers.

**[MapEval: A Map-Based Evaluation of Geo-Spatial Reasoning in Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dihan25a/dihan25a.pdf) (as "Straight-line distance calculation")**
> The specific task of computing the direct distance between two geographical points, often requiring numerical computation.

**[Emergence and Effectiveness of Task Vectors in In-Context Learning: An Encoder Decoder Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25h/han25h.pdf) (as "Bitwise arithmetic")**
> Performing a specified bitwise operation (e.g., AND, OR, XOR) on a pair of binary numbers and outputting the resulting binary number.

**[Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ak/wang25ak.pdf) (as "Linear function evaluation")**
> Computing the value of a linear function such as y = mx + b for given inputs.

**[Everything Everywhere All at Once: LLMs can In-Context Learn Multiple Tasks in Superposition](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25a/xiong25a.pdf) (as "Numerical addition")**
> Generating the correct sum of two numbers when presented with arithmetic expressions in numerical form.

**[RWKVQuant: Quantizing the RWKV Family with Proxy Guided Hybrid of Scalar and Vector Quantization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25at/xu25at.pdf) (as "Element-wise multiplication")**
> A computational operation in RWKV models where input and weight tensors are multiplied element-wise, distinct from matrix multiplication.

**[Can We Predict Performance of Large Models across Vision-Language Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25y/zhao25y.pdf) (as "Numerical calculation")**
> The task of performing mathematical calculations based on information presented in a visual format.

**[Is the Top Still Spinning? Evaluating Subjectivity in Narrative Understanding](https://aclanthology.org/2025.emnlp-main.11.pdf) (as "Problem solving")**
> Generating a correct numerical answer to a math word problem using chain-of-thought reasoning.

**[Idiosyncratic Versus Normative Modeling of Atypical Speech Recognition: Dysarthric Case Studies](https://aclanthology.org/2025.emnlp-main.1702.pdf) (as "Mathematical word problem solving")**
> Solving a natural-language math problem by invoking arithmetic or other math tools and returning the correct numeric answer.

**[A Multi-Agent Framework with Automated Decision Rule Optimization for Cross-Domain Misinformation Detection](https://aclanthology.org/2025.emnlp-main.292.pdf) (as "Numerical computation")**
> The observable behavior of performing mathematical or financial calculations to answer a quantitative question.

**[ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation](https://aclanthology.org/2025.emnlp-main.363.pdf) (as "Numerical analysis")**
> Performing arithmetic operations, comparisons, or trend detection on numerical data extracted from tables, such as calculating growth rates or identifying maxima.

**[Can Vision-Language Models Solve Visual Math Equations?](https://aclanthology.org/2025.emnlp-main.548.pdf) (as "Mathematical calculation")**
> The model performs valid arithmetic operations step-by-step, following correct order of operations and numerical precision rules.

**[LightThinker: Thinking Step-by-Step Compression](https://aclanthology.org/2025.emnlp-main.674.pdf) (as "Arithmetic execution")**
> The observable behavior of performing numerical calculations as part of a reasoning process.

**[Culture Cartography: Mapping the Landscape of Cultural Knowledge](https://aclanthology.org/2025.emnlp-main.92.pdf) (as "Three-operand arithmetic solving")**
> Generating the correct result for arithmetic expressions involving three operands and two operators, such as 'a + b + c = ?'.

**[Image Embedding Sampling Method for Diverse Captioning](https://aclanthology.org/2025.emnlp-main.157.pdf) (as "Counting")**
> Determining the frequency of a specific item in a list by iterating through elements and aggregating occurrences.

**[RLAE: Reinforcement Learning-Assisted Ensemble forLLMs](https://aclanthology.org/2025.emnlp-main.681.pdf) (as "Two-integer addition")**
> The observable task of computing the sum of two integers, either in standard numeric form or under symbolic remapping, serving as a diagnostic for algorithmic reasoning.

**[RLAE: Reinforcement Learning-Assisted Ensemble forLLMs](https://aclanthology.org/2025.emnlp-main.681.pdf) (as "Carry propagation")**
> The sub-task within a larger addition problem of carrying over a value from one columnar position to the next.

**[Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment](https://aclanthology.org/2025.emnlp-main.1302.pdf) (as "Medical calculation")**
> Producing a numerical result or clinical score by applying a predefined formula, rule set, or classification system to patient data.

**[Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment](https://aclanthology.org/2025.emnlp-main.1302.pdf) (as "Unit conversion")**
> Transforming a clinical measurement from one unit to another (e.g., µmol/L to mg/dL) as part of a calculation workflow.

**[2025.emnlp-main.1438.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1438.checklist.pdf) (as "Number puzzle solving")**
> Producing correct solutions to puzzle items that involve numerical reasoning, potentially under multilingual linguistic variation.

**[DischargeSim: A Simulation Benchmark for Educational Doctor–Patient Communication at Discharge](https://aclanthology.org/2025.emnlp-main.547.pdf) (as "Symbolic equation solving")**
> Solving linear equations when the equations are rendered as text in the image.

**[DischargeSim: A Simulation Benchmark for Educational Doctor–Patient Communication at Discharge](https://aclanthology.org/2025.emnlp-main.547.pdf) (as "Visual equation solving")**
> Solving linear equations presented as images with icon-based variables and visually repeated coefficients.

**[2025.emnlp-main.827.checklist](https://aclanthology.org/attachments/2025.emnlp-main.827.checklist.pdf) (as "Free-response math problem solving")**
> Generating step-by-step solutions to open-ended math problems in natural language, mirroring the format and reasoning of human student responses.

**[T2R-BENCH: A Benchmark for Real World Table-to-Report Task](https://aclanthology.org/2025.emnlp-main.1142.pdf) (as "Clock-time computation")**
> The observable task of performing calculations involving clock times, such as determining durations or end times.

**[T2R-BENCH: A Benchmark for Real World Table-to-Report Task](https://aclanthology.org/2025.emnlp-main.1142.pdf) (as "Weekday understanding")**
> The observable task of correctly interpreting and performing calculations involving days of the week and dates.

**[T2R-BENCH: A Benchmark for Real World Table-to-Report Task](https://aclanthology.org/2025.emnlp-main.1142.pdf) (as "Date calculation")**
> Reasoning over calendar dates, weekdays, and multi-day spans to determine valid scheduling windows.

**[SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration inMLLMs](https://aclanthology.org/2025.emnlp-main.56.pdf) (as "Atom counting")**
> Extracting and reporting the number of each type of atom (e.g., carbon, chlorine) present in a given molecular string representation.

**[SPEAttention: Making Attention Equivariant to Semantic-Preserving Permutation for Code Processing](https://aclanthology.org/2025.emnlp-main.333.pdf) (as "Audio content counting")**
> Counting how many times a specified audio event occurs in a video.

**[Predicate-Guided Generation for Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.463.pdf) (as "Counting question answering")**
> Answering questions that require aggregating or counting the frequency of a specific event type or entity attribute within a given time period.

**[DischargeSim: A Simulation Benchmark for Educational Doctor–Patient Communication at Discharge](https://aclanthology.org/2025.emnlp-main.547.pdf) (as "Object counting")**
> The task of determining the quantity of specific objects or icons presented in an image.

**[Facilitating Cognitive Accessibility withLLMs: A Multi-Task Approach to Easy-to-Read Text Generation](https://aclanthology.org/2025.emnlp-main.597.pdf) (as "Repetition counting")**
> The observable task of counting the number of times a specific action or event occurs within a video.

**[TreeReview: A Dynamic Tree of Questions Framework for Deep and EfficientLLM-based Scientific Peer Review](https://aclanthology.org/2025.emnlp-main.791.pdf) (as "Ring counting")**
> Identifying and counting the number of rings of a specific size (e.g., five- or six-membered) in a molecule from its SMILES string.

**[Debatable Intelligence: BenchmarkingLLMJudges via Debate Speech Evaluation](https://aclanthology.org/2025.emnlp-main.954.pdf) (as "Action counting")**
> Detecting and enumerating the number of times a specific action or scene occurs within a video sequence.

**[RAG-Zeval: EnhancingRAGResponses Evaluator through End-to-End Reasoning and Ranking-Based Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.1268.pdf) (as "String counting")**
> The observable behavior of counting how many times a given string appears in a text corpus using an indexed search system.

**[Where to show Demos in Your Prompt: A Positional Bias of In-Context Learning](https://aclanthology.org/2025.emnlp-main.1504.pdf) (as "Morphological tag counting")**
> The task of predicting the total number of morphological tags for a given word.

**[FANS: Formal Answer Selection forLLMNatural Language Math Reasoning Using Lean4](https://aclanthology.org/2025.emnlp-main.159.pdf) (as "Context-based date resolution")**
> Extracting and interpreting a date mentioned in a textual context to answer a question, such as identifying a team associated with a player on a specific date.

**[FANS: Formal Answer Selection forLLMNatural Language Math Reasoning Using Lean4](https://aclanthology.org/2025.emnlp-main.159.pdf) (as "Date arithmetic")**
> The task of performing calculations such as addition or subtraction of days, weeks, or months from a given base date.

**[ProbingLLMWorld Models: Enhancing Guesstimation with Wisdom of Crowds Decoding](https://aclanthology.org/2025.emnlp-main.235.pdf) (as "Temporal reasoning")**
> The observable task of understanding and reasoning about the order and duration of events described in a text.

**[Mastering Symbolic Operations: Augmenting Language Models with Compiled Neural Networks](https://proceedings.iclr.cc/paper_files/paper/2024/file/72679d76c80e079c70fe5977d21ed1e4-Paper-Conference.pdf) (as "Addition")**
> Performing decimal addition of two multi-digit numbers, either in forward or reverse digit order, with or without carry propagation.

**[Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf) (as "Quantitative reasoning")**
> The latent ability of a model to understand and solve mathematical problems, particularly those presented in natural language that require numerical and logical steps.

**[MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf) (as "Algebraic reasoning")**
> The ability to reason about variables, expressions, equations, and functions, particularly in the context of visual representations such as function plots.

**[MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf) (as "Geometry reasoning")**
> The ability to understand and reason about geometric shapes, relationships, and properties, including the use of theorems and spatial configurations.

**[MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf) (as "Statistical reasoning")**
> The ability to interpret and reason about data presented in charts, plots, and tables, including understanding trends, distributions, and statistical relationships.

**[Teaching Arithmetic to Small Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf) (as "Arithmetic capability")**
> The latent ability of a model to perform mathematical calculations such as addition, subtraction, and multiplication.

**[WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/82eec786fdfbbfa53450c5feb7d1ac92-Paper-Conference.pdf) (as "Mathematical ability")**
> The latent ability to solve arithmetic and word problems and handle math-oriented prompts correctly.

**[SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf) (as "Mathematical Reasoning")**
> The capability to solve mathematical and logic-based problems requiring step-by-step deduction.

**[Token-Supervised Value Models for Enhancing Mathematical Problem-Solving Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0801fccb1d705a9e6747e138d9a0056a-Paper-Conference.pdf) (as "Mathematical problem-solving")**
> The latent ability to solve math word problems by producing correct multi-step reasoning and final answers.

**[Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf) (as "Mathematical capability")**
> The model's ability to solve mathematical problems, particularly those requiring arithmetic and logical steps.

**[HARDMath: A Benchmark Dataset for Challenging Problems in Applied Mathematics](https://proceedings.iclr.cc/paper_files/paper/2025/file/23d64d26abb5a0e9f2014cfcc700f82a-Paper-Conference.pdf) (as "Asymptotic reasoning")**
> The model's ability to find approximate analytical solutions to complex mathematical problems by analyzing their behavior in limiting cases, such as when a parameter is very large or very small.

**[Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf) (as "Mathematical intelligence")**
> The broader latent quality reflected by benchmark performance that is intended to track genuine mathematical ability more faithfully and linearly than traditional tests.

**[ActionReasoningBench: Reasoning about Actions with and without Ramification Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf42f133f355e0e07a8957b508b26a1b-Paper-Conference.pdf) (as "Numerical RAC")**
> The ability to perform reasoning about actions and change that requires a numerical answer, combining RAC with quantitative skills.

**[ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf) (as "Mathematical understanding")**
> The latent capability to solve grade-school math problems that require multi-step numerical reasoning.

**[MMDocIR: Benchmarking Multimodal Retrieval for Long Documents](https://aclanthology.org/2025.emnlp-main.1577.pdf) (as "Financial numerical reasoning")**
> The latent ability of a model to perform multi-step computations involving financial data by integrating information from text and tables, applying domain-specific logic, and generating executable programs to derive correct answers.

**[A Closer Look at Machine Unlearning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b7db41ea66d624587f211aa15c07e45-Paper-Conference.pdf) (as "Arithmetic ability")**
> The capacity to solve grade-school or similar numerical computation problems.

**[Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Numeric reasoning")**
> The ability to extract numerical information from product metadata and perform calculations to answer questions.

**[Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf) (as "Numeracy")**
> The model's general capability regarding numerical tasks and arithmetic operations.

**[MedCalc-Bench: Evaluating Large Language Models for Medical Calculations](https://proceedings.neurips.cc/paper_files/paper/2024/file/99e81750f3fdfcaf9613db2dbf4bd623-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Arithmetic computation capability")**
> The model's underlying ability to perform mathematical operations like addition, subtraction, and exponentiation correctly as part of a larger reasoning process.

## Relationships

### Mathematical reasoning →
- **GSM8k** (measurements) — *measured_by*
  - [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf)
- **MATH** (measurements) — *measured_by*
  > We evaluate DTV on three quantitative reasoning datasets: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021) and MultiArith (Roy & Roth, 2016).
  - [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf)
- **SVAMP** (measurements) — *measured_by*
  > “We evaluate the MathCoder on five datasets, including two in-domain datasets: GSM8K (Cobbe et al., 2021) and MATH (Hendrycks et al., 2021); and three out-of-domain datasets: SVAMP (Patel et al., 2021), Mathematics (Saxton et al., 2019), and SimulEq (Kushman et al., 2014).”
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
- **MATH-500** (measurements) — *measured_by*
  > We evaluated the effectiveness of the PRM on Gemma2-2B-it, Gemma2-9B-it(Team et al., 2024), Phi-3-mini-4k-Instruct (3.8B) (Abdin et al., 2024), which are from different origins than the data generation models, using the PRM weighted Best-of-N search on MATH500.
  - [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf)
- **AQuA-RAT** (measurements) — *measured_by*
  - [Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf)
- **ASDIV** (measurements) — *measured_by*
  > We evaluate our LLM cascade approaches on six datasets, covering (1) mathematical reasoning, including GSM8k (Cobbe et al., 2021), ASDIV (Ling et al., 2017), and TabMWP (Lu et al., 2023); (2) symbolic reasoning from BIG-Bench Hard (bench authors, 2023), including DATE and Navigate; and (3) causal reasoning, including CREPE (Zhang et al., 2023). (Section 3.1)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
- **AIME 2024** (measurements) — *measured_by*
  > We select two math datasets to evaluate the performance, for one easy math dataset, GSM8K (Cobbe et al., 2021b) and one hard math dataset, AIME24. (Section 4.1)
  - [OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/302ce0673c00aee2cf84bb43d0117553-Paper-Conference.pdf)
- **OlympiadBench** (measurements) — *measured_by*
  > we select several widely recognized and representative benchmarks, including MathVista (Lu et al., 2024a), Math-Verse (Zhang et al., 2024a), MathVision (Wang et al., 2024a), Dynamath (Zou et al., 2024), and OlympiadBench (He et al., 2024). (Section 4.2)
  - [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf)
- **MultiArith** (measurements) — *measured_by*
  > We evaluate DTV on three quantitative reasoning datasets: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021) and MultiArith (Roy & Roth, 2016).
  - [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf)
- **MAWPS** (measurements) — *measured_by*
  > “we validate the efficacy and efficiency of Prompt-OIRL in offline prompt evaluation and optimization through experiments with 3 distinct LLMs, namely GPT-3.5-turbo, LLaMA-2-7B-Chat, and TigerBot-13B-Chat, across 3 arithmetic datasets: GSM8K (Cobbe et al., 2021a), MAWPS (Roy & Roth, 2016), and SVAMP(Patel et al., 2021)”
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
- **MathQA** (measurements) — *measured_by*
  > Datasets like MathQA (Amini et al., 2019), GSM8k (Cobbe et al., 2021), MATH (Hendrycks et al., 2021b), and SVAMP (Patel et al., 2021) focus on math word problems requiring multi-step reasoning and problem-solving (Section 5).
  - [MathPile: A Billion-Token-Scale Pretraining Corpus for Math](https://proceedings.neurips.cc/paper_files/paper/2024/file/2d0be3cd5173c10b6ec075d1c393a13d-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AMC** (measurements) — *measured_by*
  > we evaluate the model on mathematical reasoning questions. ... we report the pass@1 score ... on the AIME 2024 and AMC datasets. (Section 5)
  - [A Logical Fallacy-Informed Framework for Argument Generation](https://aclanthology.org/2025.naacl-long.375.pdf)
- **MathVista** (measurements) — *measured_by*
  - [Evaluating Large Vision-and-Language Models on Children's Mathematical Olympiads](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cc12fb3d4033ad72d33a51f1d0ab5d0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AddSub** (measurements) — *measured_by*
  > we ... test on six different math reasoning datasets: MultiArith (Roy and Roth, 2016), GSM8K (Cobbe et al., 2021), AddSub (Hosseini et al., 2014), AQuA (Ling et al., 2017), SingleEq (Koncel-Kedziorski et al., 2015) and SVAMP (Patel et al., 2021). (Section 4.1)
  - [OccamLLM: Fast and Exact Language Model Arithmetic in a Single Step](https://proceedings.neurips.cc/paper_files/paper/2024/file/3eceb70f47690051d6769739fbf6294b-Paper-Conference.pdf)
- **MGSM** (measurements) — *measured_by*
  > ...the latter two focus on examining the agents’ reasoning abilities, including mathematical and logical reasoning. (Section 3.1)
  - [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf)
- **SingleEq** (measurements) — *measured_by*
  > we ... test on six different math reasoning datasets: MultiArith (Roy and Roth, 2016), GSM8K (Cobbe et al., 2021), AddSub (Hosseini et al., 2014), AQuA (Ling et al., 2017), SingleEq (Koncel-Kedziorski et al., 2015) and SVAMP (Patel et al., 2021). (Section 4.1)
  - [OccamLLM: Fast and Exact Language Model Arithmetic in a Single Step](https://proceedings.neurips.cc/paper_files/paper/2024/file/3eceb70f47690051d6769739fbf6294b-Paper-Conference.pdf)
- **MATH10K** (measurements) — *measured_by*
  > For arithmetic reasoning benchmarks, we use the Math10K dataset. (Section 5.3)
  - [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf)
- **College Math** (measurements) — *measured_by*
  > We also incorporate two more challenging datasets, OlympiadBench (He et al., 2024) and CollegeMath (Tang et al., 2024), to further test our model’s generalizability on out-of-distribution challenging problems.
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
- **GSM-Hard** (measurements) — *measured_by*
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
- **Game of 24** (measurements) — *measured_by*
  > IGE reaches 100% success rate on Game of 24 (Yao et al., 2023a), a standard mathematical reasoning and search problem, 70.8% faster than classic graph search.
  - [Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf)
- **AIME** (measurements) — *measured_by*
  > We assess both models on the challenging American Invitational Mathematics Examination (AIME 24) benchmark. (Section 3.3, Chain-of-Thought Reasoning Evaluation).
  - [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf)
- **Minerva Math** (measurements) — *measured_by*
  > Second, to simulate a use-case where ex-ante quality estimation is accurate, we use the Math and Coder models from the QWEN-2.5 model family (Yang et al., 2024; Hui et al., 2024) and evaluate them on a combination of Minerva Math (Lewkowycz et al., 2022) and LiveCodeBench (Jain et al., 2024). (Section 5.2)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
- **TabMWP** (measurements) — *measured_by*
  > We evaluate our LLM cascade approaches on six datasets, covering (1) mathematical reasoning, including GSM8k (Cobbe et al., 2021), ASDIV (Ling et al., 2017), and TabMWP (Lu et al., 2023); (2) symbolic reasoning from BIG-Bench Hard (bench authors, 2023), including DATE and Navigate; and (3) causal reasoning, including CREPE (Zhang et al., 2023). (Section 3.1)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
- **TheoremQA** (measurements) — *measured_by*
  > ...GSM-Plus (Li et al., 2024), MATH, TheoremQA (Chen et al., 2023), SVAMP (Patel et al., 2021), and ASDiv (Miao et al., 2020) for math...
  - [MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf)
- **GSM-Plus** (measurements) — *measured_by*
  > The model’s performance is evaluated on two grade school math benchmarks: GSM8k (Cobbe et al., 2021) and GSM-Plus (Li et al., 2024), which is an adversarial version of GSM8k. (Section 4.4)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
- **Omni-MATH** (measurements) — *measured_by*
  > We evaluate our models on a set of common benchmarks that consists of GSM8K (1.3K examples), MATH (5K examples), AMC 2023 (40 examples), AIME 2024 (30 examples), and Omni-MATH (4.4K examples) ... These datasets cover a broad spectrum of difficulty levels, ranging from grade school mathematics to advanced competition problems.
  - [OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/302ce0673c00aee2cf84bb43d0117553-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **NumGLUE** (measurements) — *measured_by*
  > Mathematic reasoning: GSM8K math problem dataset (Cobbe et al., 2021) and NumGLUE dataset (Mishra et al., 2022). (Section 4.1.1)
  - [SmallToLarge (S2L): Scalable Data Selection for Fine-tuning Large Language Models by Summarizing Training Trajectories of Small Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/97fe251c25b6f99a2a23b330a75b11d4-Paper-Conference.pdf)
- **SAT-Math** (measurements) — *measured_by*
  > the performance for the math domain is the average result of GSM8K (Pass@1) (Cobbe et al., 2021), MATH (Pass@1) (Hendrycks et al., 2021), SAT-Math (Acc) (Zhong et al., 2023), and AQuA-RAT (Acc) (Ling et al., 2017) datasets. (Figure 1)
  - [BAdam: A Memory Efficient Full Parameter Optimization Method for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2c570b0f9938c7a58a612e5b00af9cc0-Paper-Conference.pdf)
- **MathVerse** (measurements) — *measured_by*
  > "To verify the generalization ability of G-LLaVA, we also conduct evaluation on the newly introduced MathVerse benchmark"
  - [DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/78b248ea6f627431bba5029d92be8a3d-Paper-Conference.pdf)
- **CollegeMath** (measurements) — *measured_by*
  - [E](https://aclanthology.org/2025.acl-long.417.pdf)
- **AIME 2025** (measurements) — *measured_by*
  > "Math: AIME 2024 and AIME 2025 (MAA Committees), each consisting of 30 challenging mathematical questions designed to test mathematical reasoning skills."
  - [Whisper-UT: A Unified Translation Framework for Speech and Text](https://aclanthology.org/2025.emnlp-main.149.pdf)
- **MMLU-Math** (measurements) — *measured_by*
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **SimulEq** (measurements) — *measured_by*
  > “We evaluate the MathCoder on five datasets, including two in-domain datasets: GSM8K (Cobbe et al., 2021) and MATH (Hendrycks et al., 2021); and three out-of-domain datasets: SVAMP (Patel et al., 2021), Mathematics (Saxton et al., 2019), and SimulEq (Kushman et al., 2014).”
  - [MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/15425f2df99aa1ba52712c9a4afc8536-Paper-Conference.pdf)
- **MMLU-STEM** (measurements) — *measured_by*
  > We consider three diverse math benchmarks to comprehensively evaluate the mathematical reasoning ability. These benchmarks encompass... conceptual science and math reasoning (5-shot MMLU-STEM...)
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  > “Table 1 reports the zero-shot results on the LM Eval Harness benchmark (Gao et al., 2023).”
  - [$\texttt{Model-GLUE}$: Democratized LLM Scaling for A Large Model Zoo in the Wild](https://proceedings.neurips.cc/paper_files/paper/2024/file/180a476f22a52b8ef14f42b2b927afcc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AMC 2023** (measurements) — *measured_by*
  > For the in-domain scenario, we evaluate our method on several challenging open-source mathematical benchmarks, including MATHOAI (Lightman et al., 2024), AIME2024, and AMC2023. (Section 5.1)
  - [OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/302ce0673c00aee2cf84bb43d0117553-Paper-Conference.pdf)
- **Geometry3k** (measurements) — *measured_by*
  > "Additionally, we show the results of sub-tasks on MathVista-GPS multiple-choice questions for easier evaluation in Table 15, which includes GeoQA+, UniGeo, Geometry3K, and GEOS."
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
- **OCWCourses** (measurements) — *measured_by*
  - [AlphaMath Almost Zero: Process Supervision without Process](https://proceedings.neurips.cc/paper_files/paper/2024/file/30dfe47a3ccbee68cffa0c19ccb1bc00-Paper-Conference.pdf)
- **SAT** (measurements) — *measured_by*
  > We compare the model performances on nine mathematics-related benchmarks used in RHO-1 (Lin et al., 2024) and ProX (Zhou et al., 2024a). The evaluation is conducted using the same implementation and includes few-shot chain-of-thought (CoT) examples.
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **MMStar** (measurements) — *measured_by*
  > The performance of LLaVA-Next-LLaMA3-8B model with merged task vectors across math-related Benchmarks: MathVista ..., MathVerse ..., MMStar ..., DynaMath ..., MathVision ... (Table 2)
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)
- **Logit lens** (measurements) — *measured_by*
  - [Pre-trained Large Language Models Use Fourier Features to Compute Addition](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cc8dc30e52798b27d37b795cc153310-Paper-Conference.pdf)
- **Spec-Bench** (measurements) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
- **InfiniteBench** (measurements) — *measured_by*
  > maintaining efficacy in complex mathematical and coding tasks.
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
- **MetaMath** (measurements) — *measured_by*
  > “we sampled some challenging problems from NuminaMath (Li et al., 2024b) and MetaMath(Yu et al., 2023).”
  - [Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf)
- **OCW** (measurements) — *measured_by*
  > Math: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021), OCW (Lewkowycz et al., 2022), SAT (Azerbayev et al., 2023), and MMLU STEM (Hendrycks et al., 2020)
  - [MathCoder2: Better Math Reasoning from Continued Pretraining on Model-translated Mathematical Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/bea94fe9c5573e74294657f692069d89-Paper-Conference.pdf)
- **GaoKao** (measurements) — *measured_by*
  - [Advancing Mathematical Reasoning in Language Models: The Impact of Problem-Solving Data, Data Synthesis Methods, and Training Stages](https://proceedings.iclr.cc/paper_files/paper/2025/file/aab3003c922e0fcd2fd2c951fa3c03ad-Paper-Conference.pdf)
- **GeoQA** (measurements) — *measured_by*
  > We evaluate G-LLaVA on the geometry problems solving (GPS) task (testmini split) of MathVista (Lu et al., 2023) and test set of GeoQA. (Section 5.1)
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)
- **Programming** (behaviors tasks) — *correlates*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **LiveBench** (measurements) — *measured_by*
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **GSM-symbolic** (measurements) — *measured_by*
  > "GSM-Symbolic (Mirzadeh et al., 2024), a dataset consisting of math word problems designed to assess LLMs’ mathematical reasoning skills"
  - [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ec2e7a896f8250986b3907f57621ce94-Paper-Conference.pdf)
- **Math Hard** (measurements) — *measured_by*
  > However, progress remains slower in the Math Hard, where scores are consistently lower. This suggests that while MPO iterations are becoming more robust overall, further optimization is needed for specialized tasks like complex mathematical reasoning. (Section 4.2)
  - [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf)
- **Dynamath** (measurements) — *measured_by*
  > we select several widely recognized and representative benchmarks, including MathVista (Lu et al., 2024a), Math-Verse (Zhang et al., 2024a), MathVision (Wang et al., 2024a), Dynamath (Zou et al., 2024), and OlympiadBench (He et al., 2024). (Section 4.2)
  - [AbGen: Evaluating Large Language Models in Ablation Study Design and Evaluation for Scientific Research](https://aclanthology.org/2025.acl-long.612.pdf)
- **GPQA-Diamond** (measurements) — *measured_by*
  - [A Logical Fallacy-Informed Framework for Argument Generation](https://aclanthology.org/2025.naacl-long.375.pdf)
- **MathVision** (measurements) — *measured_by*
  > Math and Science includes MathVision, G-LLaVA, SQA, and AI2D, focusing on scientific knowledge and mathematical reasoning.
  - [AbGen: Evaluating Large Language Models in Ablation Study Design and Evaluation for Scientific Research](https://aclanthology.org/2025.acl-long.612.pdf)
- **CMATH** (measurements) — *measured_by*
  > "We evaluate our method on nine English and Chinese math benchmarks ... including widely used benchmarks like GSM8K ... and various Chinese math datasets"
  - [Policy Filtration for RLHF to Mitigate Noise in Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bq/zhang25bq.pdf)
- **Minerva** (measurements) — *measured_by*
  > Table 1: Performance (%) on mathematical benchmarks. (Table 1)
  - [Whisper-UT: A Unified Translation Framework for Speech and Text](https://aclanthology.org/2025.emnlp-main.149.pdf)
- **MinervaMATH** (measurements) — *measured_by*
  > We conduct experiments on mathematical reasoning datasets with different difficulties (GSM8K, MATH500, and MinervaMATH), presenting the reasonableness of AutoMeco and the effectiveness of MIRA. (Section 1)
  - [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.171.pdf)
- **Arithmetic** (measurements) — *measured_by*
  - [Pay More Attention to Images: Numerous Images-Oriented Multimodal Summarization](https://aclanthology.org/2025.naacl-long.475.pdf)
- **GSM8K-Hard** (measurements) — *measured_by*
  > To evaluate performance, we assess the model on 9 mathematical reasoning benchmarks covering diverse domains, question formats (multiple-choice and open-ended), and difficulty levels (elementary to university): GSM8k (Cobbe et al., 2021), MATH (Hendrycks et al., 2021b), GSM-Hard (Gao et al., 2022), SVAMP (Patel et al., 2021), ASDiv (Miao et al., 2020), MAWPS (Koncel-Kedziorski et al., 2016), TabMWP (TAB) (Lu et al., 2023), MathQA (MQA) (Amini et al., 2019), MMLU-STEM (Hendrycks et al., 2021a), and SAT (Azerbayev et al., 2024). (Section 4.1)
  - [Mastering Symbolic Operations: Augmenting Language Models with Compiled Neural Networks](https://proceedings.iclr.cc/paper_files/paper/2024/file/72679d76c80e079c70fe5977d21ed1e4-Paper-Conference.pdf)
- **Prompt engineering** (behaviors tasks) — *measured_by*
  - [SimulS2S-LLM: Unlocking Simultaneous Inference of SpeechLLMs for Speech-to-Speech Translation](https://aclanthology.org/2025.acl-long.818.pdf)
- **BBH** (measurements) — *measured_by*
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
- **DROP** (measurements) — *measured_by*
  > Besides, we also provide more experimental results on the decontextualized versions of a subset of DROP (Dua et al., 2019) and IIRC (Ferguson et al., 2020) in Appendix D.1. (Section 5.1)
  - [Agent-Oriented Planning in Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/31610e68fe41a62e460e044216a10766-Paper-Conference.pdf)
- **miniF2F** (measurements) — *measured_by*
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)
- **SciBench** (measurements) — *measured_by*
  - [MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf)
- **TACT** (measurements) — *measured_by*
  - [TACT: Advancing Complex Aggregative Reasoning with Information Extraction Tools](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d7025dc9bd4c8b6fb1eef80cc618008-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Hugging Face Open LLM Leaderboard** (measurements) — *measured_by*
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **BIG-Bench** (measurements) — *measured_by*
  - [Seq-VCR: Preventing  Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf)
- **MathOdyssey** (measurements) — *measured_by*
  > recent math specific competition and Olympiad-level benchmarking on Math Odyssey (Fang et al., 2024), OlymiadBench (He et al., 2024), and the American Invitational Mathematics Examination (AIME) & the American Mathematics Competitions (AMC) (Beeching et al., 2024; DeepSeek-AI et al., 2024; Reid et al., 2024) questions show that the state-of-the-art (SOTA), both generalist and specialist, LLMs continue to struggle with advanced math reasoning. (Section 1.1).
  - [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf)
- **TRACE** (measurements) — *measured_by*
  > we also addressed the effectiveness of our approach on the public benchmark TRACE Wang et al. (2023c), which includes a learning sequence comprised of multi-choice QA, code generation, mathematical reasoning, and summarization tasks. (Section 6)
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **IIRC** (measurements) — *measured_by*
  > Besides, we also provide more experimental results on the decontextualized versions of a subset of DROP (Dua et al., 2019) and IIRC (Ferguson et al., 2020) in Appendix D.1. (Section 5.1)
  - [Agent-Oriented Planning in Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/31610e68fe41a62e460e044216a10766-Paper-Conference.pdf)
- **Activation patching** (measurements) — *measured_by*
  - [Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5f30296296d2ae402ebbd09aaa9c12-Paper-Conference.pdf)
- **Linear probing** (measurements) — *measured_by*
  - [Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5f30296296d2ae402ebbd09aaa9c12-Paper-Conference.pdf)
- **Reward-Bench** (measurements) — *measured_by*
  - [Are Generative Models Underconfident? Better Quality Estimation with Boosted Model Probability](https://aclanthology.org/2025.emnlp-main.167.pdf)
- **GeoS** (measurements) — *measured_by*
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)
- **JEEBench** (measurements) — *measured_by*
  - [PORT: Preference Optimization on Reasoning Traces](https://aclanthology.org/2025.naacl-long.550.pdf)
- **FinQA** (measurements) — *measured_by*
  > datasets such as FinQA (Chen et al., 2021b) and ConvFinQA (Chen et al., 2022) have been developed to benchmark deep learning models for such numerical reasoning tasks in the financial domain.
  - [MMDocIR: Benchmarking Multimodal Retrieval for Long Documents](https://aclanthology.org/2025.emnlp-main.1577.pdf)
- **VoxEval** (measurements) — *measured_by*
  > and 3) pioneers the assessment of complex tasks like mathematical reasoning in spoken format. (Abstract)
  - [SimulS2S-LLM: Unlocking Simultaneous Inference of SpeechLLMs for Speech-to-Speech Translation](https://aclanthology.org/2025.acl-long.818.pdf)
- **PRM800K** (measurements) — *measured_by*
  > PRM800K (Lightman et al., 2024) is derived from the MATH dataset (Hendrycks et al., 2021), which contains challenging competition-level math problems. (Section 4.2)
  - [ImpliRet: Benchmarking the Implicit Fact Retrieval Challenge](https://aclanthology.org/2025.emnlp-main.1686.pdf)
- **MMLU-redux** (measurements) — *measured_by*
  - [Fann or Flop: A Multigenre, Multiera Benchmark forArabic Poetry Understanding inLLMs](https://aclanthology.org/2025.emnlp-main.1024.pdf)
- **JudgeBench** (measurements) — *measured_by*
  > JudgeBench is a recent benchmark that evaluates LLM-based judges on challenging response pairs spanning knowledge, reasoning, math, and coding. (Section 3)
  - [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saha25b/saha25b.pdf)
- **AlpacaEval 2.0** (measurements) — *measured_by*
  > To test our hypothesis, we break down the prompts in Alpaca Eval 2.0 (Li et al., 2023) into different categories. ... We select four representative tasks: two are objective tasks that can be verified: mathematical reasoning or calculation (Math) and Coding...
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)
- **CMedCalc-Bench** (measurements) — *measured_by*
  > In this paper, we introduce CMedCalc-Bench, a new benchmark designed for Chinese medical calculation. (Abstract)
  - [Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment](https://aclanthology.org/2025.emnlp-main.1302.pdf)
- **GSM8K-Aug** (measurements) — *measured_by*
  > “We use the GSM8k-Aug dataset from (Deng et al., 2023), which has proven effective for training implicit CoT methods”
  - [MIO: A Foundation Model on Multimodal Tokens](https://aclanthology.org/2025.emnlp-main.256.pdf)
- **AGIEval-Math** (measurements) — *measured_by*
  > "AGIEval-Math (Zhong et al., 2023) is used as an out-of-distribution (OOD) test set."
  - [Answering Narrative-Driven Recommendation Queries via a Retrieve–Rank Paradigm and theOCG-Agent](https://aclanthology.org/2025.emnlp-main.668.pdf)
- **GaoKao 2023 En** (measurements) — *measured_by*
  > “We assess models’ mathematical reasoning on synthetic data using diverse benchmarks, including GSM8K (Cobbe et al., 2021), MATH-500(MATH) (Lightman et al., 2023), MathQA (Amini et al., 2019), OlympiadBench-Math(Olympiad) (He et al., 2024), OmniMATH(Omni) (Gao et al., 2024), Gaokao 2023 En(Gaokao) (Liao et al., 2024), and CollegeMath(College) (Tang et al., 2024).”
  - [Can Large Language Models Be Good Language Teachers?](https://aclanthology.org/2025.emnlp-main.1223.pdf)
- **COMPLEXTEMPQA** (measurements) — *measured_by*
  > The dataset includes diverse categories of questions, such as attribute-, comparison-, and counting-type questions, each pertaining to events, entities, or time periods.
  - [Predicate-Guided Generation for Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.463.pdf)
- **MCBench** (measurements) — *measured_by*
  > MCBench evaluates three key capabilities of LLMs: ... • Mathematical Reasoning: Each step requires precise arithmetic operations.
  - [DSVD: Dynamic Self-Verify Decoding for Faithful Generation in Large Language Models](https://aclanthology.org/2025.emnlp-main.1051.pdf)
- **TableEval** (measurements) — *measured_by*
  > This approach accommodates various task types within diverse real-world industrial scenarios, including information retrieval, numerical analysis, table reasoning, data analysis, multi-turn dialogue, and understanding of table structures. (Section 3.1)
  - [ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation](https://aclanthology.org/2025.emnlp-main.363.pdf)

### → Mathematical reasoning
- **Chain-of-thought reasoning** (constructs) — *causes*
  > In the first stage, we extract hierarchical high-level and detailed thought templates from the teacher model to guide the student model in eliciting more fine-grained reasoning thoughts.
  - [UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/7c06759d1a8567f087b02e8589454917-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Critique** (behaviors tasks) — *causes*
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **Backward reasoning** (behaviors tasks) — *causes*
  - [MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c400474e8a36d0812fdee52739288b12-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  > State-of-the-art MLLMs suffer severe hallucination on geometric figures, which greatly hinders their abilities on solving geometric problems. (Figure 1)
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)
- **Tool use** (behaviors tasks) — *causes*
  - [Are We Done withMMLU?](https://aclanthology.org/2025.naacl-long.263.pdf)
- **In-context learning** (constructs) — *causes*
  - [What Makes In-context Learning Effective for Mathematical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ac/liu25ac.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [AlphaMath Almost Zero: Process Supervision without Process](https://proceedings.neurips.cc/paper_files/paper/2024/file/30dfe47a3ccbee68cffa0c19ccb1bc00-Paper-Conference.pdf)
- **Visual understanding** (constructs) — *causes*
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **Algorithmic reasoning** (constructs) — *measured_by*
  - [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf)
- **MR-Ben** (measurements) — *measured_by*
  - [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf)
- **Prompt engineering** (behaviors tasks) — *causes*
  - [Code-Switching Red-Teaming:LLMEvaluation for Safety and Multilingual Understanding](https://aclanthology.org/2025.acl-long.658.pdf)
- **Expressive power** (constructs) — *causes*
  > The proposed method increases expressivity by redesigning two primary attention modules to improve categorical and numerical reasoning capabilities.
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
- **Model collapse** (constructs) — *causes*
  - [Seq-VCR: Preventing  Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf)
- **Cognitive ability** (constructs) — *correlates*
  - [World Models with Hints of Large Language Models for Goal Achieving](https://aclanthology.org/2025.naacl-long.4.pdf)
- **Formal theorem proving** (behaviors tasks) — *causes*
  - [People who frequently useChatGPTfor writing tasks are accurate and robust detectors ofAI-generated text](https://aclanthology.org/2025.acl-long.268.pdf)

### Associated with
- **Chain-of-thought reasoning** (constructs)
  > Although recent large language models (LLMs) (Jiang et al., 2023; Dubey et al., 2024) have showcased extensive capabilities across various domains, they still face challenges with complex multi-step reasoning tasks such as mathematical problem-solving. (Section 1)
  - [MAmmoTH: Building Math Generalist Models through Hybrid Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b063829b922fdeb4fa3472dd3471ff43-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks)
  > Complex reasoning has been an intriguing ability of large language models (LLMs), with application in for example mathematical problem-solving (Section 1).
  - [DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf)
- **Logical reasoning** (constructs)
  > “LLMs frequently fail to solve discrete mathematics problems and often make logical missteps, highlighting significant challenges in mathematical reasoning and problem-solving for LLMs.”
  - [MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf)
- **Memorization** (constructs)
  > However, the ability to recover from or correct errors in the reasoning process is generally poor across most models. This can be attributed to data memorization and potential contamination in training datasets, where models may have encountered similar/same problems before.
  - [Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5f30296296d2ae402ebbd09aaa9c12-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks)
  > Large language models (LLMs)... have demonstrated their superior capability in... mathematical reasoning... Optimization problem solving... is a field of applied mathematics
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
- **Table reasoning** (constructs)
  - [Instantly Learning Preference Alignment via In-contextDPO](https://aclanthology.org/2025.naacl-long.9.pdf)
- **Pattern recognition** (constructs)
  > “Mathematical problem solving requires a series of deductive reasoning steps, where each step is performed under a small set of premises.” (Section 1)
  - [Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mukherjee25a/mukherjee25a.pdf)
- **Textual reasoning** (behaviors tasks)
  - [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Commonsense knowledge** (constructs)
  - [How Private are Language Models in Abstractive Summarization?](https://aclanthology.org/2025.emnlp-main.1532.pdf)
- **Theorem proving** (behaviors tasks)
  - [Proving Olympiad Algebraic Inequalities without Human Demonstrations](https://proceedings.neurips.cc/paper_files/paper/2024/file/96f8c5e879c339dae55e6c2188b02a33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Length generalization** (constructs)
  - [What Algorithms can Transformers Learn? A Study in Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/45ed1a72597594c097152ef9cc187762-Paper-Conference.pdf)
- **Formal theorem proving** (behaviors tasks)
  - [LeanAgent: Lifelong Learning for Formal Theorem Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/b67c77f8db8b991d73d6f2e16f491840-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf)
- **Self-correction** (behaviors tasks)
  - [SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.1313.pdf)
- **Commonsense reasoning** (constructs)
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
- **Generalization** (constructs)
  > Unlike prior studies that primarily focus on tasks from a single domain, our method demonstrates strong generalizability across web agents, mathematical reasoning, and scientific discovery domains, further proving its effectiveness. (Section 2)
  - [Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces](https://proceedings.iclr.cc/paper_files/paper/2025/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **Easy-to-hard generalization** (constructs)
  - [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks)
  - [Position Coupling: Improving Length Generalization of Arithmetic Transformers Using Task Structure](https://proceedings.neurips.cc/paper_files/paper/2024/file/27aa3a0e6d63db269977bb2df5607cb8-Paper-Conference.pdf)
- **Planning** (constructs)
  - [Unlocking the Capabilities of Thought: A Reasoning Boundary Framework to Quantify and Optimize Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/62ab1c2cb4b03e717005479efb211841-Paper-Conference.pdf)
- **Prompt engineering** (behaviors tasks)
  - [Localized Zeroth-Order Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/9cef1316eaef9bd99da46f63334dc031-Paper-Conference.pdf)
- **Algorithmic reasoning** (constructs)
  - [Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5f30296296d2ae402ebbd09aaa9c12-Paper-Conference.pdf)
- **Data analysis** (behaviors tasks)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Data contamination** (constructs)
  > However, the ability to recover from or correct errors in the reasoning process is generally poor across most models. This can be attributed to data memorization and potential contamination in training datasets, where models may have encountered similar/same problems before.
  - [SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.1313.pdf)
- **Accuracy** (constructs)
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)
- **Decision-making** (constructs)
  - [Competing Large Language Models in Multi-Agent Gaming Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/a46adbe2f0ca0e16ef8857e188991ad7-Paper-Conference.pdf)
- **Geometric reasoning** (constructs)
  > Geometry reasoning problem is a challenging visual mathematical reasoning problem.
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)
- **State tracking** (constructs)
  - [Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a0ce3abb720b740419e193c87afd080-Paper-Conference.pdf)
- **Analytical reasoning** (constructs)
  - [Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.332.pdf)
- **Tabular reasoning** (constructs)
  - [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Logical deduction** (measurements)
  - [Critical Tokens Matter: Token-Level Contrastive Estimation Enhances LLM’s Reasoning Capability](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25j/lin25j.pdf)
- **Conciseness** (constructs)
  - [2025.emnlp-main.287.checklist](https://aclanthology.org/attachments/2025.emnlp-main.287.checklist.pdf)
- **Compositional generalization** (constructs)
  - [RLAE: Reinforcement Learning-Assisted Ensemble forLLMs](https://aclanthology.org/2025.emnlp-main.681.pdf)
- **Rule-based reasoning** (constructs)
  > Large language models (LLMs) continue to face challenges in reliably solving reasoning tasks, particularly tasks that involve precise rule following, as often found in mathematical reasoning tasks.
  - [Are Vision-Language Models Safe in the Wild? A Meme-Based Benchmark Study](https://aclanthology.org/2025.emnlp-main.1556.pdf)
