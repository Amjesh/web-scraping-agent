import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.routes import webScrapSummarizer

# add dot env
load_dotenv()

app = FastAPI()

origins = os.environ.get('ALLOW_ORIGINS')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routes
app.include_router(webScrapSummarizer.router)


# Config App
host = os.environ.get('APP_HOST')
port = os.environ.get('APP_PORT')
isReload = os.environ.get('IS_RELOAD') == 'True'
if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port=int(port), reload=isReload)
