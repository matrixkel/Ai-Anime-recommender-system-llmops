import os 
from dotenv import load_dotenv
from typing import cast


load_dotenv()

GROQ_API_KEY = cast(str, os.getenv("GROQ_API_KEY"))
MODEL_NAME = "llama-3.1-8b-instant"