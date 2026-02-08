"""
Cloud-Only RAG System with HuggingFace Inference Providers
No local models required - everything runs in the cloud
"""
import os
from config import get_config
from llm_provider import HuggingFaceLLM
from embeddings_provider import HuggingFaceEmbeddings
from vector_store import VectorStore
from document_loader import DocumentLoader

class CloudRAG:
    """RAG system using HuggingFace Inference Providers."""
    
    def __init__(self):
        """Initialize the cloud RAG system."""
        print("\n" + "="*70)
        print("🌐 CLOUD RAG SYSTEM - HuggingFace Inference Providers")
        print("="*70 + "\n")
        
        # Load configuration
        self.config = get_config()
        
        if not self.config.HF_TOKEN:
            raise ValueError("HuggingFace token is required! See config.py for setup instructions.")
        
        # Initialize components
        print("Initializing components...\n")
        
        # LLM
        self.llm = HuggingFaceLLM(
            model_name=self.config.LLM_MODEL,
            api_token=self.config.HF_TOKEN,
            max_tokens=self.config.MAX_TOKENS,
            temperature=self.config.TEMPERATURE
        )
        
        # Embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name=self.config.EMBEDDING_MODEL,
            api_token=self.config.HF_TOKEN
        )
        
        # Vector store
        self.vector_store = VectorStore(
            collection_name=self.config.COLLECTION_NAME,
            persist_directory=self.config.VECTOR_DB_DIR,
            embedding_function=self.embeddings
        )
        
        # Document loader
        self.document_loader = DocumentLoader(
            chunk_size=self.config.CHUNK_SIZE,
            chunk_overlap=self.config.CHUNK_OVERLAP
        )
        
        print("\n" + "="*70)
        print("✅ System initialized successfully!")
        print(f"📦 LLM: {self.config.LLM_MODEL}")
        print(f"🔤 Embeddings: {self.config.EMBEDDING_MODEL}")
        print(f"💾 Documents: {self.vector_store.count()}")
        print("="*70 + "\n")
    
    def add_document(self, file_path: str, doc_type: str = None):
        """
        Add a document to the knowledge base.
        
        Args:
            file_path: Path to the document
            doc_type: Type of document (auto-detected if None)
        """
        print(f"\n📄 Loading document: {file_path}")
        
        # Load and chunk document
        chunks = self.document_loader.load_document(file_path, doc_type)
        
        print(f"📑 Created {len(chunks)} chunks")
        
        # Extract texts and metadata
        texts = [chunk["content"] for chunk in chunks]
        metadatas = [chunk["metadata"] for chunk in chunks]
        
        # Add to vector store
        self.vector_store.add_documents(texts, metadatas)
        
        print(f"✅ Document added successfully\n")
    
    def query(self, question: str) -> dict:
        """
        Query the RAG system.
        
        Args:
            question: User question
            
        Returns:
            Dictionary with response and sources
        """
        print(f"\n❓ Question: {question}\n")
        
        # Retrieve relevant documents
        print("🔍 Searching knowledge base...")
        relevant_docs = self.vector_store.search(
            query=question,
            top_k=self.config.TOP_K_RESULTS
        )
        
        if not relevant_docs:
            print("⚠️  No relevant documents found in knowledge base")
            print("💭 Generating response without context...\n")
            
            response = self.llm.generate(question)
            
            return {
                "question": question,
                "response": response,
                "sources": [],
                "num_sources": 0
            }
        
        print(f"📚 Found {len(relevant_docs)} relevant chunks\n")
        
        # Build context from retrieved documents
        context = "\n\n".join([
            f"Source {i+1}:\n{doc['content']}"
            for i, doc in enumerate(relevant_docs)
        ])
        
        # Build prompt
        prompt = f"""Based on the following context, answer the question. If the answer is not in the context, say so.

Context:
{context}

Question: {question}

Answer:"""
        
        # Generate response
        print("💭 Generating response...\n")
        response = self.llm.generate(prompt)
        
        # Format sources
        sources = [
            {
                "source": doc["metadata"].get("source", "Unknown"),
                "chunk": doc["metadata"].get("chunk_index", 0),
                "preview": doc["content"][:200] + "..." if len(doc["content"]) > 200 else doc["content"]
            }
            for doc in relevant_docs
        ]
        
        return {
            "question": question,
            "response": response,
            "sources": sources,
            "num_sources": len(sources)
        }
    
    def ingest_document(self, doc_type: str, file_path: str):
        """
        Ingest a document into the knowledge base.
        
        Args:
            doc_type: Type of document (pdf, txt, docx, html, xlsx)
            file_path: Path to the document
        """
        self.add_document(file_path, doc_type)
    
    def ask(self, question: str) -> dict:
        """
        Ask a question to the RAG system.
        
        Args:
            question: User question
            
        Returns:
            Dictionary with response and sources
        """
        return self.query(question)
    
    def clear_knowledge_base(self):
        """Clear all documents from the knowledge base."""
        self.vector_store.clear()
    
    def get_stats(self) -> dict:
        """Get system statistics."""
        return {
            "model": self.config.LLM_MODEL,
            "embedding_model": self.config.EMBEDDING_MODEL,
            "documents": self.vector_store.count(),
            "chunk_size": self.config.CHUNK_SIZE,
            "top_k": self.config.TOP_K_RESULTS
        }

def main():
    """Example usage."""
    try:
        # Initialize system
        rag = CloudRAG()
        
        # Example: Add documents
        # rag.add_document("path/to/your/document.pdf")
        # rag.add_document("path/to/your/document.txt")
        
        # Example: Query
        # result = rag.query("What is the main topic?")
        # print(f"Answer: {result['response']}\n")
        # print(f"Sources used: {result['num_sources']}")
        
        print("Ready to use! See example usage in the code.\n")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()