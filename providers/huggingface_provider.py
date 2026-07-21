from config import HUGGINGFACE_API_KEY

from providers.http_provider import HTTPProvider


class HuggingFaceProvider(HTTPProvider):

    name = "huggingface"

    BASE_URL = "https://router.huggingface.co/v1/chat/completions"

    API_KEY = HUGGINGFACE_API_KEY

    DEFAULT_MODEL = "Qwen/Qwen3-Coder"

    def available_models(self):
        return [
            "Qwen/Qwen3-Coder",
            "deepseek-ai/DeepSeek-V3",
            "meta-llama/Llama-3.3-70B-Instruct",
            "mistralai/Mistral-Large-Instruct",
        ]
