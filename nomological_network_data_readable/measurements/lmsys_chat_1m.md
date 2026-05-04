# LMSYS-chat-1M
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** LMSYS-Chat-1M, LMSys-Chat-1M, LMSys, LmsysChat  

## State of the Field

Across the surveyed literature, LMSYS-chat-1M is consistently characterized as a large-scale, open-access dataset of real-world conversations between users and numerous state-of-the-art language models. Several papers specify it contains one million user-model interactions collected from the Chatbot Arena platform. The prevailing use of this dataset is as a source of authentic user inputs for a range of applications. For instance, papers use its prompts for fine-tuning models, testing classifier generalization with out-of-distribution data, and sampling inputs that "represent real-world use cases" ("Studying Rhetorically Ambiguous Questions"). The dataset is also employed to analyze and evaluate specific model behaviors in practical chat settings, such as assessing "non-adversarial reproduction" of training data or sampling anthropomorphic outputs. A distinct line of work frames the dataset as a tool for capturing human preferences, defining it as a collection of "votes from users comparing outputs from over 20 different LLMs" ("Evaluating Multimodal Language Models as Visual Assistants for Visually Impaired Users") and using it to measure human agreement with LLM judges. Its value in providing "real-world user interactions" is sometimes explicitly contrasted with datasets composed of synthetic data.

## Sources

**[Learning from negative feedback, or positive feedback or both](https://proceedings.iclr.cc/paper_files/paper/2025/file/162f1442c568f639b846a00ddc5edbd4-Paper-Conference.pdf)**
> A large-scale dataset of real-world user prompts and conversations used as a source of inputs for fine-tuning and evaluating chat-oriented language models.

**[Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf) (as "LMSYS-Chat-1M")**
> A large dataset of real-world LLM conversations used here to assess non-adversarial reproduction in practical chat settings.

**[Do Language Models Have Semantics? On the Five Standard Positions](https://aclanthology.org/2025.acl-long.1259.pdf) (as "LMSys-Chat-1M")**
> A dataset of real-world conversations with 25 state-of-the-art LLMs, used to sample anthropomorphic outputs from commercial models.

**[Evaluating Multimodal Language Models as Visual Assistants for Visually Impaired Users](https://aclanthology.org/2025.acl-long.1261.pdf) (as "LMSys")**
> The LMSys Chatbot Arena Conversations Dataset, which captures real-world user preferences by collecting votes from users comparing outputs from over 20 different LLMs.

**[Idiosyncrasies in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25z/sun25z.pdf) (as "LmsysChat")**
> A dataset capturing real-world user interactions, used as a source of out-of-distribution prompts for testing classifier generalization.
