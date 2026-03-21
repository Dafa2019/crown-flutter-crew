"""Crown Flutter Crew v1.0 - Full Lifecycle Flutter Development Team"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class CrownFlutterCrew():
    """Crown Flutter Crew - 1 Manager + 6 Workers, Hierarchical Process"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Manager Agent (not in workers list) ──

    @agent
    def tech_director(self) -> Agent:
        return Agent(
            config=self.agents_config['tech_director'],
            llm="anthropic/claude-opus-4-20250514",
            allow_delegation=True,
            memory=True,
            verbose=True,
            max_iter=25,
        )

    # ── Worker Agents ──

    @agent
    def architect(self) -> Agent:
        return Agent(
            config=self.agents_config['architect'],
            llm="anthropic/claude-sonnet-4-20250514",
            verbose=True,
        )

    @agent
    def coder(self) -> Agent:
        return Agent(
            config=self.agents_config['coder'],
            llm="anthropic/claude-sonnet-4-20250514",
            verbose=True,
        )

    @agent
    def ui_perf_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['ui_perf_expert'],
            llm="anthropic/claude-sonnet-4-20250514",
            verbose=True,
        )

    @agent
    def tester(self) -> Agent:
        return Agent(
            config=self.agents_config['tester'],
            llm="gpt-4o",
            verbose=True,
        )

    @agent
    def cicd_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['cicd_expert'],
            llm="gpt-4o",
            verbose=True,
        )

    @agent
    def security_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['security_expert'],
            llm="gpt-4o",
            verbose=True,
        )

    # ── Tasks ──

    @task
    def architecture_design(self) -> Task:
        return Task(config=self.tasks_config['architecture_design'])

    @task
    def implement_features(self) -> Task:
        return Task(config=self.tasks_config['implement_features'])

    @task
    def optimize_ui_performance(self) -> Task:
        return Task(config=self.tasks_config['optimize_ui_performance'])

    @task
    def security_audit(self) -> Task:
        return Task(config=self.tasks_config['security_audit'])

    @task
    def testing_suite(self) -> Task:
        return Task(config=self.tasks_config['testing_suite'])

    @task
    def deploy_pipeline(self) -> Task:
        return Task(config=self.tasks_config['deploy_pipeline'])

    # ── Crew ──

    @crew
    def crew(self) -> Crew:
        # tech_director is manager, exclude from workers
        workers = [
            a for a in self.agents
            if a.role != self.tech_director().role
        ]
        return Crew(
            agents=workers,
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_agent=self.tech_director(),
            planning=True,
            memory=True,
            verbose=True,
        )
