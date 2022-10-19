import requests
import os

from fastapi import FastAPI

from .config import settings as s
from .schemas import Response, GetFromResponse

API_PATH = f"/{s.url_param}"

# Add a level to the documentation and openapi.json urls to include the API directory.
new_docs_url = f"{API_PATH}/docs"
new_openapi_url = f"{API_PATH}/openapi.json"

app = FastAPI(docs_url=new_docs_url, openapi_url=new_openapi_url)

@app.get(API_PATH, response_model=Response)
def display_API_name():
    return {"API": s.display_name}

@app.get(API_PATH + "/{target}", response_model=GetFromResponse)
def reach_target(target):
    r = requests.get(f"http://{s.nginx_server}/{target}")
    return {"API":{s.display_name:r.json()}}
