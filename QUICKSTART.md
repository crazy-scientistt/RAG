# ⚡ Zero to Deploy in 5 Minutes

## Step 1: Get HuggingFace Token (1 min)

1. Go to https://huggingface.co/settings/tokens
2. Click "Create new token"
3. Select "Fine-grained"
4. Enable "Make calls to Inference Providers"
5. Copy the token (starts with `hf_`)

## Step 2: Configure Locally (30 sec)

```bash
# Copy environment template
cp .env.example .env

# Edit .env and paste your token
# HF_TOKEN=hf_your_token_here
```

## Step 3: Run Locally (2 min)

```bash
# Linux/Mac
./start.sh

# Windows
start.bat
```

Open http://localhost:3000

## Step 4: Test It (1 min)

1. Upload a PDF/TXT/DOCX file
2. Wait for "Document uploaded successfully"
3. Type a question about the document
4. Get AI-powered answer

## Step 5: Deploy to Cloud (Optional, 5 min)

### Backend (Railway)
1. Push to GitHub
2. Go to railway.app
3. New Project → Deploy from GitHub
4. Add environment variable: `HF_TOKEN=your_token`
5. Copy deployment URL

### Frontend (Netlify)
1. Edit `frontend/config.js`:
   ```javascript
   API_URL: 'https://your-railway-url.railway.app'
   ```
2. Push to GitHub
3. Go to netlify.com
4. New Site → Import from GitHub
5. Set base directory: `frontend`
6. Deploy

Done! Your RAG system is live on the internet. 🚀

## Troubleshooting

**"HF_TOKEN not found"**
→ Make sure you created `.env` and added your token

**"Cannot connect to backend"**
→ Check backend is running on port 8000

**"Upload failed"**
→ Only PDF, TXT, DOCX, HTML files supported

**"No response from AI"**
→ Verify HF_TOKEN is valid and has Inference API access

## Pro Tips

- Upload multiple documents to build knowledge base
- Larger documents = more context for better answers
- Clear knowledge base to start fresh
- Check backend logs for detailed errors
- HuggingFace Inference is FREE with quota

## What's Happening Under the Hood

```
Your Document
    ↓
Chunked into pieces
    ↓
Converted to vectors (embeddings)
    ↓
Stored in database
    ↓
Your Question
    ↓
Finds relevant chunks
    ↓
Sends to AI with context
    ↓
Returns answer
```

## Need Help?

- Check `README.md` for details
- Read `DEPLOYMENT.md` for cloud platforms
- See `ARCHITECTURE.md` for technical info
- Review `PROJECT_SUMMARY.md` for checklist

Happy RAGing! 🎉
