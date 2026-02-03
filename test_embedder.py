from src.embedder import TextEmbedder

texts = [
    "Machine learning is powerful",
    "Python is used in AI"
]

embedder = TextEmbedder()
vectors = embedder.embed_texts(texts)

print("Vector shape:", vectors.shape)
