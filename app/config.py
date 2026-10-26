from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_username: str = "postgres"
    database_password: str = "postgres"
    database_hostname: str = "localhost"
    database_port: str = "5432"
    database_name: str = "url_shortener"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()