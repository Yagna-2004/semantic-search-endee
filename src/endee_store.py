import endee
from src.embedder import TextEmbedder


class EndeeVectorStore:
    def __init__(self, collection_name="documents"):
        self.embedder = TextEmbedder()
        self.collection = endee.Collection(collection_name)

    def load_and_store(self, texts):
        """
        Embed texts and store them in Endee
        """
        embeddings = self.embedder.embed_texts(texts)

        for idx, (text, vector) in enumerate(zip(texts, embeddings)):
            self.collection.add(
                id=str(idx),
                vector=vector.tolist(),
                metadata={"text": text}
            )
