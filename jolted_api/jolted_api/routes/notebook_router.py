from fastapi import APIRouter, Body
from jolted_api.models.notebook_module import NotebookModule
from jolted_mod import create_notebook_module
from starlette.requests import Request
from pydantic import BaseModel


class NotebookModuleCreate(BaseModel):
    topic: str
    identity: str
    target_audience: str
    model: str


notebook_router = APIRouter()


@notebook_router.post("/create")
async def api_create_notebook_module(notebook_module: NotebookModuleCreate):
    return await create_notebook_module(**notebook_module.dict())
