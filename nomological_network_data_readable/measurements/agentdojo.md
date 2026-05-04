# AgentDojo
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, AgentDojo is consistently described as an evaluation benchmark that provides a dynamic and stateful environment for testing language model agents. The benchmark is used to measure agent `Safety` and `Adversarial robustness`. Its most common application is testing for agent vulnerabilities, with a specific focus on susceptibility to prompt injection attacks. AgentDojo operationalizes these evaluations through stateful, multi-turn tool-use tasks designed to simulate realistic settings. As one paper specifies, it "consists of 97 tasks across four domains: Workspace, Slack, Travel, and Banking," simulating environments like "email clients, online banking systems, [and] Slack channels." The benchmark is also noted as being studied in relation to `InjecAgent`.

## Sources

**[Mining Complex Patterns of Argumentative Reasoning in Natural Language Dialogue](https://aclanthology.org/2025.acl-long.369.pdf)**
> An evaluation benchmark that provides a dynamic environment for testing agent vulnerabilities, such as susceptibility to prompt injection attacks.

## Relationships

### → AgentDojo
- **Adversarial robustness** (constructs) — *measured_by*
  - [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Security** (constructs) — *measured_by*
  - [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Mining Complex Patterns of Argumentative Reasoning in Natural Language Dialogue](https://aclanthology.org/2025.acl-long.369.pdf)

### Associated with
- **InjecAgent** (measurements)
  - [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf)
