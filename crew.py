from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import DirectorySearchTool, FileReadTool, SerperDevTool
from typing import List
import os
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ConsultingAgentCrew():
    """Consulting Agent Crew - DeepAgent-grade consulting system"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    # Property to get knowledge directory path
    @property
    def company_knowledge_path(self) -> str:
        """Get the knowledge directory path (relative to project root)"""
        return os.path.join(os.path.dirname(__file__), 'knowledge')
    
    # Property to get RAG tools (lazy initialization)
    @property
    def company_kb_search(self) -> DirectorySearchTool:
        """Directory search tool for company knowledge base"""
        return DirectorySearchTool(
            directory=self.company_knowledge_path,
            description="Search through company knowledge base including company overview, strategy documents, capabilities, and internal documentation. Use this to find information about the company's mission, values, strategic priorities, capabilities, financials, and organizational structure."
        )
    
    @property
    def file_reader(self) -> FileReadTool:
        """File reader tool for company knowledge base"""
        return FileReadTool(
            description="Read specific files from the company knowledge base. Use this when you need to read a specific document in detail."
        )
    
    @property
    def web_search(self) -> SerperDevTool:
        """Web search tool for finding external information when company documents lack context"""
        return SerperDevTool(
            description="Search the web for current information, industry data, market trends, competitor information, or any external information when company knowledge base documents don't provide sufficient context. Always try company documents first, but use this tool when you need more current, comprehensive, or external information to complete your analysis."
        )

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def project_orchestration_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['project_orchestration_agent'], # type: ignore[index]
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]  # RAG tools for company docs + web search fallback
        )

    @agent
    def research_intelligence_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['research_intelligence_agent'], # type: ignore[index]
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]  # RAG tools to search company info + web search fallback
        )

    @agent
    def data_analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['data_analysis_agent'], # type: ignore[index]
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]  # RAG tools for company data context + web search fallback
        )

    @agent
    def strategic_framework_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['strategic_framework_agent'], # type: ignore[index]
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]  # RAG tools for strategic context + web search fallback
        )

    @agent
    def interview_synthesis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['interview_synthesis_agent'], # type: ignore[index]
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]  # RAG tools for organizational context + web search fallback
        )

    @agent
    def recommendation_engine_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['recommendation_engine_agent'], # type: ignore[index]
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]  # RAG tools to ensure recommendations align with company + web search fallback
        )

    @agent
    def document_production_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['document_production_agent'], # type: ignore[index]
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]  # RAG tools to ensure brand consistency + web search fallback
        )

    @agent
    def quality_control_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_control_agent'], # type: ignore[index]
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]  # RAG tools for quality control + web search fallback
        )

    # ============================================================================
    # PHASE-BASED TASKS (DeepAgent-Grade Consulting System)
    # ============================================================================
    
    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    
    # Phase 0: Engagement Framing
    @task
    def phase_0_engagement_framing_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_0_engagement_framing_task'], # type: ignore[index]
            output_file='phase_0_engagement_framing.md'
        )

    # Phase 1: Hypothesis-Driven Discovery (Parallel)
    @task
    def phase_1_research_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_1_research_intelligence_task'], # type: ignore[index]
            output_file='phase_1_research_intelligence_report.md'
        )

    @task
    def phase_1_data_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_1_data_analysis_task'], # type: ignore[index]
            output_file='phase_1_data_analysis_report.md'
        )

    @task
    def phase_1_interview_synthesis_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_1_interview_synthesis_task'], # type: ignore[index]
            output_file='phase_1_interview_synthesis_report.md'
        )

    # Phase 2: Synthesis & Pushback
    @task
    def phase_2_synthesis_pushback_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_2_synthesis_pushback_task'], # type: ignore[index]
            output_file='phase_2_synthesis_pushback_report.md'
        )

    @task
    def phase_2_quality_gate_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_2_quality_gate_task'], # type: ignore[index]
            output_file='phase_2_quality_gate_decision.md'
        )

    # Phase 3: Strategy Design & Option Testing
    @task
    def phase_3_strategy_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_3_strategy_design_task'], # type: ignore[index]
            output_file='phase_3_strategy_design_report.md'
        )

    @task
    def phase_3_data_modeling_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_3_data_modeling_task'], # type: ignore[index]
            output_file='phase_3_data_modeling_report.md'
        )

    # Phase 4: Recommendation Pressure-Test
    @task
    def phase_4_pressure_test_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_4_pressure_test_task'], # type: ignore[index]
            output_file='phase_4_pressure_test_report.md'
        )

    # Phase 5: Narrative & Decision Packaging
    @task
    def phase_5_document_production_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_5_document_production_task'], # type: ignore[index]
            output_file='phase_5_consulting_deliverables.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Consulting Agent Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # Note: Knowledge is accessed via RAG tools (DirectorySearchTool, FileReadTool) on each agent
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
