import os
import pydantic_settings
import pydantic


class AppConfig(pydantic_settings.BaseSettings):

    DB_URL: pydantic.PostgresDsn = os.environ.get(
        "DB_URL",
        "postgresql://postgres:postgres@localhost:5432/postgres"
    )


config = AppConfig()
