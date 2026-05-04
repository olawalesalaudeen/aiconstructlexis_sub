# Red-teaming
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** Red teaming evaluation, Red teaming  

## State of the Field

Across the provided literature, red-teaming is most commonly characterized as an adversarial testing process designed to find and exploit vulnerabilities in generative AI models. The stated goal of this process is to identify issues such as biases, harmful capabilities, and general safety vulnerabilities. While this broad framing is prevalent, a more specific usage describes red-teaming as a data-generation procedure for producing "harmful examples" intended for model fine-tuning. It is also operationalized as a formal "red teaming evaluation" to assess a model's safeguards, with one study noting its use against "28 test-time adversaries" (On Evaluating the Durability of Safeguards for Open-Weight LLMs). The process can be carried out by a "dedicated team" of human experts or automated systems, and some work discusses the composition of these teams, highlighting the benefits of diversity. Its application is noted in contexts such as "multilingual safety alignment training" (Chart2Code53: A Large-Scale Diverse and Complex Dataset for Enhancing Chart-to-Code Generation).

## Sources

**[Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)**
> A data-generation procedure used to produce harmful examples for fine-tuning the explicitly harmful model.

**[On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf) (as "Red teaming evaluation")**
> An adversarial testing process used to evaluate a model's safeguards, in this case involving 28 test-time adversaries composed of variations of fine-tuning attacks.

**[Position: Generative AI Regulation Can Learn from Social Media Regulation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/appel25a/appel25a.pdf) (as "Red teaming")**
> An adversarial testing process where a dedicated team actively tries to find and exploit vulnerabilities, biases, or harmful capabilities in a generative AI model.
