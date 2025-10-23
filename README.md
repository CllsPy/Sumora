# Blog Summary System

## Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B8BBE?logo=python&logoColor=white)
![C4 Model](https://img.shields.io/badge/C4%20Model-232F3E?logo=diagram&logoColor=white)

## Understand How To Improve Your Personal Blog Trough A Funny Review
A summarization system using a Large Language Model (LLM) automatically condenses long texts into concise summaries. It collects and preprocesses content, builds a prompt to guide the model, and uses the LLM’s contextual understanding to generate clear, focused summaries. This enables faster information consumption and supports tasks like news analysis, research synthesis, and business reporting.

## About This Project

### C4 Model
![c4lvl2](https://github.com/user-attachments/assets/11669801-7bd6-49b8-81ea-fe0f0e23cee7)

We will build a summatization system using gpt-5-nano, trough [OpenAI Api](https://openai.com/fr-FR/index/openai-api/). The system will recieve the user's url blog, extract the content with [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/) and the generate a fuuny summary to the user. Finnaly, we deployed the sistem using [Streamlit Community Cloud](https://streamlit.io/cloud).

## Development Roadmap
Follow these steps to implement the system:

1. Environment Setup - Prepare the project base
2. Data Collection - Gather Blog Information
3. Data Preprocessing - Clean Blog Data
4. Sumarization Pipeline - Implement the following step
  - extract data
  - process data
  - summarize content
5. Cloud Deployment - Deploy on Streamlit Cloud Community

Prerequisites
Python | Version 3.11.9
Streamlit Cloud Community Account - Free Tier
OpenAI Api - Paid

## Required Packages
Install these Python packages before running the code:

```python
python-dotenv
openai
scraper
streamlit
beautifulsoup4
```

