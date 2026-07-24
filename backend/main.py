from fastapi import FastAPI

from backend.app.core.config import settings
from backend.app.api.home import router as home_router
from backend.app.api.analyze import router as analyze_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
)

app.include_router(home_router)
app.include_router(analyze_router)