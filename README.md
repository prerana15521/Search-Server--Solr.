# Search Server - Solr

An intelligent, multi-language search engine that combines full-text search, large language model (LLM) query generation, and vector-based schema memory for accurate and efficient retrieval of complex datasets.

## Features

- **Natural Language Query Support**: Accepts queries in multiple languages and automatically generates database queries.
- **Full-Text Search**: Powered by Apache Solr for fast and accurate searches across multiple fields.
- **LLM Integration**: Uses Ollama (Mistral/SQLCoder) to interpret user queries and generate SQL dynamically.
- **Schema Memory**: Vector-based memory (ChromaDB) allows the system to understand table structures and select the most relevant data sources.
- **User-Friendly Interface**: Built with Streamlit for interactive query input and result display.
- **Robust Handling**: Supports synonyms, transliterations, spelling variations, and missing values.
- **Performance Logging**: Tracks query execution, LLM response, and overall processing time for optimization.

## Installation

1. Upload the files to your environment.
2. Install required Python packages:
```bash
pip install -r requirements.txt
```  
3. Set up Apache Solr and configure your core for indexing data.  
4. Run the Streamlit app:
```bash
streamlit run app.py
```  

## Usage

1. Open the web interface.
2. Enter a query in natural language.
3. View dynamic results with highlighted matching data.

## Contributing

Contributions are welcome. Please submit issues or pull requests for improvements.

## License

This project is licensed under the MIT License.
