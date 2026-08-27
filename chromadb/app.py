import chromadb
chroma_client = chromadb.Client()

collection_name = "test_collection"
collection = chroma_client.get_or_create_collection(collection_name)

# Define Test Document

documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "How are you today?"},
    {"id": "doc3", "text": "Goodbye, see you later!"},
    {"id": "doc4", "text": "Python is a popular programming language."},
    {"id": "doc5", "text": "Machine learning allows computers to learn from data."},
]

for doc in documents:
    collection.upsert(ids=doc["id"],documents=[doc["text"]])

# define a query
query = "Hello, world!"

result = collection.query(
    query_texts=[query],
    n_results=3 
    )

print(result)