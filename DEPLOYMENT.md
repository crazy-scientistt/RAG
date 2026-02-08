# 🚀 Deployment Guide

## Prerequisites

1. HuggingFace account with Inference API access
2. GitHub account
3. Cloud platform account (Railway/Render/Netlify)

## 📦 Backend Deployment

### Option 1: Railway (Recommended)

1. Push code to GitHub
2. Visit [Railway](https://railway.app)
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add environment variable: `HF_TOKEN=your_token_here`
6. Railway auto-detects and deploys
7. Copy the deployment URL (e.g., `https://your-app.railway.app`)

### Option 2: Render

1. Push code to GitHub
2. Visit [Render](https://render.com)
3. Click "New" → "Web Service"
4. Connect GitHub repository
5. Configure:
   - Build Command: `cd backend && pip install -r requirements.txt`
   - Start Command: `cd backend && uvicorn app:app --host 0.0.0.0 --port $PORT`
6. Add environment variable: `HF_TOKEN=your_token_here`
7. Deploy and copy URL

### Option 3: AWS/Heroku

Similar process - use the `Procfile` included in the project root.

## 🌐 Frontend Deployment

### Netlify (Recommended)

1. Push code to GitHub
2. Visit [Netlify](https://netlify.com)
3. Click "Add new site" → "Import existing project"
4. Select your repository
5. Configure:
   - Base directory: `frontend`
   - Build command: (leave empty)
   - Publish directory: `.` (current directory)
6. Before deploying, edit `frontend/config.js`:
   ```javascript
   API_URL: 'https://your-backend-url.railway.app'
   ```
7. Deploy

### Alternative: Vercel/GitHub Pages

Same process - just point to the `frontend` directory.

## 🔗 Connecting Frontend & Backend

### Method 1: Edit config.js (Recommended)

Edit `frontend/config.js`:
```javascript
window.FRONTEND_CONFIG = {
    API_URL: 'https://your-backend-url.com'
};
```

### Method 2: Environment Variable

Set environment variable in Netlify:
- Key: `ENV_API_URL`
- Value: `https://your-backend-url.com`

### Method 3: Direct Edit in index.html

Add before `<script src="js/app.js">`:
```html
<script>
    window.ENV_API_URL = 'https://your-backend-url.com';
</script>
```

## ✅ Verification

1. Visit your frontend URL
2. Upload a test document
3. Ask a question
4. Verify response appears

## 🔒 Security Checklist

- [ ] `.env` is in `.gitignore`
- [ ] HF_TOKEN set as environment variable (not in code)
- [ ] CORS configured correctly in backend
- [ ] HTTPS enabled on production
- [ ] No secrets in frontend code

## 🆘 Troubleshooting

**CORS Error:**
- Check backend CORS settings allow your frontend domain

**API Not Found:**
- Verify API_URL in frontend matches backend URL
- Ensure backend is running

**Upload Fails:**
- Check file size limits
- Verify file type is supported
- Check backend logs

**No Response from AI:**
- Verify HF_TOKEN is valid
- Check Inference API quota
- Review backend logs
