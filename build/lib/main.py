from crew import LinkedInContentCrew  # Direct import since crew.py is in root

def run():
    inputs = {
        'industry': 'Artificial Intelligence',
        'topic': 'AI Agents'
    }
    crew = LinkedInContentCrew()
    result = crew.run(inputs['industry'], inputs['topic'])
    print(result)

if __name__ == "__main__":
    run()