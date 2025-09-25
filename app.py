import streamlit as st
import requests
import chromadb
import ollama
import re
import pandas as pd
import logging
import time
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

SOLR_URL = "http://localhost:8983/solr/main_table/select"  # Generic placeholder
CHROMA_CLIENT = chromadb.Client()
EMBEDDING_FUNCTION = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
COLLECTION_NAME = "schema_collection"

field_mapping = {
    "field_1": "field_1",
    "field_2": "field_2",
    "field_3": "field_3",
    "field_4": "field_4",
    "field_5": "field_5",
}


bilingual_groups = {
    "field_group_1": ("field_1", "field_2"),
    "field_group_2": ("field_3", "field_4"),
}

def setup_chromadb_schema():
    collection = CHROMA_CLIENT.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=EMBEDDING_FUNCTION
    )
    try:
        if collection.count() == 0:
            documents = [f"Column: {friendly}. Field ID: {solr}" for friendly, solr in field_mapping.items()]
            ids = list(field_mapping.keys())
            metadatas = [{"field_name": solr} for solr in field_mapping.values()]
            collection.add(documents=documents, metadatas=metadatas, ids=ids)
            logging.info(" Schema fields indexed successfully in ChromaDB.")
    except Exception as e:
        logging.warning(f" ChromaDB setup warning: {e}")

def call_ollama_for_query(prompt):
    start_time = time.time()
    try:
        resp = ollama.generate(model="mistral", prompt=prompt)
        elapsed = time.time() - start_time
        if isinstance(resp, dict):
            if "response" in resp:
                return resp["response"], elapsed
            if "choices" in resp and resp["choices"]:
                return resp["choices"][0].get("text") or resp["choices"][0].get("content"), elapsed
        return str(resp), elapsed
    except Exception as e:
        logging.error(f" Ollama call failed: {e}")
        return "", 0

setup_chromadb_schema()

st.set_page_config(page_title="Dynamic Query App", layout="wide")
st.title("💡 Dynamic Query App")
st.markdown(
    "Enter a natural language question to query the database. "
    "Supports multiple languages, counts, and faceted group counts."
)

user_question = st.text_input("Your Question:")

# Continue with same logic using `field_mapping` and generic names
# Extract filters, build query, execute Solr, show results...
