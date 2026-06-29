from managers.context_manager import ContextManager
from managers.knowledge_manager import KnowledgeManager
from managers.memory_manager import MemoryManager
from providers.provider_factory import ProviderFactory


class ConversationManager:

    def __init__(self):

        self.memory = MemoryManager()

        self.knowledge = KnowledgeManager()

        self.context = ContextManager()

        self.llm = ProviderFactory.llm()

    async def chat(
        self,
        prompt,
    ):

        history = self.memory.latest()

        knowledge = self.knowledge.search(prompt)

        context = self.context.build(
            history,
            knowledge,
        )

        response = await self.llm.generate(
            prompt,
            context=context,
        )

        self.memory.add(
            {
                "role": "user",
                "content": prompt,
            }
        )

        self.memory.add(
            {
                "role": "assistant",
                "content": response["response"],
            }
        )

        return response
