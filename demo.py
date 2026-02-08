"""
Interactive Demo - Cloud RAG System
Chat with your documents using HuggingFace Inference Providers
"""
from rag_system import CloudRAG
import os

def print_header():
    """Print demo header."""
    print("\n" + "="*70)
    print("🌐 CLOUD RAG SYSTEM - Interactive Demo")
    print("="*70)
    print("\nCommands:")
    print("  add <filepath>  - Add a document to knowledge base")
    print("  ask <question>  - Ask a question")
    print("  stats           - Show system statistics")
    print("  clear           - Clear knowledge base")
    print("  quit            - Exit")
    print("="*70 + "\n")

def main():
    """Run interactive demo."""
    try:
        # Initialize system
        rag = CloudRAG()
        
        print_header()
        
        while True:
            try:
                # Get user input
                user_input = input("📝 Command: ").strip()
                
                if not user_input:
                    continue
                
                # Parse command
                parts = user_input.split(maxsplit=1)
                command = parts[0].lower()
                args = parts[1] if len(parts) > 1 else ""
                
                # Handle commands
                if command == "quit" or command == "exit":
                    print("\n👋 Goodbye!\n")
                    break
                
                elif command == "add":
                    if not args:
                        print("❌ Usage: add <filepath>\n")
                        continue
                    
                    if not os.path.exists(args):
                        print(f"❌ File not found: {args}\n")
                        continue
                    
                    rag.add_document(args)
                
                elif command == "ask":
                    if not args:
                        print("❌ Usage: ask <question>\n")
                        continue
                    
                    result = rag.query(args)
                    
                    print("\n" + "="*70)
                    print("💡 ANSWER")
                    print("="*70)
                    print(result["response"])
                    print("="*70)
                    
                    if result["sources"]:
                        print(f"\n📚 Used {result['num_sources']} source(s):")
                        for i, source in enumerate(result["sources"], 1):
                            print(f"  {i}. {source['source']} (chunk {source['chunk']})")
                    
                    print()
                
                elif command == "stats":
                    stats = rag.get_stats()
                    print("\n" + "="*70)
                    print("📊 SYSTEM STATISTICS")
                    print("="*70)
                    print(f"Model: {stats['model']}")
                    print(f"Embeddings: {stats['embedding_model']}")
                    print(f"Documents: {stats['documents']}")
                    print(f"Chunk size: {stats['chunk_size']}")
                    print(f"Top-K retrieval: {stats['top_k']}")
                    print("="*70 + "\n")
                
                elif command == "clear":
                    confirm = input("⚠️  Clear all documents? (yes/no): ").strip().lower()
                    if confirm == "yes":
                        rag.clear_knowledge_base()
                        print("✅ Knowledge base cleared\n")
                    else:
                        print("❌ Cancelled\n")
                
                else:
                    print(f"❌ Unknown command: {command}")
                    print("Type 'quit' to exit or try: add, ask, stats, clear\n")
            
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!\n")
                break
            
            except Exception as e:
                print(f"\n❌ Error: {str(e)}\n")
    
    except Exception as e:
        print(f"\n❌ Failed to initialize: {str(e)}\n")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
