# TODO: research about cohere for improving the context generation

def create_context(question: str, txt_vs):
    """
    Create a prompt context for the given question using the text vector store.
    """
    
    results = txt_vs.similarity_search(question, k=5)

    blocks = []
    seen_urls = set()
    
    for i, doc in enumerate(results):
        url = doc.metadata.get("article_url", "")

        blocks.append(doc.page_content)
        
        if url and url not in seen_urls:
            seen_urls.add(url)
            
    sources_md = "\n".join(f"- [{url}]({url})" for url in seen_urls)

    return blocks, sources_md
