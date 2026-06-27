from difflib import get_close_matches
from learning import learn
from memory import save_message
import json
from utils import clean_text

class AIChatbot:

    def __init__(self):
        with open("data/knowledge.json", "r") as file:
            self.knowledge = json.load(file)

    def find_best_match(self, question):

    questions = self.knowledge.keys()

    match = get_close_matches(
        question,
        questions,
        n=1,
        cutoff=0.6
    )

    if match:
        return match[0]

    return None
            

   def respond(self, question):

    question = clean_text(question)

    if question in self.knowledge:

        answer = self.knowledge[question]
        save_message(question, answer)
        return answer

    best_match = self.find_best_match(question)

    if best_match:

        answer = self.knowledge[best_match]
        save_message(question, answer)
        return answer

    print("\nAI: I don't know the answer.")

    choice = input("Teach me? (yes/no): ").lower()

    if choice == "yes":

        answer = input("Correct answer: ")

        learn(question, answer)

        self.knowledge[question] = answer

        save_message(question, answer)

        return "Thanks! I've learned something new."

    return "No problem."
