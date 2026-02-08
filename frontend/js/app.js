// Main application logic
const API_URL = window.FRONTEND_CONFIG?.API_URL || 'http://localhost:8000';

const elements = {
    uploadArea: document.getElementById('uploadArea'),
    fileInput: document.getElementById('fileInput'),
    uploadStatus: document.getElementById('uploadStatus'),
    chatContainer: document.getElementById('chatContainer'),
    questionInput: document.getElementById('questionInput'),
    askBtn: document.getElementById('askBtn'),
    clearBtn: document.getElementById('clearBtn'),
    docCount: document.getElementById('docCount'),
    modelName: document.getElementById('modelName')
};

// Initialize app
async function init() {
    console.log('🚀 Cloud RAG System Starting...');
    console.log(`📡 Backend API URL: ${API_URL}`);
    
    await updateStats();
    setupEventListeners();
}

// Setup all event listeners
function setupEventListeners() {
    elements.uploadArea.addEventListener('click', () => elements.fileInput.click());
    elements.fileInput.addEventListener('change', handleFileSelect);
    elements.askBtn.addEventListener('click', handleAskQuestion);
    elements.clearBtn.addEventListener('click', handleClear);
    elements.questionInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !elements.askBtn.disabled) {
            handleAskQuestion();
        }
    });

    // Drag and drop
    elements.uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        elements.uploadArea.classList.add('dragover');
    });

    elements.uploadArea.addEventListener('dragleave', () => {
        elements.uploadArea.classList.remove('dragover');
    });

    elements.uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        elements.uploadArea.classList.remove('dragover');
        handleFileSelect({ target: { files: e.dataTransfer.files } });
    });
}

// Handle file selection
async function handleFileSelect(event) {
    const files = Array.from(event.target.files);
    
    if (files.length === 0) return;

    showStatus('Uploading documents...', 'info');

    for (const file of files) {
        await uploadFile(file);
    }

    elements.fileInput.value = '';
    await updateStats();
}

// Upload single file
async function uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);

    try {
        console.log(`Uploading to: ${API_URL}/upload`);
        
        const response = await fetch(`${API_URL}/upload`, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            showStatus(`✓ ${file.name} uploaded successfully`, 'success');
            enableChat();
        } else {
            showStatus(`✗ ${file.name}: ${data.detail || 'Upload failed'}`, 'error');
        }
    } catch (error) {
        console.error('Upload error:', error);
        showStatus(`✗ ${file.name}: Cannot connect to backend at ${API_URL}`, 'error');
    }
}

// Handle question submission
async function handleAskQuestion() {
    const question = elements.questionInput.value.trim();
    
    if (!question) return;

    elements.questionInput.value = '';
    elements.askBtn.disabled = true;
    elements.questionInput.disabled = true;

    addMessage(question, 'user');
    
    const loadingMsg = addLoadingMessage();

    try {
        const response = await fetch(`${API_URL}/query`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        removeMessage(loadingMsg);

        if (response.ok) {
            addMessage(data.response, 'assistant', data.sources);
        } else {
            addMessage(`Error: ${data.detail}`, 'assistant');
        }
    } catch (error) {
        removeMessage(loadingMsg);
        addMessage(`Error: Cannot connect to backend`, 'assistant');
    } finally {
        elements.askBtn.disabled = false;
        elements.questionInput.disabled = false;
        elements.questionInput.focus();
    }
}

// Handle clear chat
async function handleClear() {
    if (!confirm('Clear all documents and chat history?')) return;

    try {
        const response = await fetch(`${API_URL}/clear`, {
            method: 'DELETE'
        });

        if (response.ok) {
            elements.chatContainer.innerHTML = '<div style="text-align: center; color: rgba(255,255,255,0.4); padding: 40px;">Upload documents to start asking questions</div>';
            showStatus('Knowledge base cleared', 'success');
            disableChat();
            await updateStats();
        }
    } catch (error) {
        showStatus(`Error: ${error.message}`, 'error');
    }
}

// Add message to chat
function addMessage(content, sender, sources = null) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    
    let html = `
        <div class="message-label">${sender === 'user' ? 'You' : 'Assistant'}</div>
        <div class="message-content">${content}</div>
    `;

    if (sources && sources.length > 0) {
        html += '<div class="sources"><strong>Sources:</strong><br>';
        sources.forEach((source, idx) => {
            html += `<div class="source-item">${idx + 1}. ${source.source} (chunk ${source.chunk})</div>`;
        });
        html += '</div>';
    }

    messageDiv.innerHTML = html;
    
    if (elements.chatContainer.firstChild && elements.chatContainer.firstChild.textContent.includes('Upload documents')) {
        elements.chatContainer.innerHTML = '';
    }
    
    elements.chatContainer.appendChild(messageDiv);
    elements.chatContainer.scrollTop = elements.chatContainer.scrollHeight;
    
    return messageDiv;
}

// Add loading message
function addLoadingMessage() {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message assistant';
    messageDiv.innerHTML = `
        <div class="message-label">Assistant</div>
        <div class="message-content"><span class="loading"></span> Thinking...</div>
    `;
    elements.chatContainer.appendChild(messageDiv);
    elements.chatContainer.scrollTop = elements.chatContainer.scrollHeight;
    return messageDiv;
}

// Remove message
function removeMessage(messageDiv) {
    if (messageDiv && messageDiv.parentNode) {
        messageDiv.parentNode.removeChild(messageDiv);
    }
}

// Show status message
function showStatus(message, type) {
    elements.uploadStatus.innerHTML = `<div class="status-message ${type}">${message}</div>`;
    setTimeout(() => {
        elements.uploadStatus.innerHTML = '';
    }, 5000);
}

// Enable chat interface
function enableChat() {
    elements.questionInput.disabled = false;
    elements.askBtn.disabled = false;
}

// Disable chat interface
function disableChat() {
    elements.questionInput.disabled = true;
    elements.askBtn.disabled = true;
}

// Update system statistics
async function updateStats() {
    try {
        const response = await fetch(`${API_URL}/stats`);
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        
        const data = await response.json();
        console.log('✅ Backend connected!', data);

        elements.docCount.textContent = data.documents;
        elements.modelName.textContent = data.model.split('/').pop().split(':')[0];

        if (data.documents > 0) {
            enableChat();
        }
    } catch (error) {
        console.error('❌ Backend connection failed:', error);
        elements.docCount.textContent = '?';
        elements.modelName.textContent = 'Offline';
        showStatus(`⚠️ Cannot connect to backend at ${API_URL}`, 'error');
    }
}

// Start the application
init();
