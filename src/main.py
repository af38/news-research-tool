import os
import pickle
import time
import streamlit as st
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.agents import create_agent
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv() #load varaibles from .env

st.title("News Research Tool")
st.sidebar.title("News Aticles URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"{i + 1}")
    print(url)
    urls.append(url)

process_button_clicked = st.sidebar.button("Preocess URLs")

file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()

query = st.text_input("Enter your question:")

if (process_button_clicked):
    # start timing
    start_time = time.time()

    # filter out empty URLs
    valid_urls = [url for url in urls if url and url.strip()]

    if not valid_urls:
        st.error("Please enter at least one valid URL")
    else:
        st.write(f"Loading {len(valid_urls)} URLs...")

        # Fast async loader
        loader = AsyncHtmlLoader(
            valid_urls,
            verify_ssl=False,
            requests_per_second=2
        )
        main_placeholder.text("Data Loading...Started...✅✅✅")
        data = loader.load()
        st.write(f"✅ Downloaded {len(data)} pages in {time.time() - start_time:.2f} seconds")

        # 2. Convert HTML to plain text
        main_placeholder.text("Converting HTML to text... ⏳")
        html2text = Html2TextTransformer()
        docs_transformed = html2text.transform_documents(data)

        # 3. Split text
        main_placeholder.text("Splitting text... ⏳")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=['\n\n', '\n', '.', '!', '?', ',', ' ', '']
        )

        # split all documents
        all_splits = text_splitter.split_documents(docs_transformed)
        st.write(f"✅ Created {len(all_splits)} text chunks")

        # 4. Create embeddings
        main_placeholder.text("Creating embeddings... ⏳")
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )

        # Test the embedding model first
        try:
            test_embedding = embeddings.embed_query("Test query")
            st.write(f"✅ Embedding model works (vector size: {len(test_embedding)})")
        except Exception as e:
            st.error(f"Embedding model error: {e}")
            st.stop()

        # Create vector store
        vectorstore = FAISS.from_documents(documents=all_splits, embedding=embeddings)
        main_placeholder.text("Embedding Vector Started Building...✅✅✅")

        # Save the vector store
        with open(file_path, 'wb') as f:
            pickle.dump(vectorstore, f)

        llm = ChatGroq(
            model="openai/gpt-oss-20b",
            temperature=0.7,
            max_tokens=1000
        )

        @tool(response_format="content_and_artifact")
        def retrieve_context(query: str):
            """Retrieve information to help answer a query."""
            retrieved_docs = vectorstore.similarity_search(query, k=2)
            serialized = "\n\n".join(
                (f"Source: {doc.metadata}\nContent: {doc.page_content}")
                for doc in retrieved_docs
            )
            return serialized, retrieved_docs

        from langchain.messages import SystemMessage
        # Create prompt template
        prompt = SystemMessage(content="""You are a news research assistant. Use the provided context to answer questions about news articles.

            Instructions:
            1. Answer based ONLY on the provided context
            2. If the answer isn't in the context, say "I don't have enough information"
            3. Be concise but comprehensive
            4. Cite which document(s) you're using for your answer")""")

        # Query processing
        from langchain.messages import AIMessage
        if query:
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    loader_vectorestore = pickle.load(f)
                agent = create_agent(llm, tools=[retrieve_context], system_prompt=prompt)
                with st.spinner("Generating answer..."):
                    result = agent.invoke({"messages": [{"role": "user", "content": query}]})
                    last_ai_message = next(
                        msg for msg in reversed(result["messages"])
                        if isinstance(msg, AIMessage)
                    )
                    st.subheader("🤖 AI Answer:")
                    st.write(last_ai_message.content)
                    main_placeholder.text(f"✅ Processing complete! Total time: {time.time() - start_time:.2f} seconds")