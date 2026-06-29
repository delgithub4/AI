class MemoryManager:

    def __init__(self):
        self.memory = []

    def add(self, message):

        self.memory.append(message)

    def history(self):

        return self.memory

    def clear(self):

        self.memory.clear()

    def latest(self, count=10):

        return self.memory[-count:]
