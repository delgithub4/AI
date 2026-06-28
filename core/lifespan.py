from contextlib import asynccontextmanager

from core.logging_config import logger


@asynccontextmanager
async def lifespan(app):

    logger.info("======================================")
    logger.info("Starting %s...", app.title)
    logger.info("Application is ready.")
    logger.info("======================================")

    yield

    logger.info("======================================")
    logger.info("Shutting down %s...", app.title)
    logger.info("Application stopped.")
    logger.info("======================================")
