from src.data_loader import WebsiteContentExtractor
from src.summarizer import llmWhisper
from pipeline.pipeline import LlmWhisperPipeline
from src.prompt_template import get_system_prompt, get_user_prompt_prefix
from config.config import OPENAI_API_KEY, MODEL_NAME

class LlmWhisperPipelineBuilder:
    def build(self) -> LlmWhisperPipeline:
        summarizer = llmWhisper(api_key=OPENAI_API_KEY, model_name=MODEL_NAME)
        data_loader = WebsiteContentExtractor

        return LlmWhisperPipeline(
            summarizer=summarizer,
            data_loader=data_loader,
        )