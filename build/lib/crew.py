import os
from pathlib import Path
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool
from src.tools.custom_tool import YourCustomTool  # If you have custom tools

config_dir = Path(__file__).parent.parent / "config"

class LinkedInContentCrew:
    def __init__(self):
        self.research_tool = SerperDevTool()
    
    def run(self, industry, topic):
        researcher = Agent(
            config=str(config_dir / "agents.yaml")['linkedin_researcher'],
            tools=[self.research_tool],
            verbose=True
        )
        
        creator = Agent(
            config=str(config_dir / "agents.yaml")['linkedin_creator'],
            verbose=True
        )
        
        research_task = Task(
            config=str(config_dir / "tasks.yaml")['research_task'],
            agent=researcher
        )
        
        content_task = Task(
            config=str(config_dir / "tasks.yaml")['content_task'],
            agent=creator,
            context=[research_task],
            output_file="../output/linkedin_posts.md"
        )
        
        crew = Crew(
            agents=[researcher, creator],
            tasks=[research_task, content_task],
            verbose=2,
            process=Process.sequential
        )
        
        return crew.kickoff(inputs={'industry': industry, 'topic': topic})