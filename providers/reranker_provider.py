class RerankerProvider:

    async def rerank(
        self,
        documents,
        query,
    ):

        return sorted(
            documents,
            key=lambda x: x.get(
                "score",
                0,
            ),
            reverse=True,
        )
