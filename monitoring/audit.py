class AuditLogger:

    def __init__(self):

        self.logs = []

    def record(
        self,
        action,
        actor,
    ):

        self.logs.append(
            {
                "action": action,
                "actor": actor,
            }
        )

    def history(self):

        return self.logs
