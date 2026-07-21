from config import GITHUB_MODELS_API_KEY

from providers.http_provider import HTTPProvider


class GitHubProvider(HTTPProvider):

    name = "github"

    BASE_URL = "https://models.github.ai/inference/chat/completions"

    API_KEY = GITHUB_MODELS_API_KEY

    DEFAULT_MODEL = "qwen/qwen3-coder"

    def available_models(self):
        return [
            "qwen/qwen3-coder",
            "deepseek-ai/DeepSeek-V3",
            "meta/Llama-4-Maverick-17B-128E-Instruct",
            "mistral-ai/Mistral-Large",
        ]
