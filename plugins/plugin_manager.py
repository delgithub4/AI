class PluginManager:

    def __init__(self):

        self.plugins = []

    def register(self, plugin):

        self.plugins.append(plugin)

    async def startup(self):

        for plugin in self.plugins:
            await plugin.startup()

    async def shutdown(self):

        for plugin in self.plugins:
            await plugin.shutdown()
