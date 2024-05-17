from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import json
import uvicorn

app = FastAPI()

class QuestionInput(BaseModel):
    question: list[str]

@app.post("/api/chat")
async def chat(question_input: QuestionInput):
    url = "http://127.0.0.1:11434/api/chat"
    
    # Join the multiline input into a single string
    question = "\n".join(question_input.question)
    
    data = { "model": "llama3", "messages": [ { "role": "user", "content": question } ] }

    try:
        r = requests.post(url, data=json.dumps(data))
        r.raise_for_status()
        final_res = r.text

        # Split the response into individual JSON strings
        response_objects = final_res.strip().split('\n')

        # Initialize an empty string to store the concatenated content
        concatenated_content = ""

        # Parse each JSON string and extract the content
        for obj in response_objects:
            message = json.loads(obj)
            content = message['message']['content']
            # Remove any newline characters from the content
            content = content.replace('\n', '')
            concatenated_content += content

        return {"response": concatenated_content}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)