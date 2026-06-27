import json
from utils import clean_text

class AIChatbot:

    def __init__(self):
        with open("data/knowledge.json", "r") as file:
            self.knowledge = json.load(file)

    def respond(self, question):

        question = clean_text(question)

        if question in self.knowledge:
            return self.knowledge[question]

        return "Sorry, I don't know the answer yet."
