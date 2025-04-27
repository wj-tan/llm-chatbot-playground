# 🧠 Streamlit + Mistral 7B Chatbot (served via Ollama)

This is a simple, self-hosted chatbot app built with:

- 🖼️ **Streamlit** as the UI  
- 🧠 **Mistral 7B** as the language model  
- 🚀 **Ollama** to serve the model with an OpenAI-compatible API

It mimics a ChatGPT-style interface, running entirely on your own infrastructure (or on free Colab GPU!).

---

## ⚙️ Steps to Run

### 🛰️ 1. Start Ollama Server (Colab)

Run the [`ollama_server.ipynb`](./ollama_server.ipynb) notebook in **Google Colab**.  
Make sure to select a **T4 GPU runtime** (under `Runtime > Change runtime type > GPU > T4`).

This will start an Ollama server with `mistral` loaded and exposed via public URL.

---

### 🖥️ 2. Run the Streamlit Frontend

Once the server is running, clone this repo and start the Streamlit app locally:

```bash
git clone https://github.com/wj-tan/vllm-demo.git
cd vllm-demo/1_streamlit_mistral7b_ollama
pip install -r requirements.txt
streamlit run app.py
