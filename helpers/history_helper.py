class HistoryHelper:

    @staticmethod
    def latest(
        history,
        limit=10,
    ):

        return history[-limit:]
