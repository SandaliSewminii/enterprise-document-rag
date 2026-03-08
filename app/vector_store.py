import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Create or load Chroma DB
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="documents")


def store_chunks(chunks):
    embeddings = embedding_model.encode(chunks).tolist()

    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            embeddings=[embeddings[i]],
            ids=[str(i)]
        )


def retrieve_similar(query, top_k=3):
    query_embedding = embedding_model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    return results["documents"][0]