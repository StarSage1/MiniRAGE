# mini-rag

This is a minimal implementation of the RAG model for question answering.

## Requirments

- Python 3.8 or later

### Install Python using Miniconda

1) Download and install Miniconda 
2) create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.8
```
3) Activate the environment:
```bash
$ conda activate mini-rag
```

## Installation

```bash
$ pip install reqirements.txt
```

### setup the environment variables

```bash
$ cp .env.example .env
```

set your environment variables in the `.env` file. like `openai_api_key` value.

```bash 
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
## POSTMAN collection

Download POSTMAN collection from [/assets/mini-rag-app.postman_collection.json]
