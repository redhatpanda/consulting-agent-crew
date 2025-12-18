from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import DirectorySearchTool, FileReadTool, SerperDevTool
from typing import List
import os

@CrewBase
class ConsultingAgentCrew():
    """Consulting Agent Crew - DeepAgent-grade consulting system"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    @property
    def company_knowledge_path(self) -> str:
        """Get the knowledge directory path (relative to project root)"""
        return os.path.join(os.path.dirname(__file__), 'knowledge')
    
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

    @agent
    def project_orchestration_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['project_orchestration_agent'],
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]
        )

    @agent
    def research_intelligence_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['research_intelligence_agent'],
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]
        )

    @agent
    def data_analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['data_analysis_agent'],
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]
        )

    @agent
    def strategic_framework_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['strategic_framework_agent'],
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]
        )

    @agent
    def interview_synthesis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['interview_synthesis_agent'],
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]
        )

    @agent
    def recommendation_engine_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['recommendation_engine_agent'],
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]
        )

    @agent
    def document_production_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['document_production_agent'],
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]
        )

    @agent
    def quality_control_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_control_agent'],
            verbose=True,
            tools=[self.company_kb_search, self.file_reader, self.web_search]
        )

    @task
    def phase_0_engagement_framing_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_0_engagement_framing_task'],
            output_file='phase_0_engagement_framing.md'
        )

    @task
    def phase_1_research_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_1_research_intelligence_task'],
            output_file='phase_1_research_intelligence_report.md'
        )

    @task
    def phase_1_data_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_1_data_analysis_task'],
            output_file='phase_1_data_analysis_report.md'
        )

    @task
    def phase_1_interview_synthesis_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_1_interview_synthesis_task'],
            output_file='phase_1_interview_synthesis_report.md'
        )

    @task
    def phase_2_synthesis_pushback_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_2_synthesis_pushback_task'],
            output_file='phase_2_synthesis_pushback_report.md'
        )

    @task
    def phase_2_quality_gate_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_2_quality_gate_task'],
            output_file='phase_2_quality_gate_decision.md'
        )

    @task
    def phase_3_strategy_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_3_strategy_design_task'],
            output_file='phase_3_strategy_design_report.md'
        )

    @task
    def phase_3_data_modeling_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_3_data_modeling_task'],
            output_file='phase_3_data_modeling_report.md'
        )

    @task
    def phase_4_pressure_test_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_4_pressure_test_task'],
            output_file='phase_4_pressure_test_report.md'
        )

    @task
    def phase_5_document_production_task(self) -> Task:
        return Task(
            config=self.tasks_config['phase_5_document_production_task'],
            output_file='phase_5_consulting_deliverables.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Consulting Agent Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
