from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_username: str 
    database_password: str 
    database_hostname: str 
    database_port: str 
    database_name: str 

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()