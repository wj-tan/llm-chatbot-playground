# README


This repository serves as a activity journal whereby I attempt to build an LLM chatbot


## For workstation with GPU

### Setting up an inference server with vLLM to serve a model

`podman pull vllm/vllm-openai:v0.8.4`


`podman run -d --name vllm-server -p 8000:8000 --ipc=host vllm/vllm-openai:v0.8.4 `
`sudo docker run --runtime nvidia --gpus all --ipc=host --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" --name vllm-server -d -p 8000:8000 vllm/vllm-openai:latest`

`podman exec -it vllm-server vllm serve Qwen/Qwen2.5-1.5B-Instruct`



`docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=<secret>" \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --model mistralai/Mistral-7B-v0.1`

## For workstation with only CPU

### Setting up an inference server with vLLM to serve a model

`podman pull docker.io/tweijian/vllm-cpu:0.8.4`



`podman run -d --name vllm-server -p 8000:8000 docker.io/tweijian/vllm-cpu:0.8.4`


`podman exec -it vllm-server vllm serve Qwen/Qwen2.5-1.5B-Instruct`
