class ModelValidator:

    MODELS = [
        "gpt",
        "llama",
        "mistral",
        "deepseek",
    ]

    @classmethod
    def validate(
        cls,
        model,
    ):

        if model not in cls.MODELS:

            raise ValueError(
                "Unsupported model."
            )

        return True
