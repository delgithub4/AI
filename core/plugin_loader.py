from core.logging_config import logger


class PluginLoader:

    def __init__(self):
        self.plugins = []

    def register(self, plugin):

        self.plugins.append(plugin)

        logger.info(
            "Plugin registered: %s",
            plugin.__class__.__name__,
        )

    async def startup(self):

        for plugin in self.plugins:

            if hasattr(plugin, "startup"):
                await plugin.startup()

    async def shutdown(self):

        for plugin in self.plugins:

            if hasattr(plugin, "shutdown"):
                await plugin.shutdown()


plugin_loader = PluginLoader()
