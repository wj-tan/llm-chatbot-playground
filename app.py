import streamlit as st
import requests
import json
import time

# Ollama API endpoint
#OLLAMA_ENDPOINT = "http://localhost:11434/v1/chat"  # change if different
OLLAMA_ENDPOINT = "https://ollama.molodetz.nl/v1/chat/completions"

st.set_page_config(page_title="Ollama Chat", page_icon="🤖")
st.title("🧠 Chat with Local LLM (Ollama)")
print("Hello")
# Chat history stored in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Build request payload for Ollama
        payload = {
            "model": "qwen2.5-coder:14b",  # CHANGE THIS (e.g., "llama3", "mistral", etc.)
            "messages": [{"role": "user", "content": prompt}],
            "stream": True,
        }

        # Stream response from Ollama
#        response = requests.post(OLLAMA_ENDPOINT, json=payload, stream=True)
#        for line in response.iter_lines():
#            if line:
#                decoded_line = line.decode('utf-8')
#                print(decoded_line)

        for line in response.iter_lines():
            if line:
                # Ollama streams JSON lines
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith('{'):
                    data = eval(decoded_line)  # safer: use `json.loads` but Ollama's output is simple
                    token = data.get("message", {}).get("content", "")
                    full_response += token
                    message_placeholder.markdown(full_response + "▌")  # Cursor effect

        message_placeholder.markdown(full_response)  # Finalize

        # Save assistant message
        st.session_state.messages.append({"role": "assistant", "content": full_response})

