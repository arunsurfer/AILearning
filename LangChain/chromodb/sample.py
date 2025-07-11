import chromadb
"""
This script demonstrates basic usage of the ChromaDB library for creating a collection,
adding documents, and querying for similar documents.
Steps performed:
1. Initializes a ChromaDB client.
2. Creates a new collection named "sample_collection".
3. Adds two sample documents to the collection with unique IDs.
4. Queries the collection for documents similar to the text "document", retrieving the top 2 results.
5. Prints the query results, displaying the ID and content of each matched document.
Dependencies:
- chromadb
Usage:
Run the script to see how documents can be stored and queried using ChromaDB.
"""

chromadb_client = chromadb.Client()

collection = chromadb_client.create_collection(name="sample_collection")

collection.add(
    ids=["1", "2"],
    documents=["This is a sample document.", "This is another sample document."]
)

results = collection.query(
    query_texts=["document"], n_results=2
)


print("Query Results:")
print(results)