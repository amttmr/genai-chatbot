# GenAI Chatbot

A simple GenAI chatbot built with FastAPI, supporting OpenAI, Google Gemini, Groq, and local LLM integrations.

## Features

- FastAPI endpoint: `/chat`
- Prompt engineering with templates
- Support for OpenAI, Google Gemini, Groq, and local LLMs

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Add API keys to `.env` file:
   - `OPENAI_API_KEY=your_openai_key` (requires billing)
   - `GOOGLE_API_KEY=your_google_key` (free quota available)
   - `GROQ_API_KEY=your_groq_key` (free usage available)
3. Run the app: `python -m app.main`

## Docker

Build and run with Docker:

```bash
docker build -t genai-chatbot .
docker run -p 8000:8000 genai-chatbot
```

## API Usage

POST /chat

```json
{
  "message": "Hello, how are you?",
  "model": "openai"
}
```

Supported models: "openai", "gemini", "groq", "local"
