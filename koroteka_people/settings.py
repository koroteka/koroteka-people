from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql:///koroteka_people"


settings = Settings()
