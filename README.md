# Consulting Agent Crew

A DeepAgent-grade consulting system powered by [crewAI](https://crewai.com), designed to deliver MBB-quality strategic consulting through hypothesis-driven analysis, rigorous quality gates, and evidence-backed recommendations.

This system orchestrates 8 specialized consulting agents through a 5-phase workflow to produce enterprise-grade strategic consulting deliverables. Each agent operates with access to company knowledge bases (RAG) and web search capabilities, ensuring recommendations are grounded in both internal context and external market realities.

## Features

- **Hypothesis-Driven Workflow**: All analysis mapped to testable hypotheses with explicit evidence tagging
- **5-Phase Structure**: Sequential phases with explicit quality gates that can loop back if standards aren't met
- **Evidence Tagging**: Every finding tagged as supports/weakens/inconclusive relative to hypotheses
- **Quality Control Gates**: Explicit gates prevent weak recommendations from proceeding
- **RAG + Web Search**: Company knowledge base search with automatic fallback to web search for current market data
- **Pressure-Testing**: Recommendations tested against hostile board scenarios, assumption failures, and execution risks
- **8 Specialized Agents**: Each agent has a specific role (Principal/Partner-level) matching MBB consulting structures

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

**Customize the consulting engagement:**
- Modify `config/agents.yaml` to adjust agent roles, goals, and backstories
- Modify `config/tasks.yaml` to customize phase tasks and requirements
- Modify `crew.py` to add custom tools or modify agent configurations
- Modify `main.py` to change the default client inputs (client_company, strategic_objective, target_market)
- Add company knowledge documents to `knowledge/` directory (company_overview.md, company_strategy.md, company_capabilities.md, etc.)

## Running the Project

To run the consulting crew with default inputs (TechCorp Global example), execute from the root folder:

```bash
crewai run
```

Or run directly with Python:

```bash
python main.py
```

This initializes the Consulting Agent Crew, assembling all 8 agents and executing tasks sequentially through the 5-phase workflow. Each phase produces markdown deliverables that are saved to the project root.

## Project Structure

```
.
├── config/
│   ├── agents.yaml          # 8 agent definitions (roles, goals, backstories)
│   └── tasks.yaml           # 5-phase task definitions with quality gates
├── knowledge/               # Company knowledge base (RAG)
│   ├── company_overview.md  # Company profile, mission, values, structure
│   ├── company_strategy.md  # Strategic priorities and initiatives
│   ├── company_capabilities.md  # Organizational capabilities
│   └── user_preference.txt  # User preferences and context
├── tools/                    # Custom tools
│   └── custom_tool.py       # Additional custom tools (if needed)
├── crew.py                  # Crew class with 8 agents and 11 tasks
├── main.py                  # Entry point with default client inputs
└── pyproject.toml           # Project configuration and dependencies
```

## Understanding the Crew

### The 8 Agents

The Consulting Agent Crew consists of 8 specialized agents, each with Principal or Partner-level expertise:

1. **Project Orchestration Agent** (Engagement Manager) - Coordinates workflow, manages dependencies, tracks deliverables
2. **Research Intelligence Agent** (Principal) - Industry reports, competitive analysis, market intelligence, PESTEL analysis
3. **Data Analysis Agent** (Principal) - Quantitative analysis, financial modeling, statistical analysis, forecasting
4. **Strategic Framework Agent** (Partner) - Applies Porter's Five Forces, SWOT, Value Chain, strategic frameworks
5. **Interview Synthesis Agent** (Principal) - Stakeholder interviews, qualitative synthesis, organizational analysis
6. **Recommendation Engine Agent** (Partner) - Generates strategic recommendations, implementation roadmaps, ROI estimates
7. **Document Production Agent** (Principal) - Creates executive summaries, reports, slide decks, tailored messaging
8. **Quality Control Agent** (Partner) - Enforces quality gates, challenges assumptions, validates evidence quality

All agents have access to:
- **Company Knowledge Base Search** (DirectorySearchTool) - Searches internal company documents
- **File Reader** (FileReadTool) - Reads specific company documents in detail
- **Web Search** (SerperDevTool) - Searches web for current market data when company docs lack context

### The 5-Phase Workflow

The crew operates through a rigorous 5-phase consulting process:

**Phase 0: Engagement Framing**
- Problem statement (root causes, not symptoms)
- Success metrics
- 2-4 testable hypotheses (not solutions)
- Explicit unknowns
- Initial problem structuring (hypothesis/issue tree)
- *Agent: Project Orchestration Agent*
- *Output: `phase_0_engagement_framing.md`*

**Phase 1: Hypothesis-Driven Discovery** (Parallel Work)
Three parallel tasks that test hypotheses:
- **Research Intelligence**: Industry analysis, competitive landscape, market trends, PESTEL
- **Data Analysis**: Financial modeling, quantitative analysis, scenario analysis, benchmarking
- **Interview Synthesis**: Stakeholder interviews, qualitative insights, organizational assessment
- *Agents: Research Intelligence Agent, Data Analysis Agent, Interview Synthesis Agent*
- *Outputs: `phase_1_research_intelligence_report.md`, `phase_1_data_analysis_report.md`, `phase_1_interview_synthesis_report.md`*
- *Critical: Every finding tagged as SUPPORTS/WEAKENS/INCONCLUSIVE for each hypothesis*

**Phase 2: Synthesis & Pushback** (Quality Gate)
- Synthesize all Phase 1 evidence
- Hypothesis validation matrix
- Refined problem framing
- Shortlist of 2-4 strategic options
- Explicit trade-offs
- Framework analysis (Porter's Five Forces, SWOT, Value Chain)
- **Quality Gate Decision**: PROCEED / LOOP BACK / REFRAME
- *Agents: Strategic Framework Agent, Quality Control Agent*
- *Outputs: `phase_2_synthesis_pushback_report.md`, `phase_2_quality_gate_decision.md`*

**Phase 3: Strategy Design & Option Testing**
- Detailed option analysis (Build/Buy/Partner/Hybrid)
- Financial impact (3-5 year projections)
- Execution complexity assessment
- Risk profiles and mitigation
- Organizational readiness evaluation
- Financial modeling and scenario analysis
- *Agents: Recommendation Engine Agent, Data Analysis Agent*
- *Outputs: `phase_3_strategy_design_report.md`, `phase_3_data_modeling_report.md`*

**Phase 4: Recommendation Pressure-Test** (Critical Gate)
- Pressure-test against hostile board scenarios
- Test assumption failures
- Evaluate execution risks
- Assess competitive response
- Validate organizational reality
- **Gate Decision**: PROCEED / REFINE
- *Agent: Quality Control Agent*
- *Output: `phase_4_pressure_test_report.md`*

**Phase 5: Narrative & Decision Packaging**
- Executive Summary (decision-first approach)
- Detailed Strategic Report (hypothesis-led narrative)
- Executive Presentation Deck outline
- Tailored messaging (C-suite vs operational)
- Comprehensive appendices
- *Agent: Document Production Agent*
- *Output: `phase_5_consulting_deliverables.md`*

### Quality Gates

The system includes explicit quality gates that can loop back to previous phases:
- **Phase 2 Gate**: If evidence is weak → loop back to Phase 1; if hypotheses wrong → reframe in Phase 0
- **Phase 4 Gate**: If recommendations fail pressure-test → send back to Phase 3 for refinement

This ensures only defensible, evidence-backed recommendations reach the client.
