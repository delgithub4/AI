from providers.provider_factory import ProviderFactory


class EmbeddingTask:

    async def run(
        self,
        text,
    ):

        provider = ProviderFactory.embeddings()

        return await provider.embed(text)
