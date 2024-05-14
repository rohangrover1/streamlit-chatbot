import streamlit as st
from openai import OpenAI

def run_chatbot(personality):
    # with st.sidebar:
    #     openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    #     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    #     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    #     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

    #     option = st.selectbox(
    #     "Choose a personality",
    #     ("Drunk Uncle", "Angry Boss", "Nagging Spouse"))

    st.title(f"💬 {personality} Chatbot")
    

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
    {"role": "system", "content": f"You are an assistant with a personality of {personality}"},
    {"role": "assistant", "content": "How can I help you?"}
    ]

    for msg in st.session_state.messages:
        if msg["role"] != "system":
            st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        client = OpenAI(api_key=openai_api_key)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages, temperature=0)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

if __name__ == "__main__":
  
    st.title("Welcome to the chatbot app")

    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
        "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

        personality = st.selectbox(
        "Choose a personality",
        ("Drunk Uncle", "Angry Boss", "Nagging Spouse"),
        index=None,
        placeholder="select a personality")

    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    else:
        if not personality:
            st.info("Please choose your personality")
            st.stop()
        else:
            run_chatbot(personality)
    

    
