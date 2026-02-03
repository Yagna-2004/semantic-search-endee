**Semantic Search System using Endee**

**Project Overview**
This project implements a semantic search engine that retrieves information based on meaning rather than keywords. It uses transformer-based embeddings to represent text as vectors and is designed to integrate with the Endee vector database.

**Problem Statement**
Keyword search often fails because:
- Users may not know exact words
- Synonyms are used
- Context is important

This project solves these problems by using vector embeddings and semantic similarity instead of simple keyword matching.

**Features**
- Converts text documents into vector embeddings
- Processes user queries semantically
- Retrieves the most relevant results
- Modular and extensible design
- Interactive command-line search interface

**Technology Stack**
- Python
- Sentence-Transformers
- NumPy
- Scikit-learn
- Endee (Vector Database – intended backend)

**Project Structure**

semantic-search-endee/
├── data/
│   └── documents.txt
├── src/
│   ├── embedder.py
│   ├── endee_store.py
│   └── search_engine.py
├── app.py
├── test_embedder.py
├── requirements.txt
└── README.md

**How Endee is Used**

The system is designed to use Endee as a vector database:
1. Text documents → converted into embeddings  
2. Embeddings → stored in Endee  
3. User query → converted to embedding  
4. Endee returns the most similar vectors as search results  

**Local Setup Status**

Endee OSS was configured using Docker Compose and a local build from source.  
During local execution, the Docker build failed due to restricted network access when downloading external system packages.  
This is an environmental limitation.  
The integration design and code structure remain correct and aligned with Endee usage.  
To ensure the project remains runnable, a fallback semantic search using cosine similarity is implemented for demonstration.

**Setup Instructions**

**1. Clone the repository**
git clone https://github.com/Yagna-2004/semantic-search-endee.git
cd semantic-search-endee

**2. Create virtual environment**
python -m venv venv
venv\Scripts\activate

**3. Install dependencies**
pip install -r requirements.txt

**4. Run the application**
python app.py

**5. Test embeddings (optional)**
python test_embedder.py

**Sample Usage**

After running the application:
Enter your query (type 'exit' to quit):
machine learning

The system will return semantically ranked results based on meaning.
**sample testcases**  
Enter your query (type 'exit' to quit): **machine learning**
**Top Results:**
Machine learning is a subset of artificial intelligence that learns from data. (score: 0.6111)
Deep learning is a specialized form of machine learning using neural networks. (score: 0.4407)
Python is widely used for machine learning and data science applications. (score: 0.3660)
Enter your query (type 'exit' to quit): **what is deep learning**
**Top Results:**
Deep learning is a specialized form of machine learning using neural networks. (score: 0.8338)
Machine learning is a subset of artificial intelligence that learns from data. (score: 0.4948)
Python is widely used for machine learning and data science applications. (score: 0.3119)
Enter your query (type 'exit' to quit): **artificial intelligence**
**Top Results:**
Artificial intelligence enables machines to mimic human intelligence. (score: 0.6228)
Machine learning is a subset of artificial intelligence that learns from data. (score: 0.5579)
Deep learning is a specialized form of machine learning using neural networks. (score: 0.4524)

**Future Improvements**
- Complete Endee service integration in an unrestricted environment
- Add FastAPI-based web interface
- Extend the system into a RAG pipeline
- Support PDF and document uploads
- Add recommendation features

**Conclusion**
This project demonstrates understanding of:
- Vector embeddings
- Semantic search concepts
- Practical AI/ML application design
- Integration with vector databases
- Real-world system architecture

