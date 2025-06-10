# **LinkedIn Content Agent by crewAI**  

🚀 AI-powered LinkedIn content creation made easy – automate high-quality posts with a collaborative crew of AI agents.  


## **Table of Contents**  
1. [Installation](#installation)  
2. [Configuration](#configuration)  
3. [Running the Project](#running-the-project)  
4. [Understanding Your Crew](#understanding-your-crew)  
5. [Support](#support)  


## **Installation**  

### **Prerequisites**  
- Python **>=3.10 <3.13**  
- **[UV](https://github.com/astral-sh/uv)** (for dependency management)  

### **Setup**  
1. Install **UV**:  
   pip install uv
   
2. Install dependencies:  
   crewai install


## **Configuration**  

### **1. Set Up API Keys**  
Add your `OPENAI_API_KEY` to `.env`:  
OPENAI_API_KEY=your-api-key-here

### **2. Customize Agents (`agents.yaml`)**  
Define your AI agents (e.g., **Researcher**, **Writer**, **Editor**) in:  
`src/linkedin_content_agent/config/agents.yaml`  

Example:  
researcher:
  role: "Find trending LinkedIn topics"
  goal: "Deliver data-backed insights for content creation"
  backstory: "An expert in social media trends and SEO."


### **3. Define Tasks (`tasks.yaml`)**  
Set up workflows (e.g., "Write a viral LinkedIn post") in:  
`src/linkedin_content_agent/config/tasks.yaml`  

Example:  
research_task:
  description: "Analyze trending LinkedIn topics in AI"
  agent: "researcher"


### **4. Modify Crew Logic (`crew.py`)**  
Customize agent interactions in:  
`src/linkedin_content_agent/crew.py`  

### **5. Adjust Inputs (`main.py`)**  
Change prompts or inputs in:  
`src/linkedin_content_agent/main.py`  


## **Running the Project**  

Start your AI content team:  
crewai run

**Output:** Generated LinkedIn posts will be saved as `report.md` (or your specified format).  


## **Understanding Your Crew**  

Your agents work together like a content agency:  

| **Agent**      | **Role**                          | **Tools**                |
|----------------|-----------------------------------|--------------------------|
| **Researcher** | Finds viral topics & data         | Web search, SEO analysis |
| **Writer**     | Crafts engaging posts             | GPT-4, storytelling      |
| **Editor**     | Polishes tone & clarity           | Grammar checks           |
| **Strategist** | Optimizes for engagement          | Analytics tools          |


## **Support**  

Need help?  
📖 [Documentation](https://docs.crewai.com)  
🐛 [GitHub Issues](https://github.com/crewAI-examples/LinkedIn-Content-Agent)  
💬 [Discord Community](https://discord.gg/crewai)  


**Let’s automate LinkedIn content like a pro!** ✨  


### **Key Features**  
✅ **Multi-agent collaboration** (research → writing → editing)  
✅ **Customizable workflows** (adjust tasks in YAML)  
✅ **SEO & engagement optimization**  
✅ **Easy deployment** (1 command: `crewai run`)  
