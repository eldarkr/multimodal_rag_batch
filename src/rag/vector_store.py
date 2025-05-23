from langchain_chroma import Chroma

from src.utils.config import settings
from src.embeddings.embedder import MultimodalEmbedder

embedder = MultimodalEmbedder()


def get_text_vector_store():
    return Chroma(
        persist_directory=str(settings.TXT_INDEX_DIR),
        collection_name=settings.TXT_COLLECTION_NAME,
        embedding_function=embedder
    )


def get_image_vector_store():
    return Chroma(
        persist_directory=str(settings.IMG_INDEX_DIR),
        collection_name=settings.IMG_COLLECTION_NAME,
        embedding_function=embedder
    )
