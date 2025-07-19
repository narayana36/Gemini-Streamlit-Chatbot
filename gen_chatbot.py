import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
Gemini_Api_Key=os.getenv("gemini_api_key")
genai.configure(api_key=Gemini_Api_Key)

llm = genai.GenerativeModel("models/gemini-1.5-flash")


if "history" not in st.session_state:
    st.session_state.history = []
    
def format_history_for_model(history):
    '''Formats history entries to match the model's expected structure'''
    formatted_history = []
    for entry in history:
        formatted_history.append({
            
            "role": entry["role"],
            
            "parts": [{"text":entry["content"]}]
        })
        
    return formatted_history

def get_response(message):

    #Format history for model and initialize chatbot
    formatted_history= format_history_for_model(st.session_state.history)
    chatbot= llm.start_chat(history=formatted_history)
    response= chatbot.send_message(message)


    #Append user message and Al response to history
    st.session_state.history.append({"role": "user", "content": message})
    st.session_state.history.append({"role": "model", "content": response.text})

    return response.text

st.title("Welcome to the Chatbot")


st.chat_message("ai").write("Hello, I am a helpful AI Assistant. How can I help you today?")

#Display the previous chat history

for entry in st.session_state.history:
    if entry["role"]=="user":
        st.chat_message("human").write(entry["content"])
    else:
        st.chat_message("ai").write(entry["content"])


human_prompt=st.chat_input("Say Something.....!")

if human_prompt:
    st.chat_message("human").write(human_prompt)
    response = get_response(human_prompt)
    st.chat_message("ai").write(response)
    