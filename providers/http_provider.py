import requests

from providers.base_provider import BaseProvider

from core.request import AIRequest
from core.response import AIResponse


class HTTPProvider(BaseProvider):
    """
    Base class for providers that expose an OpenAI-compatible HTTP API.
    """

    BASE_URL = ""
    API_KEY = ""
    DEFAULT_MODEL = ""

    def headers(self):
        return {
            "Authorization": f"Bearer {self.API_KEY}",
            "Content-Type": "application/json",
        }

    def build_payload(self, request: AIRequest):

        messages = []

        if request.system_prompt:
            messages.append({
                "role": "system",
                "content": request.system_prompt
            })

        messages.append({
            "role": "user",
            "content": request.prompt
        })

        return {
            "model": request.model or self.DEFAULT_MODEL,
            "messages": messages,
            "temperature": request.temperature,
            "max_tokens": request.max_tokens,
        }

    def parse_response(self, response_json):

        choices = response_json.get("choices", [])

        if not choices:
            raise ValueError("Provider returned no choices.")

        return choices[0]["message"]["content"]

    def chat(self, request: AIRequest):

        try:

            response = requests.post(
                self.BASE_URL,
                headers=self.headers(),
                json=self.build_payload(request),
                timeout=60,
            )

            response.raise_for_status()

            data = response.json()

            text = self.parse_response(data)

            return AIResponse(
                success=True,
                text=text,
                provider=self.name,
                model=request.model,
            )

        except requests.Timeout:

            return AIResponse(
                success=False,
                text="Request timed out.",
                provider=self.name,
                model=request.model,
            )

        except requests.HTTPError:

            try:
                error = response.json()
            except Exception:
                error = response.text

            return AIResponse(
                success=False,
                text=f"HTTP Error: {error}",
                provider=self.name,
                model=request.model,
            )

        except Exception as e:

            return AIResponse(
                success=False,
                text=str(e),
                provider=self.name,
                model=request.model,
            )

    def health_check(self):
        return bool(self.API_KEY)

    def available_models(self):
        return []
