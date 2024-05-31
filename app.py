import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

# Load the API key from the environment variable
key = os.getenv('api_key')

icon = Image.open("ai-removebg-preview.png")

genai.configure(api_key=key)

st.set_page_config(
    page_icon=icon,
    layout='centered',
    page_title="Lue Powered By Gemini 1.5 Pro"
)

st.markdown(f"""
            <style>
            .stApp {{
                background-image: url("https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/Keyword-Hero---2096x1182_1.gif"); 
                background-attachment: fixed;
                background-size: cover;
            }}
            .chat-message {{
                background-color: #808080;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                color: white;
            }}
            .user-message {{
                background-color: #000000;  /* Black */
            }}
            .bot-message {{
                background-color: #000000;  /* Black */
            }}
            </style>
            """, unsafe_allow_html=True)

c30, c31, c32 = st.columns([0.02, 0.3, 3])

with c30:
    st.caption(" ")
    st.image("ai-removebg-preview.png", width=80)

with c32:
    st.title("Lue Powered By Gemini 1.5 Pro")

st.subheader(' ', divider='rainbow')

# Define the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# User input
ask = st.text_input("Ask Me Anything:")

# Handle user input and generate response
if st.button("Send"):
    if ask:
        prompt_parts = [ask]
        
        # Generate response from the model
        response = model.generate_content(prompt_parts)
        
        # Store the conversation in chat history
        st.session_state.chat_history.append({"user": ask, "bot": response.text})

# Display chat history
for chat in st.session_state.chat_history:
    st.markdown(f"<div class='chat-message user-message'><strong>🙍‍♂️ You:</strong> {chat['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='chat-message bot-message'><strong>🤖 Bot:</strong> {chat['bot']}</div>", unsafe_allow_html=True)
    st.subheader(' ', divider='rainbow')  # Separator for readability
