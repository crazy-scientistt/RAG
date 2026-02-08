"""
FastAPI backend for Cloud RAG system
"""
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from pathlib import Path
import shutil

from rag_system import CloudRAG

app = FastAPI(title="Cloud RAG API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global RAG instance
rag_instance = None
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    question: str
    response: str
    sources: list
    num_sources: int

@app.on_event("startup")
async def startup_event():
    """Initialize RAG system on startup"""
    global rag_instance
    try:
        rag_instance = CloudRAG()
        print("✅ RAG system initialized")
    except Exception as e:
        print(f"❌ Failed to initialize RAG: {e}")
        raise

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "message": "Cloud RAG API",
        "documents": rag_instance.vector_store.count() if rag_instance else 0
    }

@app.get("/stats")
async def get_stats():
    """Get system statistics"""
    if not rag_instance:
        raise HTTPException(status_code=500, detail="RAG system not initialized")
    return rag_instance.get_stats()

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Upload and process a document"""
    if not rag_instance:
        raise HTTPException(status_code=500, detail="RAG system not initialized")
    
    allowed_extensions = {'.pdf', '.txt', '.docx', '.html', '.htm'}
    file_ext = Path(file.filename).suffix.lower()
    
    if file_ext not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type. Allowed: {', '.join(allowed_extensions)}"
        )
    
    try:
        file_path = UPLOAD_DIR / file.filename
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        rag_instance.add_document(str(file_path))
        
        return {
            "status": "success",
            "message": f"Document '{file.filename}' processed successfully",
            "filename": file.filename,
            "total_documents": rag_instance.vector_store.count()
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing document: {str(e)}")
    finally:
        file.file.close()

@app.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    """Ask a question to the RAG system"""
    if not rag_instance:
        raise HTTPException(status_code=500, detail="RAG system not initialized")
    
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    try:
        result = rag_instance.ask(request.question)
        return QueryResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")

@app.delete("/clear")
async def clear_knowledge_base():
    """Clear all documents from the knowledge base"""
    if not rag_instance:
        raise HTTPException(status_code=500, detail="RAG system not initialized")
    
    try:
        rag_instance.clear_knowledge_base()
        for file in UPLOAD_DIR.glob("*"):
            if file.is_file():
                file.unlink()
        
        return {
            "status": "success",
            "message": "Knowledge base cleared"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error clearing knowledge base: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
