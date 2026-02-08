const fetch = require('node-fetch');

exports.handler = async (event) => {
  // 1. Only allow POST requests
  if (event.httpMethod !== "POST") {
    return { 
      statusCode: 405, 
      body: JSON.stringify({ error: "Method Not Allowed" }) 
    };
  }

  try {
    // 2. Parse the incoming message from your frontend
    const body = JSON.parse(event.body);
    const userMessage = body.inputs || body.message;

    // 3. Call HuggingFace
    const response = await fetch(
      "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill",
      {
        headers: { 
          Authorization: `Bearer ${process.env.HF_TOKEN}`,
          "Content-Type": "application/json" 
        },
        method: "POST",
        body: JSON.stringify({ inputs: userMessage }),
      }
    );

    const data = await response.json();

    // 4. Return the AI's response
    return {
      statusCode: 200,
      body: JSON.stringify(data),
    };
  } catch (error) {
    console.error("Error:", error);
    return { 
      statusCode: 500, 
      body: JSON.stringify({ error: error.message }) 
    };
  }
};
