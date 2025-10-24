# Blog Summary System

<img width="860" height="516" alt="image" src="https://github.com/user-attachments/assets/d7926522-8b3e-4c6b-a159-433196b75edd" />


## Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B8BBE?logo=python&logoColor=white)
![C4 Model](https://img.shields.io/badge/C4%20Model-232F3E?logo=diagram&logoColor=white)

## Overview
This project demonstrates how to enhance a personal blog through automated content summarization. It uses a Large Language Model (LLM) to generate concise and engaging summaries of blog articles. The system retrieves a blog URL, extracts text content, and produces a short, humorous summary that helps users quickly understand the main ideas.

## About This Project

### C4 Model
![c4lvl2](https://github.com/user-attachments/assets/11669801-7bd6-49b8-81ea-fe0f0e23cee7)

This system uses the GPT-5-Nano model via the [OpenAI API](https://openai.com/fr-FR/index/openai-api/). The workflow receives a blog URL from the user, extracts content with [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/), and generates a lighthearted summary. Finally, the application is deployed using [Streamlit Community Cloud](https://streamlit.io/cloud).

## Development Roadmap

1. **Environment Setup** – Initialize the project structure.  
2. **Data Collection** – Fetch blog content using the provided URL.  
3. **Data Preprocessing** – Clean and prepare the extracted text.  
4. **Summarization Pipeline** –  
   - Extract data  
   - Process text  
   - Generate summary  
5. **Cloud Deployment** – Publish the app on Streamlit Community Cloud.

## Prerequisites
- Python 3.11.9  
- Streamlit Cloud Community account (Free Tier)  
- OpenAI API key (Paid)

## Required Packages
Install the dependencies before running the project:

```bash
pip install -e .
