from pydantic import BaseSettings

class Settings(BaseSettings):
    url_param: str
    display_name: str
    nginx_server: str

    class Config:
        env_file=".env"

settings = Settings()
