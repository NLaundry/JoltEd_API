from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from typing import List
from jolted_api.exceptions import WikiModuleDatabaseError

from jolted_api.models.wiki_module import WikiModuleCreate, WikiModule
from jolted_api.services import (
    create_and_save_wiki_module,
    delete_wiki_module_by_id,
    get_all_wiki_modules,
    get_wiki_module_by_id,
    update_wiki_module_by_id,
)

wiki_module_router = APIRouter()


@wiki_module_router.post("/create")
async def api_create_wiki_module(wiki_request: WikiModuleCreate) -> WikiModule:
    """
    Creates a new wiki module and saves it to the database.

    Args:
        wiki_request (WikiModuleCreate): The wiki module creation request object.

    Raises:
        HTTPException: If there is a validation error or a database error.

    Returns:
        WikiModule: The created wiki module.
    """
    try:
        return await create_and_save_wiki_module(wiki_request)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except WikiModuleDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@wiki_module_router.get("/get_all")
async def api_get_all_wiki_modules() -> List[WikiModule]:
    """
    Retrieves all wiki modules from the database.

    Raises:
        HTTPException: If there is a database error.

    Returns:
        List[WikiModule]: A list of all wiki modules.
    """
    try:
        return await get_all_wiki_modules()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@wiki_module_router.put("/update/{wiki_module_id}")
async def api_update_wiki_module(wiki_module_id: str, wiki_content: str) -> WikiModule:
    """
    Updates a wiki module's content by its ID.

    Args:
        wiki_module_id (str): The ID of the wiki module to update.
        wiki_content (str): The new content for the wiki module.

    Raises:
        HTTPException: If the wiki module is not found or there is a database error.

    Returns:
        WikiModule: The updated wiki module.
    """
    try:
        updated_wiki_module = await update_wiki_module_by_id(wiki_module_id, wiki_content)
        if not updated_wiki_module:
            raise HTTPException(status_code=404, detail="WikiModule not found")
    except WikiModuleDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return updated_wiki_module


@wiki_module_router.delete("/delete/{wiki_module_id}")
async def api_delete_wiki_module(wiki_module_id: str) -> WikiModule:
    """
    Deletes a wiki module by its ID.

    Args:
        wiki_module_id (str): The ID of the wiki module to delete.

    Raises:
        HTTPException: If the wiki module is not found or there is a database error.

    Returns:
        WikiModule: The deleted wiki module.
    """
    try:
        wiki_module_deleted = await delete_wiki_module_by_id(wiki_module_id)
        if not wiki_module_deleted:
            raise HTTPException(status_code=404, detail="WikiModule not found")
        return wiki_module_deleted
    except WikiModuleDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@wiki_module_router.get("/get_by_id/{wiki_module_id}")
async def api_get_wiki_module_by_id(wiki_module_id: str) -> WikiModule:
    """
    Returns a wiki module gotten by its ID.

    Args:
        wiki_module_id (str): The ID of the wiki module to retrieve.

    Raises:
        HTTPException: If the wiki module is not found or there is a database error.

    Returns:
        WikiModule: The wiki module as a JSON object.
    """
    try:
        wiki_module = await get_wiki_module_by_id(wiki_module_id)
        if not wiki_module:
            raise HTTPException(status_code=404, detail="WikiModule not found")
        return wiki_module
    except WikiModuleDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))

