# 📰 News Research Tool

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1%2B-orange)](https://www.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/af38/news-research-tool?style=social)](https://github.com/af38/news-research-tool)

An AI-powered news research tool that lets you load news articles from URLs and ask questions about their content using Retrieval-Augmented Generation (RAG). The tool uses advanced NLP techniques to understand and analyze news content, providing insightful answers with proper citations.

## ✨ Features

### 📥 **Multi-URL Processing**
- Load and analyze multiple news articles simultaneously
- Automatic HTML parsing and text extraction
- Smart chunking for optimal context preservation

### 🤖 **AI-Powered Q&A**
- Natural language question answering
- Context-aware responses using RAG
- Support for multiple Groq LLM models (Mixtral, Llama 3, Gemma)

### 🔍 **Smart Information Retrieval**
- Semantic search using FAISS vector database
- Relevant context extraction from documents
- Configurable similarity search parameters

### 📚 **Transparent Citations**
- Source tracking for every answer
- Expandable document previews
- Confidence scoring for retrieved information

### ⚡ **Performance & Scalability**
- Fast inference with Groq's LPU technology
- Persistent vector storage for repeated use
- Efficient batch processing of multiple articles

### 🎨 **User-Friendly Interface**
- Clean Streamlit-based UI
- Real-time progress indicators
- Interactive chat interface
- One-click sample questions

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | Streamlit | Web interface |
| **Backend** | Python 3.9+ | Core logic |
| **AI Framework** | LangChain | LLM orchestration |
| **Vector Database** | FAISS | Similarity search |
| **Embeddings** | HuggingFace (all-MiniLM-L6-v2) | Text vectorization |
| **LLM Provider** | Groq API | Fast inference |
| **Document Loading** | AsyncHtmlLoader, Html2TextTransformer | Web scraping |
| **Text Processing** | RecursiveCharacterTextSplitter | Document chunking |

## 📋 Prerequisites

Before you begin, ensure you have:

1. **Python 3.9 or higher**
   ```bash
   python --version
    ```
2. **Groq API Key (free at console.groq.com)**
3. **Git (for version control)**

## 🚀 Quick Installation
1. **Clone the Repository**
   ```bash
    git clone https://github.com/yourusername/news-research-tool.git
    cd news-research-tool
    ```

2. **Create Virtual Environment**
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
    ```
    
4. **Set Up Environment Variables**
Create a .env file in the project root:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
    ```

## 🎮 Usage
```bash
streamlit run main.py
```
## 🧪 How It Works
1. **Document Processing Pipeline**
   ```bash
   URLs → HTML Download → Text Extraction → Chunking → Embeddings → FAISS Index
    ```
2. **Query Processing**
   ```bash
   User Question → Embedding → Similarity Search → Context Retrieval → LLM Answer Generation
   ```
3. **RAG Architecture**

The tool implements Retrieval-Augmented Generation (RAG):
- Retrieval: Finds relevant document chunks using FAISS vector similarity
- Augmentation: Combines retrieved chunks with the user's question
- Generation: Uses Groq LLM to generate accurate, context-aware answers

## 📈 Future Enhancements
- Support for PDF and DOCX files
- Batch processing for large article collections
- Multi-language support
- Advanced analytics and visualization
- Topic modeling and trend analysis
- User authentication and saved sessions
- API endpoint for programmatic access
- Integration with news APIs (NewsAPI, GDELT)


## 📄 License
MIT License
