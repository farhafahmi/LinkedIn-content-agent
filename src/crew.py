import yaml
from pathlib import Path
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool
from src.tools.custom_tool import MyCustomTool

# Load configuration files
config_dir = Path(__file__).parent / "config"

with open(config_dir / "agents.yaml", "r") as f:
    agents_config = yaml.safe_load(f)

with open(config_dir / "tasks.yaml", "r") as f:
    tasks_config = yaml.safe_load(f)

class LinkedInContentCrew:
    def __init__(self):
        self.research_tool = SerperDevTool()

    def run(self, industry, topic):
        researcher = Agent(
            config=agents_config['linkedin_researcher'],
            tools=[self.research_tool],
            verbose=True
        )

        creator = Agent(
            config=agents_config['linkedin_creator'],
            verbose=True
        )

        research_task = Task(
            config=tasks_config['trend_research_task'],
            agent=researcher
        )

        content_task = Task(
            config=tasks_config['content_creation_task'],
            agent=creator,
            context=[research_task],
            output_file="output/linkedin_posts.md"
        )

        crew = Crew(
            agents=[researcher, creator],
            tasks=[research_task, content_task],
            verbose=True,
            process=Process.sequential
        )

        return crew.kickoff(inputs={'industry': industry, 'topic': topic})
