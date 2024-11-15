from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from openai_generate import llm_generate_response
from scrapy import scrape_website

app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sales-prospect.netlify.app"],  # List the front-end origins allowed to access the API
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Request schema
class SalesRequest(BaseModel):
    url: str

@app.get("/")
async def root():
    response = "Hello World"
    return {"message": response}


# Endpoint for extracting candidate information
@app.post("/sales_prospect")
async def extract_info(request: SalesRequest):
    try:
        title, body = scrape_website(request.url)

        response = llm_generate_response(title, body)
        return {"extracted_info": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))