class MetricsCollector:

    def __init__(self):

        self.metrics = {}

    def increment(self, key):

        self.metrics[key] = self.metrics.get(
            key,
            0,
        ) + 1

    def snapshot(self):

        return self.metrics.copy()
