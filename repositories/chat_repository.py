class ChatRepository:

    def __init__(self):

        self.messages = []

    def save(self, message):

        self.messages.append(message)

    def all(self):

        return self.messages

    def clear(self):

        self.messages.clear()
