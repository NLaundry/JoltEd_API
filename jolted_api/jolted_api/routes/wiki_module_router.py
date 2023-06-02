from fastapi import APIRouter, Body
from jolted_api.models.wiki_module import WikiModule
from jolted_mod import create_wiki_module
from starlette.requests import Request
from pydantic import BaseModel


class WikiModuleCreate(BaseModel):
    topic: str
    identity: str
    target_audience: str
    model: str


wiki_module_router = APIRouter()


@wiki_module_router.post("/create")
async def api_create_wiki_module(wiki_module: WikiModuleCreate):
    return await create_wiki_module(**wiki_module.dict())
