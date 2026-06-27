import json

KNOWLEDGE_FILE = "data/knowledge.json"


def learn(question, answer):

    with open(KNOWLEDGE_FILE, "r") as file:
        knowledge = json.load(file)

    knowledge[question] = answer

    with open(KNOWLEDGE_FILE, "w") as file:
        json.dump(knowledge, file, indent=4)
