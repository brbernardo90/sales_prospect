from typing import Optional

from fastapi import FastAPI
from openai_generate import llm_generate_response

app = FastAPI()


@app.get("/")
async def root():
    response = llm_generate_response("Hello World")
    return {"message": response}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}