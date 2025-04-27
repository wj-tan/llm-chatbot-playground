# LLM Chatbot Playground

This repository showcases multiple methods of building and deploying Large Language Model (LLM) chatbots, with different configurations for UI, backend APIs, and LLM models. The goal of this project is to provide simple, accessible examples of using different LLM technologies, including Streamlit UIs, OpenAI, Ollama, and more.

---

## 🧠 What is in this repo?

### Current Projects:

1. **[Streamlit + Mistral 7B + Ollama](https://github.com/wj-tan/vllm-demo/tree/main/1_streamlit_mistral7b_ollama)**
   - A simple self-hosted chatbot UI using **Streamlit**, with **Mistral 7B** as the LLM model served by the **Ollama API**.
   - **Run locally** or **containerized with Docker**.
   - Steps:
     - [Start the Ollama Server in Google Colab](./1_streamlit_mistral7b_ollama/ollama_server.ipynb) (with T4 GPU).
     - Run `streamlit run app.py` to interact with the chatbot.
     - Alternatively, build and run with Docker for a containerized version.

---

## ⚙️ How to Get Started

### Step 1: Clone the Repo

Start by cloning the repository:

```bash
git clone https://github.com/wj-tan/vllm-demo.git
cd vllm-demo
