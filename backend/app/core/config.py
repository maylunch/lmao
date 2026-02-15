from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Global Chinese Portfolio"
    API_V1_STR: str = "/api/v1"

    DB_USER: str = "root"
    DB_PASSWORD: str = "password"
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 3306
    DB_NAME: str = "lmao"

    JWT_SECRET: str = "CHANGE_ME"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_HOURS: int = 2
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    REDIS_URL: str = "redis://127.0.0.1:6379/0"

    PAY_CALLBACK_SECRET: str = "CHANGE_ME"
    PAY_NONCE_TTL_SECONDS: int = 300
    PAY_TIMESTAMP_TOLERANCE_SECONDS: int = 300

    AI_API_URL: str = "https://api.deepseek.com/v1/chat/completions"
    AI_API_KEY: str = "CHANGE_ME"
    AI_MODEL: str = "deepseek-chat"

    MARKET_DATA_URL: str = "https://example.com/market"
    MARKET_FETCH_SYMBOLS: str = "000300.SH"
    MARKET_FETCH_INTERVAL_MINUTES: int = 30

    CELERY_BROKER_URL: str = "redis://127.0.0.1:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://127.0.0.1:6379/2"


settings = Settings()