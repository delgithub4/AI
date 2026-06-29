from core.logging_config import logger
from core.plugin_loader import plugin_loader


async def shutdown():

    logger.info("Stopping AI service...")

    await plugin_loader.shutdown()

    logger.info("AI service stopped.")
