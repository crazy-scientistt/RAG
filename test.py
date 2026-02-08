"""
API-driven RAG System Entry Point
Processes uploaded documents and handles queries via API
"""
from rag_system import CloudRAG
from typing import Optional

class RAGAPIHandler:
    """API-driven handler for RAG system operations"""
    
    def __init__(self):
        """Initialize RAG system for API usage"""
        self.rag = CloudRAG()
    
    def process_uploaded_document(self, file_path: str, doc_type: Optional[str] = None) -> dict:
        """Process an uploaded document from web request"""
        try:
            self.rag.ingest_document(doc_type, file_path)
            return {
                "status": "success",
                "message": f"Document processed successfully",
                "documents_count": self.rag.vector_store.count()
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    def answer_question(self, question: str) -> dict:
        """Process a question from web request"""
        try:
            return self.rag.ask(question)
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    def get_system_stats(self) -> dict:
        """Get current system statistics"""
        return self.rag.get_stats()
    
    def clear_all_documents(self):
        """Clear the knowledge base"""
        self.rag.clear_knowledge_base()

if __name__ == "__main__":
    handler = RAGAPIHandler()
    print("RAG API Handler ready for web requests")