from typing import Optional

from beanie import Document
from pydantic import BaseModel, Field

from .types import PyObjectId


class WikiModule(Document, BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str
    content: str

    class Settings:
        validate_on_save = True


class WikiModuleCreate(BaseModel):
    # used for creating a new wiki module endpoint
    topic: str
    identity: str
    target_audience: str
    model: str
