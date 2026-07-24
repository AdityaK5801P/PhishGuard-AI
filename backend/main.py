from fastapi import FastAPI

from backend.app.api.home import router as home_router
from backend.app.api.analyze import router as analyze_router

app = FastAPI(
    title="PhishGuard AI",
    version="1.0.0",
    description="AI-powered phishing detection API"
)

app.include_router(home_router)
app.include_router(analyze_router)