from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class LlmWhisperPipeline:
    def __init__(self, summarizer, data_loader):
        self.summarizer = summarizer
        self.data_loader = data_loader
    
    def run(self, url: str):
        try:
            logger.info("Runing Pipeline.")

            content = self.data_loader(url).acess_and_extract()
            
            summary = self.summarizer.get_summary(content)

            logger.info("Pipeline Completed sucessfully,")
            return summary
    
        except Exception as e:
            logger.error(f"Pipeline Failed {str(e)}")
            raise CustomException(e)
            
