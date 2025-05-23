import json

from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

from src.utils.config import settings


def load_documents():
    # TODO: experiment with different splitting strategies
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
        separators=[" "],
    )
    
    text_docs = []
    image_docs = []

    with open(settings.ARTICLES_DIR, encoding="utf-8") as f:
        articles = json.load(f)

        for index, article in enumerate(articles, start=1):
            chunks = splitter.split_text(article["body"])
            
            for i, chunk in enumerate(chunks):
                text_docs.append(
                    Document(
                        page_content=chunk,
                        metadata={
                            "chunk_id": i,
                            "article_no": index,
                            "article_url": article.get("link"),
                        },
                    )
                )
            
            for img in article.get("images", []):
                image_docs.append(
                    Document(
                        page_content=img,
                        metadata={
                            "article_url": article.get("link")
                        },
                    )
                )
    
    return text_docs, image_docs
