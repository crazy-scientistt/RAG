"""
HuggingFace Inference Providers - Embeddings Provider
Cloud-based text embeddings
"""
import requests
from typing import List

class HuggingFaceEmbeddings:
    """HuggingFace Inference Providers for text embeddings."""
    
    def __init__(self, model_name: str, api_token: str):
        """
        Initialize HuggingFace embeddings.
        
        Args:
            model_name: Embedding model name
            api_token: HuggingFace API token
        """
        self.model_name = model_name
        # FIXED: Use new router endpoint instead of deprecated api-inference
        self.api_url = f"https://router.huggingface.co/models/{model_name}"
        self.api_token = api_token
        
        # Set embedding dimension based on model
        self.embedding_dim = self._get_embedding_dimension(model_name)
        
        self.headers = {
            "Authorization": f"Bearer {self.api_token}"
        }
        
        print(f"✅ Embeddings initialized: {model_name}")
        print(f"📐 Embedding dimension: {self.embedding_dim}")
    
    def _get_embedding_dimension(self, model_name: str) -> int:
        """Get the embedding dimension for a given model."""
        # Map of common embedding models to their dimensions
        dimension_map = {
            "sentence-transformers/all-MiniLM-L6-v2": 384,
            "BAAI/bge-small-en-v1.5": 384,
            "BAAI/bge-base-en-v1.5": 768,
            "BAAI/bge-large-en-v1.5": 1024,  # BGE-large has 1024 dimensions
            "sentence-transformers/all-mpnet-base-v2": 768,
        }
        return dimension_map.get(model_name, 768)  # Default to 768 if unknown
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for multiple documents.
        
        Args:
            texts: List of text documents
            
        Returns:
            List of embedding vectors
        """
        embeddings = []
        for text in texts:
            embedding = self.embed_query(text)
            embeddings.append(embedding)
        return embeddings
    
    def embed_query(self, text: str) -> List[float]:
        """
        Generate embedding for a single query.
        
        Args:
            text: Query text
            
        Returns:
            Embedding vector
        """
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json={"inputs": text},
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                
                # Handle different response formats
                if isinstance(result, list):
                    if len(result) > 0 and isinstance(result[0], list):
                        return result[0]  # Nested list format
                    return result  # Direct list format
                
                return []
            
            elif response.status_code == 503:
                # Model is loading, wait and retry once
                import time
                print("⏳ Model loading, waiting 20 seconds...")
                time.sleep(20)
                
                response = requests.post(
                    self.api_url,
                    headers=self.headers,
                    json={"inputs": text},
                    timeout=30
                )
                
                if response.status_code == 200:
                    result = response.json()
                    if isinstance(result, list):
                        if len(result) > 0 and isinstance(result[0], list):
                            return result[0]
                        return result
                
                raise Exception("Model still loading after retry")
            
            else:
                raise Exception(f"API Error ({response.status_code}): {response.text}")
        
        except Exception as e:
            print(f"❌ Embedding error: {str(e)}")
            # FIXED: Return a zero vector with correct dimension for the model
            return [0.0] * self.embedding_dim
    
    def __call__(self, text: str) -> List[float]:
        """Allow calling instance directly."""
        return self.embed_query(text)