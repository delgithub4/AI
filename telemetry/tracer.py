import time


class RequestTracer:

    def start(self):

        return time.perf_counter()

    def finish(self, started):

        return time.perf_counter() - started
