class ModelHelper:

    @staticmethod
    def supports_streaming(model):

        return model in [
            "gpt",
            "llama",
        ]
