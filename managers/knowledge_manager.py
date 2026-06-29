class KnowledgeManager:

    def __init__(self):

        self.documents = []

    def add(self, document):

        self.documents.append(document)

    def search(self, query):

        return [
            d
            for d in self.documents
            if query.lower() in str(d).lower()
        ]

    def all(self):

        return self.documents
