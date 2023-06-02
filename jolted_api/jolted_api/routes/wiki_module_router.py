from fastapi import APIRouter, HTTPException
from jolted_api.models.wiki_module import WikiModule, WikiModuleInDB, WikiModuleCreate
from jolted_mod import create_wiki_module
from jolted_api.services import create_and_save_wiki_module, get_all_wiki_modules, get_wiki_module_by_id, update_wiki_module_by_id, delete_wiki_module_by_id
from pydantic import BaseModel, ValidationError
from jolted_api.models import PyObjectId
from bson import ObjectId

wiki_module_router = APIRouter()


@wiki_module_router.post("/create")
async def api_create_wiki_module(wiki_request: WikiModuleCreate):
    try:
        return await create_and_save_wiki_module(wiki_request)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))


@wiki_module_router.get("/get_all")
async def api_get_all_wiki_modules():
    try:
        return await get_all_wiki_modules()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@wiki_module_router.put("/update/{wiki_module_id}")
async def api_update_wiki_module(wiki_module_id: str, wiki_content: str):
    updated_wiki_module = await update_wiki_module_by_id(wiki_module_id, wiki_content)
    if not updated_wiki_module:
        raise HTTPException(status_code=404, detail="WikiModule not found")
    return updated_wiki_module


@wiki_module_router.delete("/delete/{wiki_module_id}")
async def api_delete_wiki_module(wiki_module_id: str):
    response = await delete_wiki_module_by_id(wiki_module_id)
    if not response:
        raise HTTPException(status_code=404, detail="WikiModule not found")
    return response


@wiki_module_router.get("/get_by_id/{wiki_module_id}")
async def api_get_wiki_module_by_id(wiki_module_id: str):
    wiki_module = await get_wiki_module_by_id(wiki_module_id)
    if not wiki_module:
        raise HTTPException(status_code=404, detail="WikiModule not found")
    return wiki_module
