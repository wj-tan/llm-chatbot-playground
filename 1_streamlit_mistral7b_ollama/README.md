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
```

## 🐳 Run the App with Docker

You can also run this app fully containerized using Docker.

### 🧱 Step 1: Build the Docker Image

```bash
docker build -t streamlit-chatbot .
docker run -p 8501:8501 streamlit-chatbot
```

### 🚀 Step 2: Run the Docker Container

```bash
docker run -p 8501:8501 streamlit-chatbot
```

### ⚙️ Optional: Customize the Ollama Server URL

If your Ollama server is running on a different endpoint, edit the base_url in app.py:

```
client = OpenAI(
    base_url = 'https://<your-server-url>/v1/',
    api_key='ollama',  # required, but unused, just put anything will do
)
```

Then rebuild the Docker image for the change to take effect:

```bash
docker build -t streamlit-chatbot .
```


