"""
Configuration for HuggingFace Inference Providers RAG System
Cloud-only setup - no local models required
"""
import os
from dataclasses import dataclass

@dataclass
class Config:
    """Cloud RAG system configuration."""
    
    # ==================== HUGGINGFACE INFERENCE PROVIDERS ====================
    # Get your token: https://huggingface.co/settings/tokens
    # Create "Fine-grained" token with "Make calls to Inference Providers" permission
    
    HF_TOKEN: str = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACE_TOKEN") 
    
    # ==================== MODEL SELECTION ====================
    # Using Kimi-K2-Instruct via Novita provider
    # This is a powerful reasoning and instruction-following model from Moonshot AI
    
    LLM_MODEL: str = "moonshotai/Kimi-K2-Instruct:novita"
    
    # Generation parameters
    MAX_TOKENS: int = 512        # Maximum tokens to generate
    TEMPERATURE: float = 0.7     # 0.0 = focused, 1.0 = creative
    
    # ==================== EMBEDDINGS ====================
    # Using BGE-large-en-v1.5 - High quality English embeddings
    # One of the best open-source embedding models for English text
    
    EMBEDDING_MODEL: str = "BAAI/bge-large-en-v1.5"
    
    # ==================== VECTOR DATABASE ====================
    VECTOR_DB_DIR: str = "./data/chroma"
    COLLECTION_NAME: str = "rag_knowledge"
    TOP_K_RESULTS: int = 4       # Number of relevant chunks to retrieve
    
    # ==================== DOCUMENT PROCESSING ====================
    CHUNK_SIZE: int = 1000       # Characters per chunk
    CHUNK_OVERLAP: int = 200     # Overlap between chunks
    
    # ==================== PROVIDER SELECTION GUIDE ====================
    # Suffix options for model selection:
    # - :fastest   → Auto-select provider with highest throughput
    # - :cheapest  → Auto-select provider with lowest cost
    # - :sambanova → Force SambaNova provider
    # - :groq      → Force Groq provider (ultra-fast)
    # - :together  → Force Together AI provider
    # - :fireworks → Force Fireworks provider
    # - :novita    → Force Novita provider (used for Kimi-K2)
    # - (no suffix) → Use your preference order from HuggingFace settings

def get_config() -> Config:
    """Get system configuration."""
    config = Config()
    
    # Validate token
    if not config.HF_TOKEN:
        print("\n" + "="*70)
        print("⚠️  WARNING: No HuggingFace token found!")
        print("="*70)
        print("\n📋 To fix this:")
        print("1. Get token from: https://huggingface.co/settings/tokens")
        print("2. Create 'Fine-grained' token with 'Inference Providers' permission")
        print("3. Set environment variable:")
        print("   export HF_TOKEN='your_token_here'")
        print("\nOr edit this file and set HF_TOKEN directly.\n")
        print("="*70 + "\n")
    
    return config