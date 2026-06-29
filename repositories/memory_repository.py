class MemoryRepository:

    def __init__(self):

        self.items = []

    def save(self, item):

        self.items.append(item)

    def latest(self, limit=20):

        return self.items[-limit:]
