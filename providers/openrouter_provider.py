from config import OPENROUTER_API_KEY

from providers.http_provider import HTTPProvider


class OpenRouterProvider(HTTPProvider):

    name = "openrouter"

    BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

    API_KEY = OPENROUTER_API_KEY

    DEFAULT_MODEL = "deepseek/deepseek-chat-v3"

    def available_models(self):
        return [
            "deepseek/deepseek-chat-v3",
            "qwen/qwen3-coder",
            "meta-llama/llama-3.3-70b-instruct",
        ]
