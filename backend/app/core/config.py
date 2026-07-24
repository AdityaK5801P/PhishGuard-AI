from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "PhishGuard AI"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = (
        "AI-powered phishing URL detection and analysis platform."
    )

    DATABASE_URL: str = "sqlite:///./phishguard.db"

    class Config:
        env_file = ".env"


settings = Settings()