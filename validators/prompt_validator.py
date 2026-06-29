class PromptValidator:

    @staticmethod
    def validate(prompt):

        banned = [
            "",
            None,
        ]

        if prompt in banned:

            raise ValueError(
                "Invalid prompt."
            )

        return True
