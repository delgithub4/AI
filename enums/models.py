from enum import Enum


class Model(str, Enum):

    GPT = "gpt"

    LLAMA = "llama"

    MISTRAL = "mistral"

    DEEPSEEK = "deepseek"
