"""
ChromaDB Vector Store
Stores and retrieves document embeddings
"""
import chromadb
from chromadb.config import Settings
from typing import List, Dict, Any

class VectorStore:
    """ChromaDB vector store for document retrieval."""
    
    def __init__(
        self,
        collection_name: str,
        persist_directory: str,
        embedding_function
    ):
        """
        Initialize ChromaDB vector store.
        
        Args:
            collection_name: Name of the collection
            persist_directory: Directory to persist data
            embedding_function: Function to generate embeddings
        """
        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=Settings(anonymized_telemetry=False)
        )
        
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )
        
        self.embedding_function = embedding_function
        
        print(f"✅ Vector store initialized: {collection_name}")
        print(f"   Documents: {self.collection.count()}")
    
    def add_documents(self, texts: List[str], metadatas: List[Dict[str, Any]]):
        """
        Add documents to the vector store.
        
        Args:
            texts: List of document texts
            metadatas: List of metadata dictionaries
        """
        if not texts:
            return
        
        # Generate embeddings
        embeddings = self.embedding_function.embed_documents(texts)
        
        # Generate IDs
        current_count = self.collection.count()
        ids = [f"doc_{current_count + i}" for i in range(len(texts))]
        
        # Add to collection
        self.collection.add(
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )
        
        print(f"✅ Added {len(texts)} documents to vector store")
    
    def search(self, query: str, top_k: int = 4) -> List[Dict[str, Any]]:
        """
        Search for relevant documents.
        
        Args:
            query: Search query
            top_k: Number of results to return
            
        Returns:
            List of relevant documents with metadata
        """
        # Generate query embedding
        query_embedding = self.embedding_function.embed_query(query)
        
        # Search
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        # Format results
        documents = []
        if results["documents"] and len(results["documents"]) > 0:
            for i, doc in enumerate(results["documents"][0]):
                documents.append({
                    "content": doc,
                    "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                    "distance": results["distances"][0][i] if results["distances"] else 0.0
                })
        
        return documents
    
    def clear(self):
        """Clear all documents from the collection."""
        self.client.delete_collection(self.collection.name)
        self.collection = self.client.get_or_create_collection(
            name=self.collection.name,
            metadata={"hnsw:space": "cosine"}
        )
        print("✅ Vector store cleared")
    
    def count(self) -> int:
        """Get number of documents in store."""
        return self.collection.count()
