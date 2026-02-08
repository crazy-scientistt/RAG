# 📦 Installation Guide - Step by Step

## Prerequisites Check

Before you start, you need:

1. ✅ **Python 3.12.8**
2. ✅ **HuggingFace account** with token
3. ✅ **Terminal/Command Prompt** access
4. ✅ **Internet connection**

## Step 1: Verify Python Version (2 minutes)

```bash
python --version
```

**Expected output:** `Python 3.12.8`

**If you see a different version:**
- See [PYTHON_REQUIREMENTS.md](PYTHON_REQUIREMENTS.md) for installation
- Or use `python3.12` instead of `python` in all commands

## Step 2: Extract the Project (30 seconds)

```bash
# Extract ZIP file
unzip ragcloud_web_fixed.zip

# Navigate into folder
cd ragcloud_web

# List files to verify
ls -la
```

You should see:
- `backend/` folder
- `frontend/` folder
- `start.sh` or `start.bat`
- `.env.example`
- `README.md`

## Step 3: Get HuggingFace Token (2 minutes)

### 3a. Create Token

1. Go to: https://huggingface.co/settings/tokens
2. Click **"Create new token"**
3. Select **"Fine-grained"** type
4. Enable **"Make calls to Inference Providers"**
5. Click **"Generate token"**
6. **Copy the token** (starts with `hf_`)

### 3b. Save Token

```bash
# Copy the example file
cp .env.example .env

# Edit .env file
nano .env  # or use any text editor
```

Change this line:
```
HF_TOKEN=your_huggingface_token_here
```

To:
```
HF_TOKEN=hf_your_actual_token_here
```

Save and exit.

## Step 4: Install Dependencies (2-3 minutes)

### Option A: Automatic (Easiest)

```bash
# This installs everything automatically
./start.sh  # Linux/Mac
# OR
start.bat   # Windows
```

The script will:
- ✅ Check Python version
- ✅ Create virtual environment
- ✅ Install all packages from requirements.txt
- ✅ Start both backend and frontend
- ✅ Open on http://localhost:3000

**Done! Skip to Step 6.**

### Option B: Manual Installation

If automatic doesn't work, do it manually:

```bash
# 1. Go to backend folder
cd backend

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate  # Windows

# 4. Your terminal should now show (venv)

# 5. Upgrade pip
pip install --upgrade pip

# 6. Install all dependencies
pip install -r requirements.txt

# Wait 2-3 minutes for installation...
```

## Step 5: Run the System (30 seconds)

### If you used Option A (start.sh):
Already running! Go to Step 6.

### If you used Option B (manual):

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python app.py
```

You should see:
```
✅ System initialized successfully!
📦 LLM: Kimi-K2-Instruct
Uvicorn running on http://0.0.0.0:8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
python -m http.server 3000
```

You should see:
```
Serving HTTP on 0.0.0.0 port 3000 ...
```

## Step 6: Test the System (1 minute)

### 6a. Open in Browser

Open: http://localhost:3000

You should see:
- ✅ Dark starfield background
- ✅ "Cloud RAG System" title
- ✅ Upload area
- ✅ Chat interface

### 6b. Test Backend Connection

Open: http://localhost:3000/test.html

This runs automatic diagnostics. All tests should pass:
- ✅ Test 1: Backend Health Check
- ✅ Test 2: Stats Endpoint
- ✅ Test 3: CORS Check

### 6c. Upload a Test Document

1. Click upload area or drag a PDF/TXT/DOCX file
2. Wait for "✓ filename uploaded successfully"
3. Document count should increase
4. Chat interface should enable

### 6d. Ask a Question

1. Type a question about your document
2. Click "Ask" or press Enter
3. Wait for AI response
4. Response should appear in chat

**Success!** ✅ System is working!

## Verification Checklist

After installation, verify:

- [ ] Python version is 3.12.8: `python --version`
- [ ] .env file exists with HF_TOKEN set
- [ ] Virtual environment created: `backend/venv/` folder exists
- [ ] Dependencies installed: `pip list` shows fastapi, chromadb, etc.
- [ ] Backend running: http://localhost:8000 shows {"status":"online"}
- [ ] Frontend running: http://localhost:3000 shows upload page
- [ ] Test page passes: http://localhost:3000/test.html all green
- [ ] Can upload file successfully
- [ ] Can ask questions and get answers

## Common Installation Issues

### "python: command not found"

**Fix:** Use `python3` instead:
```bash
python3 --version
python3 -m venv venv
```

### "pip: command not found"

**Fix:** Use python -m pip:
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### "Package installation failed"

**Fix:** Install packages individually:
```bash
pip install fastapi
pip install uvicorn[standard]
pip install python-multipart
pip install requests
pip install chromadb
pip install langchain
pip install langchain-text-splitters
pip install pypdf
pip install python-docx
pip install beautifulsoup4
pip install python-dotenv
```

### "Port 8000 already in use"

**Fix:** Kill existing process:
```bash
# Linux/Mac
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### "Cannot import name 'FastAPI'"

**Fix:** Virtual environment not activated:
```bash
source backend/venv/bin/activate  # Linux/Mac
backend\venv\Scripts\activate  # Windows
```

### "HF_TOKEN not found"

**Fix:** Check .env file:
```bash
cat .env  # Should show HF_TOKEN=hf_...
```

Make sure:
- File is named `.env` (not `.env.txt`)
- Token starts with `hf_`
- No quotes around token
- No spaces

## Next Steps

After successful installation:

1. **Upload documents:** PDF, TXT, DOCX, or HTML files
2. **Ask questions:** About the uploaded content
3. **Explore:** Try different types of documents
4. **Deploy:** See [DEPLOYMENT.md](DEPLOYMENT.md) for cloud hosting

## Need Help?

- 📖 [README.md](README.md) - Quick start
- 🐍 [PYTHON_REQUIREMENTS.md](PYTHON_REQUIREMENTS.md) - Python setup
- 🔧 [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Fix common issues
- ⚡ [QUICKFIX.md](QUICKFIX.md) - Upload errors
- 🏗️ [ARCHITECTURE.md](ARCHITECTURE.md) - How it works

Happy RAGging! 🚀
