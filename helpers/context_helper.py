class ContextHelper:

    @staticmethod
    def merge(*contexts):

        return "\n".join(
            str(c)
            for c in contexts
        )
