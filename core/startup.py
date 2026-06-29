from core.logging_config import logger
from core.plugin_loader import plugin_loader


async def startup():

    logger.info("Initializing AI service...")

    await plugin_loader.startup()

    logger.info("AI service initialized.")
