from sklearn.metrics.pairwise import cosine_similarity
from src.embedder import TextEmbedder


class SemanticSearchEngine:
    def __init__(self, documents):
        self.embedder = TextEmbedder()
        self.documents = documents
        self.document_vectors = self.embedder.embed_texts(documents)

    def search(self, query, top_k=3):
        query_vector = self.embedder.embed_texts([query])

        similarities = cosine_similarity(
            query_vector,
            self.document_vectors
        )[0]

        ranked_indices = similarities.argsort()[::-1][:top_k]

        results = []
        for idx in ranked_indices:
            results.append({
                "text": self.documents[idx],
                "score": float(similarities[idx])
            })

        return results
