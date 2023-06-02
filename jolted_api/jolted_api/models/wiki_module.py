from pydantic import BaseModel, Field
from beanie import Document
from typing import Optional
from .types import PyObjectId


class WikiModule(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str
    content: str


class WikiModuleInDB(Document, WikiModule):
    pass
