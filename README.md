# README


This repository serves as a activity journal whereby I attempt to build an LLM chatbot


## For workstation with GPU

## For workstation with only CPU

### Setting up an inference server with vLLM to serve a model

`podman pull docker.io/tweijian/vllm-cpu:0.8.4`



`podman run -d --name vllm-server -p 8000:8000 docker.io/tweijian/vllm-cpu:0.8.4`


`podman exec -it vllm-server vllm serve Qwen/Qwen2.5-1.5B-Instruct`
