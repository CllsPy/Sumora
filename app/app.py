from pipeline.builder_pipeline import LlmWhisperPipelineBuilder

if __name__ == "__main__":
    pipeline = LlmWhisperPipelineBuilder().build()
    summary = pipeline.run("https://www.cnnbrasil.com.br/")
    print(summary)
