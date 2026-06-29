class HistoryTask:

    async def archive(
        self,
        history,
    ):

        return {
            "archived": len(history),
        }
