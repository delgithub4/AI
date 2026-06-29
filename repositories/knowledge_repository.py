class KnowledgeRepository:

    def __init__(self):

        self.documents = []

    def insert(self, document):

        self.documents.append(document)

    def search(self, keyword):

        return [
            doc
            for doc in self.documents
            if keyword.lower() in str(doc).lower()
        ]

    def all(self):

        return self.documents
