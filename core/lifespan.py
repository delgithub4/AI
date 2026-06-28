from contextlib import asynccontextmanager

from core.logging_config import logger


@asynccontextmanager
async def lifespan(app):

    logger.info("Starting service...")

    yield

    logger.info("Service stopped.")
