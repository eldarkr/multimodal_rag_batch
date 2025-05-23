# Multimodal RAG System (Text + Image)

<img src="other/demo2.gif" alt="demo" style="width: 100%;" />


### Tools & Technologies
 - Multimodal embedding model (CLIP-ViT-B-32)
 - ChromaDB
 - OpenAI API (gpt-4o-mini)
 - LangChain

### Simplified Architecture

![alt text](other/architecture.png)

### Prerequisites

 - Python 3.13
 - OpenAI API key
 - [uv](https://docs.astral.sh/uv/) package manager
 - Required Python packages ([pyproject.toml](https://github.com/eldarkr/multimodal_rag_batch/blob/master/pyproject.toml))
 - Docker (optional)

### Project Structure

```
multimodal_rag_batch/
├── 📄 pyproject.toml                 # Project dependencies
├── 📄 .env                           # Environment variables
├── 📄 main.py                        # Streamlit application entry point
│
├── 📁 src/
│   ├── 📁 rag/
│   │   ├── 📄 context.py             # Building a context for LLM
│   │   ├── 📄 vector_store.py        # Functions to work with vector store
│   │   └── 📄 openai_chain.py        # Response generation
│   │
│   ├── 📁 index/
│   │   ├── 📄 index_documents.py     # Document indexing and loading to vector DB
│   │   └── 📄 data_loader.py         # Data loading utilities
│   │
│   ├── 📁 embeddings/
│   │   └── 📄 embedder.py            # Multimodal embedding models
│   │
│   └── 📁 utils/
│       └── 📄 config.py              # Configuration management
│
├── 📁 data/                          # Data storage directory
│   ├── 📁 articles/
│   ├── 📁 images/
│   └── 📄 parse_news.ipynb           # Downloading and preprocessing news data
│
├── 📁 index_store/                   # Vector database storage
└── 📁 other/                         # Additional resources
```

---

### Installation

1. **Clone the repository**
    ```bash
    git clone <repository-url>
    cd multimodal_rag_batch
    ```

2. **Install dependencies (for UNIX-like OS)**
    ```bash
    uv venv
    source .venv/bin/activate
    uv sync
    ```

3. **Set up environment variables**
    Create a `.env` file with your API key:
    ```bash
    OPENAI_API_KEY=your_api_key
    ```

### How to Run

Make sure the `data/` folder contains news articles and related images. 
If not, you can use `data/parse_news.ipynb` to download them.

 - **Without Docker**

    1. Launch the app:
        ```bash
        streamlit run main.py
        ```
    
    2. If embeddings are not preloaded, click the **`Load and index data`** button.

    3. Enjoy!

 - **With Docker**

    1. Run command:
        ```bash
        docker build -t your_image_name .
        docker run -p 8501:8501 your_image_name
        ```
    
    2. Open the link provided in the terminal.

---

### System Design Explanation

#### 1. Data Ingestion
- News articles and images are downloaded and preprocessed via `parse_news.ipynb`. 
All process and explanaition described in that file.
- Only **Weekly Issues** are used to keep the dataset small and consistent for testing.

#### 2. Embedding
- Used `RecursiveCharacterTextSplitter` to break documents into chunks.
- Each text chunk and its related image are embedded using **CLIP-ViT-B-32**.
- **Why?**
  - Multimodal
  - Lightweight
  - Developed by OpenAI and compatible with LangChain

#### 3. Vector Store
- I use **ChromaDB** to store embeddings.
- **Why?**
  - It is lightweight and easy to set up
  - Has native support in LangChain

#### 4. Retrieval
- The system embeds the question using CLIP.
- Retrieves the most relevant 4 text chunks and 2 images via **cosine similarity** from ChromaDB.

#### 5. Response Generation
- Retrieved chunks are compiled into a prompt.
- Prompt is sent to **GPT-4o-mini** via LangChain for answer generation.
- **Why?**
  - Lower latency and cost
  - Good for testing and QA tasks

#### 6. Frontend
- Built with **Streamlit**, allowing:
  - Query input
  - Contextual output display
  - Display images
- **Why?**
  - Fast prototyping for ML apps, beautiful UI.

### Future Improvements
- **Add automated evaluation of RAG performance using RAGAS**
- Replace `print` with structured logging
- Improve document chunking strategy
- Avoid redundant computation by caching
- Improve image understanding by OCR or generating image description using APIs (for example gpt-4o)
- For better UX, add progress bar and etc
