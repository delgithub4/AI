from providers.embedding_provider import EmbeddingProvider
from providers.llm_provider import LLMProvider
from providers.reranker_provider import RerankerProvider
from providers.tokenizer_provider import TokenizerProvider


class ProviderFactory:

    _instances = {}

    @classmethod
    def llm(cls):

        if "llm" not in cls._instances:
            cls._instances["llm"] = LLMProvider()

        return cls._instances["llm"]

    @classmethod
    def embeddings(cls):

        if "embedding" not in cls._instances:
            cls._instances["embedding"] = EmbeddingProvider()

        return cls._instances["embedding"]

    @classmethod
    def tokenizer(cls):

        if "tokenizer" not in cls._instances:
            cls._instances["tokenizer"] = TokenizerProvider()

        return cls._instances["tokenizer"]

    @classmethod
    def reranker(cls):

        if "reranker" not in cls._instances:
            cls._instances["reranker"] = RerankerProvider()

        return cls._instances["reranker"]
