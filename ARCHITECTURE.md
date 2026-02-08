# 🏗️ System Architecture

## Project Structure

```
ragcloud_web/
├── backend/                    # FastAPI backend
│   ├── app.py                 # Main API server
│   ├── config.py              # Configuration
│   ├── rag_system.py          # Core RAG logic
│   ├── document_loader.py     # Document processing
│   ├── embeddings_provider.py # HuggingFace embeddings
│   ├── llm_provider.py        # HuggingFace LLM
│   ├── vector_store.py        # ChromaDB interface
│   ├── requirements.txt       # Python dependencies
│   ├── run.sh / run.bat       # Backend runners
│   └── uploads/               # Uploaded documents
│
├── frontend/                   # Static web app
│   ├── index.html             # Main UI
│   ├── config.js              # API configuration
│   ├── js/
│   │   ├── app.js             # Application logic
│   │   └── starfield.js       # Animation
│   └── static/                # Assets
│
├── test.py                    # API handler (modified)
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
├── README.md                  # Quick start guide
├── DEPLOYMENT.md              # Deployment guide
├── netlify.toml               # Netlify config
├── railway.json               # Railway config
├── Procfile                   # Heroku/Render config
└── start.sh / start.bat       # Quick start scripts
```

## Data Flow

```
User uploads document
    ↓
Frontend (index.html)
    ↓
POST /upload → Backend API
    ↓
Document Loader → Chunks text
    ↓
Embeddings Provider → Generates vectors (HuggingFace)
    ↓
Vector Store → Saves to ChromaDB
    ↓
Returns success


User asks question
    ↓
Frontend (index.html)
    ↓
POST /query → Backend API
    ↓
Vector Store → Searches similar chunks
    ↓
LLM Provider → Generates answer (HuggingFace)
    ↓
Returns response to user
```

## Component Details

### Backend API (FastAPI)
- `POST /upload` - Process uploaded documents
- `POST /query` - Answer questions
- `GET /stats` - System statistics  
- `DELETE /clear` - Clear knowledge base
- CORS enabled for frontend

### RAG System
- **Document Loader**: Handles PDF, TXT, DOCX, HTML
- **Text Splitter**: Chunks with overlap
- **Embeddings**: BAAI/bge-large-en-v1.5 via HuggingFace
- **LLM**: Kimi-K2-Instruct via HuggingFace Novita
- **Vector DB**: ChromaDB (local persistence)

### Frontend
- Pure JavaScript (no framework)
- Starfield canvas animation
- Dark theme UI
- Real-time file upload
- Chat interface
- Mobile responsive

## Security

- HF_TOKEN stored in environment only
- No secrets in code
- CORS configured
- Input validation
- File type restrictions

## Scalability

- Stateless API (horizontal scaling)
- ChromaDB (can replace with cloud DB)
- HuggingFace Inference (auto-scaling)
- Static frontend (CDN-ready)
