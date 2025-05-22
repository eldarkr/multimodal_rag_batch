import pathlib
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings class to manage configuration for the application.
    """
    
    DEVICE: str = 'cpu'

    IMG_INDEX_DIR: pathlib.Path = pathlib.Path("index_store/image")
    TXT_INDEX_DIR: pathlib.Path = pathlib.Path("index_store/text")
    ARTICLES_DIR: pathlib.Path = pathlib.Path("data/articles/articles_251_300.json")
    
    IMG_COLLECTION_NAME: str = "image"
    TXT_COLLECTION_NAME: str = "text"

    TXT_EMBED_MODEL: str = "intfloat/e5-base-v2"
    
    IMG_EMBED_MODEL: str = "ViT-B-32-quickgelu"
    IMG_EMBED_CHECKPOINT: str = "openai"
    
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 50
    
    OPENAI_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
