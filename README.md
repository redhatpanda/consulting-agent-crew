# Consulting Agent Crew

A DeepAgent-grade consulting system powered by [crewAI](https://crewai.com), designed to deliver MBB-quality strategic consulting through hypothesis-driven analysis, rigorous quality gates, and evidence-backed recommendations.

## Features

- **Hypothesis-Driven Workflow**: All analysis mapped to testable hypotheses
- **Phase-Based Structure**: 5 phases with explicit quality gates
- **Evidence Tagging**: Every finding tagged as supports/weakens/inconclusive
- **Quality Control**: Explicit gates prevent weak recommendations
- **Web Search Integration**: Automatic fallback to web search when company docs lack context
- **Pressure-Testing**: Recommendations tested against hostile scenarios

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management.

First, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
crewai install
```

### Configuration

**Add your API keys into the `.env` file:**
- `OPENAI_API_KEY` - Required for LLM functionality
- `SERPER_API_KEY` - Required for web search (get your key from [serper.dev](https://serper.dev))

**Customize your crew:**
- Modify `config/agents.yaml` to define your agents
- Modify `config/tasks.yaml` to define your tasks
- Modify `crew.py` to add your own logic, tools and specific args
- Modify `main.py` to add custom inputs for your agents and tasks
- Add company knowledge to `knowledge/` directory

## Running the Project

To kickstart your consulting crew, run from the root folder:

```bash
crewai run
```

This initializes the Consulting Agent Crew, assembling agents and executing tasks in the phase-based workflow.

## Project Structure

```
.
├── config/
│   ├── agents.yaml          # Agent definitions
│   └── tasks.yaml           # Phase-based task definitions
├── knowledge/               # Company knowledge base (RAG)
├── tools/                    # Custom tools
├── crew.py                  # Crew definition
├── main.py                  # Entry point
└── pyproject.toml           # Project configuration
```

## Understanding the Crew

The Consulting Agent Crew operates in 5 phases:

1. **Phase 0: Engagement Framing** - Problem statement, hypotheses, success metrics
2. **Phase 1: Hypothesis-Driven Discovery** - Parallel research, data analysis, interviews
3. **Phase 2: Synthesis & Pushback** - Evidence synthesis, hypothesis validation, quality gate
4. **Phase 3: Strategy Design & Option Testing** - Strategic options with financial modeling
5. **Phase 4: Recommendation Pressure-Test** - Rigorous testing against hostile scenarios
6. **Phase 5: Narrative & Decision Packaging** - Hypothesis-led, evidence-backed deliverables

Each phase has explicit gates that can loop back to previous phases if quality standards aren't met.
