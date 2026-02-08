// Frontend Configuration
// Edit this file to set your backend API URL for production deployment

window.FRONTEND_CONFIG = {
    // Set to your deployed backend URL
    // Examples:
    // - Railway: 'https://your-app.railway.app'
    // - Render: 'https://your-app.onrender.com'
    // - Heroku: 'https://your-app.herokuapp.com'
    API_URL: window.ENV_API_URL || 'http://localhost:8000'
};
