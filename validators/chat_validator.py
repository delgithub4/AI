class ChatValidator:

    @staticmethod
    def validate(prompt):

        if not prompt:

            raise ValueError(
                "Prompt is required."
            )

        if len(prompt.strip()) == 0:

            raise ValueError(
                "Prompt cannot be empty."
            )

        return True
