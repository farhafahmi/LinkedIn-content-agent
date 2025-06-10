from crew import LinkedInContentCrew

def run():
    crew = LinkedInContentCrew()
    result = crew.run("Artificial Intelligence", "LinkedIn Content Strategy")
    print(result)

if __name__ == "__main__":
    run()
