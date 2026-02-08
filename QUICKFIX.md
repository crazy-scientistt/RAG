# ⚡ QUICK FIX: Upload "Failed to fetch" Error

## 3-Step Fix

### 1️⃣ Is Backend Running?

Open new terminal:
```bash
curl http://localhost:8000
```

**If you get an error:** Backend not running!

**Fix:**
```bash
cd backend
python app.py
```

Should see: `✅ Starting server on http://localhost:8000`

---

### 2️⃣ Run Diagnostic Test

Open in browser:
```
http://localhost:3000/test.html
```

This will show EXACTLY what's wrong.

---

### 3️⃣ Check Browser Console

1. Open website: http://localhost:3000
2. Press **F12** (or right-click → Inspect)
3. Click **Console** tab
4. Try uploading a file
5. Look for error messages

**Common messages:**

❌ `Failed to fetch` → Backend not running or wrong URL
❌ `CORS error` → Backend CORS not configured  
❌ `404 Not Found` → Wrong API endpoint
✅ `200 OK` → Success!

---

## Still Broken? Nuclear Option

Stop everything and restart:

```bash
# Kill all terminals (Ctrl+C)

# Delete and recreate .env
rm .env
cp .env.example .env
# Edit .env and add: HF_TOKEN=your_token_here

# Start fresh
./start.sh  # or start.bat on Windows
```

---

## The Real Issue (Most Common)

**99% of the time:** Backend is NOT actually running.

**How to verify:**
1. Look at your terminal running backend
2. Should see: `Uvicorn running on http://0.0.0.0:8000`
3. Open http://localhost:8000 in browser
4. Should see: `{"status":"online"...}`

**If you don't see this:** Backend crashed or never started.

**Check for:**
- Missing HF_TOKEN in .env
- Missing dependencies (run: `pip install -r requirements.txt`)
- Port 8000 already in use
- Python errors in terminal

---

## Visual Checklist

```
✅ Terminal 1: Backend running (shows "Uvicorn running...")
✅ Terminal 2: Frontend running (shows "Serving HTTP...")  
✅ Browser: http://localhost:8000 shows {"status":"online"}
✅ Browser: http://localhost:3000 shows upload page
✅ Browser Console (F12): No red errors
✅ .env file exists with HF_TOKEN set
```

All green? Should work! 🎉

Not all green? Fix the ❌ items first.

---

## Need More Help?

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for complete guide.
