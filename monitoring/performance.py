import time


class PerformanceMonitor:

    def measure(self, func):

        async def wrapper(*args, **kwargs):

            start = time.perf_counter()

            result = await func(
                *args,
                **kwargs,
            )

            elapsed = time.perf_counter() - start

            return {
                "elapsed": elapsed,
                "result": result,
            }

        return wrapper
