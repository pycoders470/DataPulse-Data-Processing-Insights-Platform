import os


class Settings:

    PROJECT_NAME: str = "DataPulse"

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://user:password@localhost/datapulse"
    )

    REDIS_URL: str = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379"
    )

    SECRET_KEY: str = os.getenv(
        "SECRET_KEY",
        "change_me"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
    )

    UPLOAD_DIR: str = os.getenv(
        "UPLOAD_DIR",
        "data/uploads"
    )


settings = Settings()