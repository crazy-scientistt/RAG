# 🐍 Python Version & Dependencies

## Required Python Version

**Python 3.12.8** is required for this project.

### Check Your Python Version

```bash
python --version
# Should show: Python 3.12.8
```

### Install Python 3.12.8

**Windows:**
- Download from: https://www.python.org/downloads/release/python-3128/
- Run installer, check "Add Python to PATH"

**macOS:**
```bash
brew install python@3.12
```

**Linux (Ubuntu/Debian):**
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv
```

### Using Different Python Version

If you have multiple Python versions:

```bash
# Use python3.12 explicitly
python3.12 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

python --version  # Verify it's 3.12.8
```

## Package Versions

All packages use versions specified in `backend/requirements.txt`:

```
# Web Framework (for API server)
fastapi>=0.104.1
uvicorn[standard]>=0.24.0
python-multipart>=0.0.6

# Core RAG Dependencies
requests>=2.31.0          # HTTP client
chromadb>=1.0.0           # Vector database
langchain>=0.1.0          # LLM framework
langchain-text-splitters>=0.0.1  # Text chunking
pypdf>=3.17.0             # PDF processing
python-docx>=1.1.0        # Word document processing
beautifulsoup4>=4.12.0    # HTML parsing
python-dotenv>=1.0.0      # Environment variables
```

### Why These Versions?

- **`>=`** means "this version or newer"
- These are the minimum tested versions
- Ensures compatibility with Python 3.12.8
- Matches original RAG system requirements

## Installation

### Automatic (Recommended)

The start scripts automatically:
1. Check Python version
2. Create virtual environment
3. Install all dependencies

```bash
./start.sh  # or start.bat
```

### Manual Installation

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

## Verify Installation

```bash
# Activate virtual environment first
source backend/venv/bin/activate  # Linux/Mac
# or
backend\venv\Scripts\activate  # Windows

# Check installed packages
pip list

# Should see:
# fastapi        0.104.1 (or newer)
# chromadb       1.0.0 (or newer)
# langchain      0.1.0 (or newer)
# etc.
```

## Troubleshooting

### "Python 3.12.8 not found"

Install Python 3.12.8 using instructions above, then:
```bash
# Use explicit version
python3.12 -m venv venv
```

### "Package installation failed"

```bash
# Upgrade pip first
pip install --upgrade pip

# Try installing packages one by one
pip install fastapi
pip install uvicorn[standard]
# etc.
```

### "Command 'python' not found"

Try `python3` instead:
```bash
python3 --version
python3 -m venv venv
```

### Version Mismatch Warning

If you see:
```
⚠️  WARNING: Python version mismatch!
   Required: Python 3.12.8
   Found:    Python 3.11.x
```

**Options:**
1. Install Python 3.12.8 (recommended)
2. Continue anyway (might work, but not guaranteed)
3. Use Docker (always correct version)

## Using Virtual Environment

**Always activate the virtual environment before running:**

```bash
# Activate
source backend/venv/bin/activate  # Linux/Mac
backend\venv\Scripts\activate     # Windows

# Your prompt should show (venv)

# Now run commands
python app.py
pip install package-name

# Deactivate when done
deactivate
```

## Docker Alternative

Don't want to manage Python versions? Use Docker:

```dockerfile
FROM python:3.12.8-slim
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .
CMD ["python", "app.py"]
```

```bash
docker build -t ragcloud .
docker run -p 8000:8000 -e HF_TOKEN=your_token ragcloud
```

## Summary

✅ **Required:** Python 3.12.8  
✅ **Packages:** As specified in `requirements.txt`  
✅ **Install:** Use `./start.sh` for automatic setup  
✅ **Virtual Env:** Always use venv for isolation  
✅ **Check:** Run `python --version` to verify
