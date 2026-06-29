from hashlib import sha256


class EmbeddingProvider:

    async def embed(self, text: str):

        return {
            "embedding_id": sha256(
                text.encode()
            ).hexdigest(),
            "dimensions": 768,
        }
