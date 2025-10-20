import streamlit as st
from pipeline.builder_pipeline import LlmWhisperPipelineBuilder
from pipeline.pipeline import LlmWhisperPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="GPTWhisper", layout="wide")


load_dotenv()

@st.cache_resource
def init_pipeline():
    return LlmWhisperPipelineBuilder()

pipeline = init_pipeline().build()

st.title("O que teus amigos não tem coragem de falar")

query = st.text_input("URL")
if query:
    with st.spinner("Disperdiçando energia com você..."):
        response = pipeline.run(query)
        st.markdown("### Meu desprezo: ")
        st.write(response)