from abc import ABC, abstractmethod


class EmbeddingInterface(ABC):

    @abstractmethod
    async def embed(
        self,
        text: str,
    ):
        ...
