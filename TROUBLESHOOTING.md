# 🔧 Troubleshooting Guide

## Common Issues and Solutions

### 1. Backend Connection Errors

#### ❌ "Cannot connect to backend at http://localhost:8000"

**Symptoms:**
- Frontend shows "Offline" in the UI
- Red error message about connection
- Browser console shows network errors

**Solutions:**

1. **Check if backend is running:**
   - Look for terminal/command window with backend
   - Should show: "Uvicorn running on http://0.0.0.0:8000"
   - If not running, start it: `cd backend && start.bat` (Windows) or `./start.sh` (Linux/Mac)

2. **Check the URL:**
   - Open `frontend/config.js`
   - Verify: `API_URL: 'http://localhost:8000'`
   - Make sure it's NOT `'/api/chat'` or any other path

3. **Test backend directly:**
   - Open browser: http://localhost:8000
   - Should see: `{"status":"online","message":"Cloud RAG API",...}`
   - If you get "connection refused" → backend not running
   - If you get a response → backend is fine, check frontend config

### 2. HuggingFace Token Issues

#### ❌ "No HuggingFace token found!"

**Solution:**
```bash
# Windows CMD
set HF_TOKEN=hf_your_token_here

# Windows PowerShell  
$env:HF_TOKEN="hf_your_token_here"

# Linux/Mac
export HF_TOKEN=hf_your_token_here
```

**Or create `.env` file in backend folder:**
```
HF_TOKEN=hf_your_token_here
```

#### ❌ "Invalid token" or authentication errors

**Solutions:**

1. **Check token permissions:**
   - Go to https://huggingface.co/settings/tokens
   - Token must have "Inference Providers" permission enabled
   - Must be a "Fine-grained" token, not "Read" or "Write"

2. **Regenerate token:**
   - Delete old token
   - Create new "Fine-grained" token
   - Enable "Make calls to Inference Providers"
   - Copy new token and set it again

### 3. Module/Import Errors

#### ❌ "ModuleNotFoundError: No module named 'fastapi'"

**Solution:**
```bash
cd backend
pip install -r requirements.txt
```

#### ❌ "ModuleNotFoundError: No module named 'config'"

**Solution:**
This happens when running from wrong directory.

**Always run from backend directory:**
```bash
cd backend
python app.py
```

### 4. File Upload Issues

#### ❌ "Unsupported file type"

**Supported formats only:**
- PDF: `.pdf`
- Text: `.txt`
- Word: `.docx`
- HTML: `.html`, `.htm`

**Not supported:**
- `.doc` (old Word format) - convert to `.docx`
- `.odt`, `.rtf` - convert to `.docx` or `.txt`
- Images - OCR not supported yet

#### ❌ Upload fails silently or shows error

**Check backend logs for:**
```
Error processing document: ...
```

**Common causes:**
1. **Corrupted file** → Try different file
2. **Empty file** → File must have content
3. **Scanned PDF** → Must be text-based PDF (not image)

### 5. CORS Errors

#### ❌ "CORS policy: No 'Access-Control-Allow-Origin' header"

**This happens when using `file://` protocol**

**Solution - Use local server:**
```bash
cd frontend
python -m http.server 3000
```
Then open: http://localhost:3000

**Alternative - Use any web server:**
```bash
# Node.js
npx http-server frontend -p 3000

# PHP
cd frontend && php -S localhost:3000
```

### 6. No Response from AI

#### ❌ Questions get stuck or timeout

**Check backend logs for:**
```
Error generating response: ...
```

**Common causes:**

1. **HuggingFace service down:**
   - Check: https://status.huggingface.co
   - Try different model in `config.py`

2. **No documents uploaded:**
   - System needs documents to answer questions
   - Upload at least one document first

3. **Network issues:**
   - Check internet connection
   - HuggingFace Inference requires internet

### 7. Slow Performance

#### ❌ Uploads or queries are very slow

**Solutions:**

1. **Reduce chunk size in `backend/config.py`:**
   ```python
   CHUNK_SIZE: int = 500  # Instead of 1000
   ```

2. **Reduce number of results:**
   ```python
   TOP_K_RESULTS: int = 2  # Instead of 4
   ```

3. **Use faster model:**
   ```python
   LLM_MODEL: str = "meta-llama/Llama-3.2-3B-Instruct:groq"
   ```
   (Groq is much faster than Novita for some models)

### 8. Vector Database Errors

#### ❌ "ChromaDB" errors or database corruption

**Solution - Reset database:**
```bash
# Stop backend first!
# Then delete database:

# Windows
rmdir /s data

# Linux/Mac
rm -rf data

# Restart backend - will create fresh database
```

### 9. Port Already in Use

#### ❌ "Address already in use" or "Port 8000 is in use"

**Find and kill process:**

**Windows:**
```cmd
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F
```

**Linux/Mac:**
```bash
lsof -ti:8000 | xargs kill -9
```

**Or use different port in `backend/app.py`:**
```python
uvicorn.run(app, host="0.0.0.0", port=8001)  # Changed to 8001
```
And update `frontend/config.js`:
```javascript
API_URL: 'http://localhost:8001'
```

## 🧪 Testing Your Setup

### 1. Test Backend

```bash
cd backend
python -c "from rag_system import CloudRAG; rag = CloudRAG(); print('SUCCESS')"
```

Should print configuration and "SUCCESS"

### 2. Test API Endpoints

```bash
# Health check
curl http://localhost:8000

# Stats
curl http://localhost:8000/stats
```

### 3. Check Browser Console

1. Open frontend
2. Press F12 → Console tab
3. Should see: "✅ Backend connected!"
4. Any errors? They'll show here

## 📞 Still Having Issues?

1. **Check all logs:**
   - Backend terminal output
   - Browser console (F12)
   - Look for red error messages

2. **Verify versions:**
   ```bash
   python --version  # Should be 3.10+
   pip list | grep fastapi
   pip list | grep chromadb
   ```

3. **Clean install:**
   ```bash
   # Remove old environment
   rm -rf venv
   
   # Fresh install
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

## 🐛 Reporting Bugs

When reporting issues, include:
1. Operating System
2. Python version
3. Full error message from backend
4. Browser console errors
5. Steps to reproduce
