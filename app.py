from src.search_engine import SemanticSearchEngine


def load_documents():
    with open("data/documents.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


if __name__ == "__main__":
    documents = load_documents()

    print("Loading documents and generating embeddings...\n")

    search_engine = SemanticSearchEngine(documents)

    print("Semantic Search Ready 🚀")

    while True:
        query = input("\nEnter your query (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        results = search_engine.search(query)

        print("\nTop Results:")
        for r in results:
            print(f"- {r['text']}  (score: {r['score']:.4f})")
