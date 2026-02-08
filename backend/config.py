"""
Configuration for HuggingFace Inference Providers RAG System
"""
import os
from dataclasses import dataclass

@dataclass
class Config:
    """Cloud RAG system configuration."""
    
    # HuggingFace Token - REQUIRED
    HF_TOKEN: str = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACE_TOKEN") or ""
    
    # Model Selection
    LLM_MODEL: str = "moonshotai/Kimi-K2-Instruct:novita"
    EMBEDDING_MODEL: str = "BAAI/bge-large-en-v1.5"
    
    # Generation Parameters
    MAX_TOKENS: int = 512
    TEMPERATURE: float = 0.7
    
    # Vector Database
    VECTOR_DB_DIR: str = "./data/chroma"
    COLLECTION_NAME: str = "rag_knowledge"
    TOP_K_RESULTS: int = 4
    
    # Document Processing
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200

def get_config() -> Config:
    """Get system configuration."""
    config = Config()
    
    if not config.HF_TOKEN:
        print("\n" + "="*70)
        print("⚠️  WARNING: No HuggingFace token found!")
        print("="*70)
        print("\n📋 To fix this:")
        print("1. Get token from: https://huggingface.co/settings/tokens")
        print("2. Create 'Fine-grained' token with 'Inference Providers' permission")
        print("3. Set environment variable:")
        print("   export HF_TOKEN='your_token_here'")
        print("="*70 + "\n")
    
    return config