import os
import shutil

from langchain_chroma import Chroma

from src.utils.config import settings
from src.index.data_loader import load_documents
from src.embeddings.embedder import MultimodalEmbedder


def build_and_save_index(docs, embedder, collection_name, dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)
    
    Chroma.from_documents(
        documents=docs,
        embedding=embedder,
        collection_name=collection_name,
        persist_directory=str(dir),
    )
    print(f"Index for {collection_name} built and saved to {dir}")


def load_and_index_data():
    """
    Loads text and image documents, generates embeddings for each type using the appropriate
    embedder, and builds persistent Chroma indices.
    """
    
    text_docs, image_docs = load_documents()
    print(f"Loaded {len(text_docs)} text chunks and {len(image_docs)} images")

    build_and_save_index(
        image_docs, 
        MultimodalEmbedder(is_image=True), 
        settings.IMG_COLLECTION_NAME, 
        settings.IMG_INDEX_DIR
    )
    build_and_save_index(
        text_docs, 
        MultimodalEmbedder(), 
        settings.TXT_COLLECTION_NAME, 
        settings.TXT_INDEX_DIR
    )
