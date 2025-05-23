import os
import time
import streamlit as st
from src.rag.openai_chain import generate_structured_answer


@st.cache_resource
def get_text_vector_store():
    from src.rag.vector_store import get_text_vector_store
    return get_text_vector_store()


@st.cache_resource  # ???
def get_image_vector_store():
    from src.rag.vector_store import get_image_vector_store
    return get_image_vector_store()


@st.cache_resource
def load_and_index_data():
    from src.index.index_documents import load_and_index_data
    load_and_index_data()


def get_relevant_images(question, img_vs):
    result = img_vs.similarity_search(question, k=2)
    images = [doc for doc in result]
    return images


def get_relevant_texts_and_sources(question, txt_vs):
    from src.rag.context import create_context
    return create_context(question, txt_vs)


def main():
    if st.button("Load and index data"):
        load_and_index_data()
        st.success("✅ Data indexed!")

    question = st.text_input("Enter your question:")
    
    if question:
        txt_vs = get_text_vector_store()
        
        start_time = time.time()
        with st.spinner("🔍 Searching relevant chunks..."):
            blocks, sources_md = get_relevant_texts_and_sources(question, txt_vs)
        elapsed_time = time.time() - start_time
    
        st.success(f"✅ Retrieved {len(blocks)} chunks in {elapsed_time:.2f} seconds.")
        
        with st.spinner("📝 Generating structured answer..."):
            answer = generate_structured_answer(question, blocks)
        st.markdown(answer)

        img_vs = get_image_vector_store()
        images = get_relevant_images(question, img_vs)
        st.write("### Related Images")
        for image in images:
            image_path = f"data/{image.page_content}"
            
            if os.path.exists(image_path):
                st.image(image_path, use_container_width=True)
            else:
                st.warning(f"Image not found: {image_path}")
                
        st.write("### Sources")
        st.markdown(sources_md)
    

if __name__ == "__main__":
    main()
