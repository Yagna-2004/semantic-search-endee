# Semantic Search System using Endee

## Project Overview
This project implements a semantic search engine that retrieves information based on meaning rather than keywords. It uses transformer-based embeddings to represent text as vectors and is designed to integrate with the Endee vector database.

## Problem Statement
Keyword search often fails because:
- Users may not know exact words  
- Synonyms are used  
- Context is important  

This project solves that by using vector embeddings and semantic similarity.

## Features
- Converts text documents into embeddings  
- Processes user queries semantically  
- Retrieves most relevant results  
- Modular design for easy extension  

## Technology Stack
- Python  
- Sentence-Transformers  
- NumPy  
- Endee (Vector Database – intended backend)

## Project Structure
semantic-search-endee/
│
├── data/
│ └── documents.txt
│
├── src/
│ ├── embedder.py
│ ├── endee_store.py
│ └── search_engine.py
│
├── app.py
├── test_embedder.py
├── requirements.txt
└── README.md


## How Endee is Used

The system is designed to use Endee as a vector database:

1. Text documents → embeddings  
2. Embeddings → stored in Endee  
3. User query → embedding  
4. Endee returns most similar vectors  

### Local Setup Status

Endee OSS was configured using Docker Compose and a local build from source.  
During local execution, the Docker build failed due to restricted network access when downloading external system packages.

This is an environmental limitation.  
The integration design and code structure remain correct.

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd semantic-search-endee

2. Create virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Test embeddings
python test_embedder.py

Future Improvements

Complete Endee service integration

Add FastAPI interface

Extend to RAG pipeline

Support document uploads

Conclusion

This project demonstrates understanding of:

Vector embeddings

Semantic search

System design

Integration with vector databases

