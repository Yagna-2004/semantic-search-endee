from sentence_transformers import SentenceTransformer


class TextEmbedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts):
        """
        Convert a list of text strings into vector embeddings
        """
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings
