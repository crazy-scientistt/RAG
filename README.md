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

### Step 4: Open Frontend

Simply open `frontend/index.html` in your web browser.

## 📁 Project Structure

```
rag-fixed/
├── backend/           # All Python backend code
│   ├── app.py
│   ├── config.py
│   ├── rag_system.py
│   └── ...
├── frontend/          # All HTML/CSS/JS frontend code
│   ├── index.html
│   ├── config.js
│   └── js/
└── data/             # Vector database storage (auto-created)
```

## 🔧 How to Use

1. **Upload Documents**: Drag & drop PDF, TXT, DOCX, or HTML files
2. **Ask Questions**: Type your question and press Enter
3. **View Sources**: See which document chunks were used
4. **Clear Data**: Click Clear to remove all documents

## 🐛 Troubleshooting

See `TROUBLESHOOTING.md` for detailed solutions to common issues.

### Quick Checks:
- Backend running? Visit: http://localhost:8000
- HF_TOKEN set? Check environment variables
- Frontend can't connect? Check `frontend/config.js`
