import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Get the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment or .env file")

# Initialize the ChatOpenAI model
model = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=api_key)

# Streamlit app
import streamlit as st

st.title("인공지능 시인")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.write("이 앱은 인공지능 시인을 소개하는 앱입니다.")

# Get the user input
content = st.text_input("시의 주제를 입력하세요.")

# Generate a poem
if st.button("시 작성 요청하기"):
    response = model.predict(content + "에 대한 시를 써줘")
    st.write(response)





