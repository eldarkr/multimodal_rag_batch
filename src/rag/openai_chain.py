from langchain.schema import Document
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from src.utils.config import settings

PROMPT = """
    Use the following context to answer the question below in structured markdown.
    You should only use the context provided and NOT make any assumptions or use external sources.
    
    Context:
    {context}

    Question: {question}

    answer in structured markdown:
"""


def generate_structured_answer(question: str, chunks: list[str | Document]) -> str:
    context = "\n\n".join(
        chunk.page_content if isinstance(chunk, Document) else str(chunk)
        for chunk in chunks
    )
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=settings.OPENAI_API_KEY)
    
    prompt = PromptTemplate(
        template=PROMPT,
        input_variables=["context", "question"]
    )
    chain = prompt | llm
    
    return chain.invoke({"context": context, "question": question}).content
