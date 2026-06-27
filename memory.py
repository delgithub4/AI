import json
import os

MEMORY_FILE = "data/chat_history.json"


def load_history():

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_message(user, ai):

    history = load_history()

    history.append({
        "user": user,
        "assistant": ai
    })

    with open(MEMORY_FILE, "w") as file:
        json.dump(history, file, indent=4)
