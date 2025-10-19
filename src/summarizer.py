import os
from dotenv import load_dotenv
from openai import OpenAI
from src.data_loader import WebsiteContentExtractor
from src.prompt_template import get_system_prompt, get_user_prompt_prefix
from src.prompt_template import get_system_prompt, get_user_prompt_prefix


class llmWhisper:
    def __init__(self, api_key: str, model_name: str, url: str):
        self.model_name = model_name
        self.api_key = api_key
        self.openai = OpenAI(api_key=api_key)  
        self.website = WebsiteContentExtractor(url).acess_and_extract()

    def build_prompt(self):
        return [
            {
                "role": "system",
                "content": get_system_prompt()  
            },
            {
                "role": "user",
                "content": get_user_prompt_prefix() + self.website  
            }
        ]

    def get_summary(self):
        response = self.openai.chat.completions.create(
            model=self.model_name,
            messages=self.build_prompt() 
        )
        print(response.choices[0].message.content)
    
if __name__ == "__main__":
    whisper = llmWhisper(url="", model_name="", api_key="")
    whisper.get_summary()
