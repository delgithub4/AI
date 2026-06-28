from fastapi import FastAPI

from core.config import settings
from core.lifespan import lifespan

from routes.ai import router as ai_router
from routes.health import router as health_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(ai_router)
app.include_router(health_router)


@app.get("/", tags=["Root"])
def home():

    return {
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "running",
    }
