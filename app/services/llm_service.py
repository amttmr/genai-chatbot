import openai
import google.generativeai as genai
from groq import Groq
import os
from dotenv import load_dotenv
from prompts.templates import get_prompt_template

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Groq client
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(message: str, model: str = "openai") -> str:
    if model == "openai":
        return generate_openai_response(message)
    elif model == "gemini":
        return generate_gemini_response(message)
    elif model == "groq":
        return generate_groq_response(message)
    elif model == "local":
        return generate_local_response(message)
    else:
        raise ValueError("Unsupported model")

def generate_openai_response(message: str) -> str:
    try:
        system_prompt = get_prompt_template("chat").replace("{user_message}", message)
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI API error: {e}")
        raise

def generate_gemini_response(message: str) -> str:
    try:
        system_prompt = get_prompt_template("chat").replace("{user_message}", message)
        model = genai.GenerativeModel('models/gemini-pro')
        response = model.generate_content(system_prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API error: {e}")
        raise

def generate_groq_response(message: str) -> str:
    try:
        print(f"Groq input message: {message}")
        response = groq_client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Respond in a friendly and informative way."},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Groq API error: {e}")
        raise

def generate_local_response(message: str) -> str:
    # Placeholder for local LLM integration
    # For example, using a local model like GPT-J or similar
    # This would require additional setup
    return f"Local response to: {message}"
