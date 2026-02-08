# 🔧 Troubleshooting Guide

## Error: "Failed to fetch" when uploading files

This error means the frontend cannot connect to the backend. Here's how to fix it:

### Step 1: Verify Backend is Running

Open a new terminal and check:

```bash
# The backend should be running on port 8000
curl http://localhost:8000
```

**Expected output:**
```json
{"status":"online","message":"Cloud RAG API","documents":0}
```

**If you get an error:** Backend is not running. Start it:

```bash
cd backend
python app.py
```

### Step 2: Check Frontend is Using Correct URL

Open browser console (F12) and look for:
```
📡 Backend API URL: http://localhost:8000
```

**If the URL is wrong:** Edit `frontend/config.js`:
```javascript
window.FRONTEND_CONFIG = {
    API_URL: 'http://localhost:8000'
};
```

### Step 3: Test Backend Connection

Open in browser:
```
http://localhost:3000/test.html
```

This will run automated tests and show exactly what's wrong.

### Step 4: Check for CORS Errors

In browser console (F12), look for errors like:
```
Access to fetch at 'http://localhost:8000/upload' from origin 'http://localhost:3000' 
has been blocked by CORS policy
```

**If you see CORS errors:**

1. Stop the backend
2. Check `backend/app.py` has:
   ```python
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],
       ...
   )
   ```
3. Restart backend: `cd backend && python app.py`

### Step 5: Verify HuggingFace Token

```bash
# Check .env file exists
cat .env

# Should show:
# HF_TOKEN=hf_your_token_here
```

**If .env is missing or empty:**
```bash
cp .env.example .env
# Edit .env and add your token
```

### Step 6: Check File Permissions

Make sure uploaded files can be saved:

```bash
# Backend creates 'uploads' directory automatically
# But check it exists and is writable
ls -la backend/uploads/
```

### Step 7: Port Conflicts

Check if ports 8000 or 3000 are already in use:

```bash
# Linux/Mac
lsof -i :8000
lsof -i :3000

# Windows
netstat -ano | findstr :8000
netstat -ano | findstr :3000
```

**If ports are in use:** Kill the process or use different ports.

## Common Error Messages

### "Cannot connect to backend at http://localhost:8000"

**Cause:** Backend not running
**Fix:** Start backend with `cd backend && python app.py`

### "HF_TOKEN not set"

**Cause:** Environment variable missing
**Fix:** Edit `.env` file and add your HuggingFace token

### "Network error - TypeError: Failed to fetch"

**Cause:** CORS or connectivity issue
**Fix:** 
1. Check backend is running
2. Verify CORS is enabled in backend
3. Use test.html to diagnose

### "Unsupported file type"

**Cause:** File type not allowed
**Fix:** Only upload PDF, TXT, DOCX, or HTML files

### "ModuleNotFoundError: No module named 'fastapi'"

**Cause:** Dependencies not installed
**Fix:** 
```bash
cd backend
pip install -r requirements.txt
```

## Quick Diagnostic Commands

```bash
# Check if backend is responding
curl http://localhost:8000

# Check backend stats
curl http://localhost:8000/stats

# Check if ports are listening
# Linux/Mac
netstat -an | grep -E "8000|3000"

# Windows
netstat -an | findstr "8000 3000"

# View backend logs
# Run backend in foreground to see logs
cd backend && python app.py
```

## Still Not Working?

1. **Restart everything:**
   ```bash
   # Kill all processes
   # Ctrl+C in all terminals
   
   # Start fresh
   ./start.sh  # or start.bat
   ```

2. **Use test page:**
   - Open `http://localhost:3000/test.html`
   - Check all test results
   - Follow specific error messages

3. **Check browser console:**
   - Press F12
   - Click "Console" tab
   - Look for red error messages
   - Share these if asking for help

4. **Verify file structure:**
   ```bash
   ragcloud_web/
   ├── backend/
   │   └── app.py  ← Must exist
   ├── frontend/
   │   ├── index.html  ← Must exist
   │   └── js/
   │       └── app.js  ← Must exist
   └── .env  ← Must exist with HF_TOKEN
   ```

5. **Try different browser:**
   - Some browsers block localhost requests
   - Try Chrome, Firefox, or Edge
   - Disable browser extensions temporarily

## Success Checklist

- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] .env file exists with HF_TOKEN
- [ ] Browser console shows no errors
- [ ] test.html shows all tests passing
- [ ] Can upload a file successfully

If all checked ✅, system should work!
