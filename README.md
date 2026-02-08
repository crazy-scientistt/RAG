# ☁️ Cloud RAG System

Upload documents and ask questions powered by AI. Production-ready web application with dark theme UI and starfield animation.

## 📋 Requirements

- **Python 3.12.8** (required)
- HuggingFace account with Inference API access

Check your version: `python --version`  
See [PYTHON_REQUIREMENTS.md](PYTHON_REQUIREMENTS.md) for installation help.

## 🚀 Quick Start

### Run Backend
```bash
cd backend
pip install -r requirements.txt
export HF_TOKEN="your_huggingface_token"
python app.py
```
Runs on http://localhost:8000

### Run Frontend
```bash
cd frontend
python -m http.server 3000
```
Runs on http://localhost:3000

### Connect Frontend to Backend

**Local:** Automatic connection to localhost:8000

**Production:** Edit `frontend/config.js`:
```javascript
window.FRONTEND_CONFIG = {
    API_URL: 'https://your-backend-url.com'
};
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

## 🔐 Get HuggingFace Token

1. Visit https://huggingface.co/settings/tokens
2. Create "Fine-grained" token with "Inference Providers" permission
3. Copy token and set as `HF_TOKEN` environment variable

## 🔧 Troubleshooting

**Upload fails or "Failed to fetch" error?**

1. Open http://localhost:3000/test.html to run diagnostics
2. Check browser console (F12) for errors
3. Verify backend is running on port 8000
4. See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed help
