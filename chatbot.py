from learning import learn
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

        save_message(question, answer)

        return answer

    print("\nAI: I don't know the answer to that.")

    choice = input("Would you like to teach me? (yes/no): ").lower()

    if choice == "yes":

        new_answer = input("Type the correct answer: ")

        learn(question, new_answer)

        self.knowledge[question] = new_answer

        save_message(question, new_answer)

        return "Thank you! I've learned something new."

    return "Okay! Maybe next time."
