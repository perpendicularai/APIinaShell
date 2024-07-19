from fastapi import FastAPI
import uvicorn
from llama_cpp import Llama
import os

app = FastAPI()

username = os.getenv("USERNAME")

@app.post("/api/generate/")
async def gentext(prompt: str):
    llm = Llama(
        model_path=f"<PATH TO GGUF MODEL>"
    )

    output = llm.create_chat_completion(
        [
            {
                'role':'user', 'content': f'{prompt}',
            }
        ]
    )

    final_response = output

    return {
            "llamacpp_response": final_response
        }

