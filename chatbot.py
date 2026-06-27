from memory import save_message
import json
from utils import clean_text

class AIChatbot:

    def __init__(self):
        with open("data/knowledge.json", "r") as file:
            self.knowledge = json.load(file)

    def respond(self, question):

    question = clean_text(question)

    if question in self.knowledge:
        answer = self.knowledge[question]
    else:

        answer = (
            "I don't know that yet. "
            "I'm still learning."
        )

    save_message(question, answer)

    return answer

        return (
            "I don't know the answer to that yet. "
            "Try asking something else."
        )
