import os

from dotenv import load_dotenv

load_dotenv()

# ==================================================
# API Keys
# ==================================================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# ==================================================
# API Base URLs
# ==================================================

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

GITHUB_BASE_URL = "https://models.github.ai/inference/chat/completions"

HUGGINGFACE_BASE_URL = "https://router.huggingface.co/v1/chat/completions"
