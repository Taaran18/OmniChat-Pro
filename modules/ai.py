import openai
import os
from dotenv import load_dotenv

load_dotenv()


class AIService:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.models = {
            "gpt-5.2": "gpt-5.2",
            "gpt-5.2-mini": "gpt-5.2-mini",
            "gpt-5.2-nano": "gpt-5.2-nano",
            "gpt-4.1": "gpt-4.1",
            "gpt-4.1-mini": "gpt-4.1-mini",
            "gpt-4.1-nano": "gpt-4.1-nano",
            "gpt-4o": "gpt-4o",
            "gpt-4o-mini": "gpt-4o-mini",
            "gpt-4-turbo": "gpt-4-turbo",
            "gpt-3.5-turbo": "gpt-3.5-turbo",
        }

    def get_chat_response(
        self, messages, model_name="gpt-4o-mini", temperature=0.7, stream=True
    ):
        model_id = self.models.get(model_name, "gpt-4o-mini")
        response = self.client.chat.completions.create(
            model=model_id, messages=messages, temperature=temperature, stream=stream
        )
        if stream:
            for chunk in response:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        else:
            return response.choices[0].message.content
