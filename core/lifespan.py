from contextlib import asynccontextmanager

from core.logging_config import logger


@asynccontextmanager
async def lifespan(app):

    logger.info("=" * 60)
    logger.info("Starting %s", app.title)
    logger.info("Environment: %s", app.debug)
    logger.info("Application ready.")
    logger.info("=" * 60)

    yield

    logger.info("=" * 60)
    logger.info("Stopping %s", app.title)
    logger.info("Shutdown complete.")
    logger.info("=" * 60)
