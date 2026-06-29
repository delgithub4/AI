from providers.provider_factory import ProviderFactory


class ModelManager:

    def __init__(self):
        self.provider = ProviderFactory.llm()

    def current_model(self):
        return self.provider.model

    def change_model(self, model: str):
        self.provider.change_model(model)

    def available_models(self):
        return [
            "gpt",
            "llama",
            "mistral",
            "deepseek",
        ]
