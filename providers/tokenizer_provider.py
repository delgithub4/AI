class TokenizerProvider:

    def count_tokens(
        self,
        text: str,
    ):

        return len(text.split())

    def truncate(
        self,
        text: str,
        limit: int,
    ):

        return " ".join(
            text.split()[:limit]
        )
