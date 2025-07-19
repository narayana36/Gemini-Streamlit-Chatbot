# Gemini-Streamlit-Chatbot

A simple chatbot application built using Google's Gemini AI and the Streamlit framework. This project demonstrates how to easily create a conversational interface leveraging the power of large language models.

## Features

* **Gemini AI Integration:** Uses Google's Gemini language model for natural language understanding and generation.
* **Streamlit UI:** Provides a clean and interactive user interface for chatting with the AI.
* **Chat History Persistence:**  Maintains chat history across sessions using Streamlit's session state.
* **Secure API Key Handling:**  Loads the Gemini API key from a `.env` file, enhancing security.

## Getting Started

1. **Prerequisites:**
   * Python 3.8 or higher
   * A Google Cloud project with the Gemini API enabled.  Obtain your API key.
   * `pip install streamlit google-generativeai python-dotenv`

2. **Create a `.env` file:** Create a file named `.env` in the root directory of the project.  Add your Gemini API key:
   gemini_api_key=YOUR_API_KEY

3. **Clone the repository:**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Gemini-Streamlit-Chatbot.git
4. **Run the APP:**
    streamlit run app.py
