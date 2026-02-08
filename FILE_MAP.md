# 📂 Project Structure

```
ragcloud_web/
│
├── 📖 Documentation
│   ├── README.md              ← Start here! Quick start guide
│   ├── PROJECT_SUMMARY.md     ← Delivery checklist
│   ├── DEPLOYMENT.md          ← Deploy to cloud platforms
│   └── ARCHITECTURE.md        ← Technical architecture
│
├── 🚀 Quick Start
│   ├── start.sh               ← Linux/Mac: Run both services
│   ├── start.bat              ← Windows: Run both services
│   ├── .env.example           ← Copy to .env, add HF_TOKEN
│   └── .gitignore             ← Prevents committing secrets
│
├── 🔧 Backend (FastAPI)
│   └── backend/
│       ├── app.py             ← Main API server ⭐
│       ├── config.py          ← System configuration
│       ├── rag_system.py      ← Core RAG logic
│       ├── document_loader.py ← PDF/DOCX/HTML processing
│       ├── embeddings_provider.py  ← HuggingFace embeddings
│       ├── llm_provider.py    ← HuggingFace LLM inference
│       ├── vector_store.py    ← ChromaDB interface
│       ├── requirements.txt   ← Python dependencies
│       ├── run.sh            ← Backend-only runner (Linux)
│       └── run.bat           ← Backend-only runner (Windows)
│
├── 🌐 Frontend (Static Web App)
│   └── frontend/
│       ├── index.html         ← Main UI ⭐
│       ├── config.js          ← API URL configuration
│       └── js/
│           ├── app.js         ← Upload & chat logic
│           └── starfield.js   ← Animated background
│
├── 🔄 Modified Entry Point
│   └── test.py                ← API handler (was CLI) ⭐
│
├── ☁️ Deployment Configs
│   ├── netlify.toml           ← Netlify (frontend)
│   ├── railway.json           ← Railway (backend)
│   └── Procfile               ← Heroku/Render (backend)
│
└── 📚 Original RAG Components (for reference)
    ├── config.py
    ├── rag_system.py
    ├── document_loader.py
    ├── embeddings_provider.py
    ├── llm_provider.py
    └── vector_store.py

⭐ = Key files you'll interact with most
```

## 🎯 File Purposes

### Must Edit/Configure
- `.env` - Add your HF_TOKEN here
- `frontend/config.js` - Set backend URL for production

### Main Entry Points
- `start.sh` / `start.bat` - Run everything locally
- `backend/app.py` - Backend API server
- `frontend/index.html` - Frontend application
- `test.py` - API handler (modified from CLI)

### Documentation
- `README.md` - Quick start (2 min read)
- `DEPLOYMENT.md` - Cloud deployment (5 min read)
- `ARCHITECTURE.md` - Technical details (5 min read)
- `PROJECT_SUMMARY.md` - Delivery checklist

### Deployment
- `netlify.toml` - Auto-deploy frontend
- `railway.json` - Auto-deploy backend
- `Procfile` - Alternative backend deployment

## 🚦 Usage Flow

1. **Setup** → Edit `.env` with HF_TOKEN
2. **Local** → Run `./start.sh`
3. **Upload** → Drop documents in web UI
4. **Ask** → Type questions in chat
5. **Deploy** → Push to GitHub, connect Railway + Netlify

## 🔐 Security

- ✅ Token in environment only
- ✅ `.env` in `.gitignore`
- ✅ No secrets in code
- ✅ CORS configured
- ✅ Production-ready
