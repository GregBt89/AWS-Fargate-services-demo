from typing import Dict
from pydantic import BaseModel

class Response(BaseModel):
   API: str

class GetFromResponse(BaseModel):
   API: Dict