from abc import ABC


class BasePlugin(ABC):

    name = "plugin"

    async def startup(self):
        pass

    async def shutdown(self):
        pass
