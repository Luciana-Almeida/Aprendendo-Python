from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Store API"
    ROOT_PATH: str = "/"

    DATABASE_URL: str  # Campo obrigatório para a URL do banco de dados

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
