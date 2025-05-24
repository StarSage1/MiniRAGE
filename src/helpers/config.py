from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    File_Uploaded_Types: list
    File_Max_Size: int
    File_Default_Chunk_Size: int
    class Config:
        env_file=".env"

def GetSettings():
    return Settings()
    