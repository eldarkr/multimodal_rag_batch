from langchain.embeddings.base import Embeddings
from langchain_experimental.open_clip import OpenCLIPEmbeddings

from src.utils.config import settings


class MultimodalEmbedder(Embeddings):
    def __init__(self, is_image: bool = False):
        self.is_image = is_image
        self.model = OpenCLIPEmbeddings(
            model_name=settings.EMBED_MODEL,
            checkpoint=settings.EMBED_CHECKPOINT,
            device=settings.DEVICE,
        )

    def embed_documents(self, image_paths: list[str]) -> list[list[float]]:
        if not self.is_image:
            return self.model.embed_documents(image_paths)
        
        fixed_paths = ["data/" + path for path in image_paths]  # ???
        return self.model.embed_image(fixed_paths)

    def embed_query(self, text: str) -> list[float]:
        return self.model.embed_query(text)
