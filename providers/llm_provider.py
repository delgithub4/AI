from core.logging_config import logger


class LLMProvider:

    def __init__(self):

        self.model = "default"

    async def generate(
        self,
        prompt: str,
        context: str = "",
        temperature: float = 0.7,
    ):

        logger.info(
            "Generating response using %s",
            self.model,
        )

        return {
            "response": "",
            "model": self.model,
            "temperature": temperature,
            "context": context,
        }

    def change_model(self, model: str):

        self.model = model
