# 🚀 Quick Start Guide

## 1️⃣ Get Your HuggingFace Token (2 minutes)

1. Visit: https://huggingface.co/settings/tokens
2. Click "New token" → Select "Fine-grained"
3. Enable: **"Make calls to Inference Providers"**
4. Click "Generate token" and copy it

## 2️⃣ Set Up Backend (1 minute)

### Option A: Using Environment Variable

**Windows Command Prompt:**
```cmd
set HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxx
cd backend
start.bat
```

**Windows PowerShell:**
```powershell
$env:HF_TOKEN="hf_xxxxxxxxxxxxxxxxxxxxx"
cd backend
.\start.bat
```

**Linux/Mac:**
```bash
export HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxx
cd backend
./start.sh
```

### Option B: Using .env File

1. Copy `.env.example` to `.env` in backend folder
2. Edit `.env` and add your token:
   ```
   HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxx
   ```
3. Run start script:
   - Windows: `start.bat`
   - Linux/Mac: `./start.sh`

## 3️⃣ Open Frontend (10 seconds)

**Easy way:** Just double-click `frontend/index.html`

**Better way (avoids CORS issues):**
```bash
cd frontend
python -m http.server 3000
```
Then open: http://localhost:3000

## ✅ You're Ready!

1. **Upload a document** (PDF, TXT, DOCX, or HTML)
2. **Ask questions** about it
3. **Get AI-powered answers** with source citations

## 🆘 Having Issues?

### Backend won't start
- ❌ No token error → Set HF_TOKEN correctly
- ❌ Module errors → Run `pip install -r requirements.txt`

### Frontend can't connect
- ❌ Check backend is running (should say "http://localhost:8000")
- ❌ Check browser console (Press F12)
- ❌ Try using `python -m http.server 3000` instead of file://

### Test Connection
1. Backend running? Visit: http://localhost:8000
2. Should see: `{"status":"online","message":"Cloud RAG API","documents":0}`

---

**That's it! You're ready to use Cloud RAG! 🎉**
