# Cloud RAG System - Fixed Version

A Retrieval-Augmented Generation (RAG) system using HuggingFace Inference Providers.

## 🚀 Quick Start

### Prerequisites
- Python 3.10+ 
- HuggingFace account with Inference Providers token
- Modern web browser

### Step 1: Get HuggingFace Token

1. Go to https://huggingface.co/settings/tokens
2. Create a **Fine-grained** token
3. Enable **"Make calls to Inference Providers"** permission
4. Copy your token

### Step 2: Set Environment Variable

**Windows (Command Prompt):**
```cmd
set HF_TOKEN=your_token_here
```

**Windows (PowerShell):**
```powershell
$env:HF_TOKEN="your_token_here"
```

**Linux/Mac:**
```bash
export HF_TOKEN=your_token_here
```

**Or create a `.env` file in the backend directory:**
```
HF_TOKEN=your_token_here
```

### Step 3: Start Backend

**Windows:**
```cmd
cd backend
start.bat
```

**Linux/Mac:**
```bash
cd backend
./start.sh
```

The backend will start on `http://localhost:8000`

### Step 4: Open Frontend

Simply open `frontend/index.html` in your web browser.

**Or use Python's built-in server:**
```bash
cd frontend
python -m http.server 3000
```
Then visit `http://localhost:3000`

## 📁 Project Structure

```
rag-fixed/
├── backend/
│   ├── app.py              # FastAPI server
│   ├── config.py           # Configuration
│   ├── rag_system.py       # RAG orchestration
│   ├── llm_provider.py     # LLM interface
│   ├── embeddings_provider.py # Embeddings interface
│   ├── vector_store.py     # ChromaDB vector store
│   ├── document_loader.py  # Document processing
│   ├── requirements.txt    # Python dependencies
│   ├── start.bat          # Windows start script
│   └── start.sh           # Linux/Mac start script
├── frontend/
│   ├── index.html         # Main UI
│   ├── config.js          # Frontend config
│   └── js/
│       ├── app.js         # Main app logic
│       └── starfield.js   # Background animation
└── data/                  # Vector database storage
```

## 🔧 How to Use

1. **Upload Documents**: Drag & drop or click to upload PDF, TXT, DOCX, or HTML files
2. **Ask Questions**: Type your question and press Enter or click Ask
3. **View Sources**: See which document chunks were used to answer
4. **Clear Data**: Click Clear to remove all documents and start fresh

## 📝 Supported File Types

- PDF (`.pdf`)
- Text files (`.txt`)
- Word documents (`.docx`)
- HTML files (`.html`, `.htm`)

## 🐛 Troubleshooting

### Backend won't start

**Error: "No HuggingFace token found"**
- Make sure you've set the `HF_TOKEN` environment variable
- Check that the token has "Inference Providers" permission

**Error: "Module not found"**
- Run: `pip install -r requirements.txt`

### Frontend can't connect

**Error: "Cannot connect to backend"**
- Make sure backend is running on `http://localhost:8000`
- Check the browser console (F12) for errors
- Verify `frontend/config.js` has the correct API_URL

**CORS errors:**
- Make sure you're not using `file://` protocol
- Use a local server: `python -m http.server 3000`

### No documents showing

- Check backend logs for upload errors
- Verify file format is supported
- Check that files contain extractable text

## 💡 Configuration

Edit `backend/config.py` to customize:

- **LLM Model**: Change `LLM_MODEL` to use different models
- **Chunk Size**: Adjust `CHUNK_SIZE` for different document splitting
- **Retrieval Count**: Modify `TOP_K_RESULTS` for more/fewer sources

## 🔒 Security Notes

- Never commit your HF_TOKEN to version control
- Use environment variables for sensitive data
- This is for development/testing - add authentication for production

## 📚 API Endpoints

- `GET /` - Health check
- `GET /stats` - System statistics
- `POST /upload` - Upload document
- `POST /query` - Ask question
- `DELETE /clear` - Clear knowledge base

## 🎯 Key Fixes from Original

1. ✅ Fixed frontend API URL configuration
2. ✅ Removed duplicate files in root directory
3. ✅ Simplified directory structure
4. ✅ Added proper startup scripts
5. ✅ Fixed CORS configuration
6. ✅ Improved error messages
7. ✅ Added comprehensive documentation

## 📞 Need Help?

Check the browser console (F12) and backend terminal for error messages.
