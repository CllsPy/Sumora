from openai import OpenAI
from src.prompt_template import get_system_prompt, get_user_prompt_prefix


class llmWhisper:
    def __init__(self, api_key: str, model_name: str):
        self.api_key = api_key
        self.model_name = model_name
        self.openai = OpenAI()


    def build_prompt(self, content: str):
        return [
            {"role": "system", "content": get_system_prompt()},
            {"role": "user", "content": get_user_prompt_prefix() + content}
        ]

    def get_summary(self, content: str):
        response = self.openai.chat.completions.create(
            model=self.model_name,
            messages=self.build_prompt(content) 
        )
        return (response.choices[0].message.content)
