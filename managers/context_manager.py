class ContextManager:

    def build(
        self,
        history,
        knowledge,
    ):

        context = []

        context.extend(history)

        context.extend(knowledge)

        return "\n".join(
            str(item)
            for item in context
        )
