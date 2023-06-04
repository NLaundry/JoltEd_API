from bson import ObjectId
from jolted_mod import create_wiki_module
from typing import List
from jolted_api.exceptions import (
    WikiModuleDatabaseError,
    WikiModuleNotFoundError,
    BeanieExceptionNames,
)

from jolted_api.exceptions import WikiModuleNotFoundError, WikiModuleDatabaseError
from jolted_api.models.types import PyObjectId
from jolted_api.models.wiki_module import WikiModule, WikiModuleCreate


async def create_and_save_wiki_module(wiki_request: WikiModuleCreate) -> WikiModule:
    """
    Create and save a WikiModule in the database.

    Args:
        wiki_request (WikiModuleCreate): An instance of WikiModuleCreate containing the data
                                         needed to create a new WikiModule.

    Returns:
        WikiModule: The newly created WikiModule instance.
    """
    try:
        holder = await create_wiki_module(**wiki_request.dict())
        # TODO: need to create errors int he jolted_mod package
        wiki_module = WikiModule(name=wiki_request.topic, content=holder)
        await wiki_module.save()
        return wiki_module
    except Exception as e:
        exception_name = e.__class__.__name__
        match exception_name:
            case BeanieExceptionNames.DOCUMENT_WAS_NOT_SAVED.value:
                raise WikiModuleDatabaseError(
                    message=BeanieExceptionNames.DOCUMENT_WAS_NOT_SAVED.value
                )
            case BeanieExceptionNames.DOCUMENT_ALREADY_CREATED.value:
                raise WikiModuleDatabaseError(
                    message="Unable to create and save wiki module"
                )
            case _:
                raise Exception(e)


async def get_all_wiki_modules() -> List[WikiModule]:
    """
    Get a list of all wiki modules.

    Returns:
        list: A list of all wiki modules in the database.
    """
    try:
        return await WikiModule.all().to_list()
    except Exception as e:
        exception_name = e.__class__.__name__
        match exception_name:
            case BeanieExceptionNames.COLLECTION_WAS_NOT_INITIALIZED.value:
                raise WikiModuleDatabaseError(
                    message=BeanieExceptionNames.COLLECTION_WAS_NOT_INITIALIZED.value
                )
            case _:
                raise Exception(e)


async def get_wiki_module_by_id(wiki_module_id: str) -> WikiModule:
    """
    Get a wiki module by its ID.

    Args:
        wiki_module_id (str): The ID of the wiki module to retrieve.

    Returns:
        WikiModule: The wiki module with the specified ID.

    Raises:
        WikiModuleNotFoundError: If the wiki module with the given ID is not found.
    """
    wiki_module_id = PyObjectId(wiki_module_id)
    try:
        wiki_module = await WikiModule.get(wiki_module_id)
        if not wiki_module:
            raise WikiModuleNotFoundError(wiki_module_id)
        return wiki_module
    except Exception as e:
        exception_name = e.__class__.__name__
        match exception_name:
            case BeanieExceptionNames.DOCUMENT_NOT_FOUND.value:
                raise WikiModuleNotFoundError(wiki_module_id)
            case BeanieExceptionNames.COLLECTION_WAS_NOT_INITIALIZED.value:
                raise WikiModuleDatabaseError(
                    message=BeanieExceptionNames.COLLECTION_WAS_NOT_INITIALIZED.value
                )
            case _:
                raise Exception(e)


async def update_wiki_module_by_id(
    wiki_module_id: str, wiki_content: str
) -> WikiModule:
    """
    Update the content of a wiki module by its ID.

    Args:
        wiki_module_id (str): The ID of the wiki module to update.
        wiki_content (str): The new content for the wiki module.

    Returns:
        WikiModule: The updated wiki module.

    Raises:
        WikiModuleNotFoundError: If the wiki module with the given ID is not found.
        WikiModuleDatabaseError: If the save operation fails.
    """
    wiki_module_id = PyObjectId(ObjectId(wiki_module_id))
    wiki_module = await WikiModule.get(wiki_module_id)
    if not wiki_module:
        raise WikiModuleNotFoundError(wiki_module_id)
    updated_wiki_module = wiki_module.copy(update={"content": wiki_content})
    try:
        return await updated_wiki_module.replace()
    except Exception as e:
        exception_name = e.__class__.__name__
        match exception_name:
            case BeanieExceptionNames.DOCUMENT_WAS_NOT_SAVED.value:
                raise WikiModuleDatabaseError(message=BeanieExceptionNames.DOCUMENT_WAS_NOT_SAVED.value)
            case BeanieExceptionNames.WRONG_DOCUMENT_UPDATE_STRATEGY.value:
                raise WikiModuleDatabaseError(message=BeanieExceptionNames.WRONG_DOCUMENT_UPDATE_STRATEGY.value)
            case BeanieExceptionNames.COLLECTION_WAS_NOT_INITIALIZED.value:
                raise WikiModuleDatabaseError(message=BeanieExceptionNames.COLLECTION_WAS_NOT_INITIALIZED.value)
            case _:
                raise Exception(e)


async def delete_wiki_module_by_id(wiki_module_id: str) -> WikiModule:
    """
    Delete a wiki module by its ID.

    Args:
        wiki_module_id (str): The ID of the wiki module to delete.

    Returns:
        dict: A dictionary containing a message indicating the wiki module has been deleted.

    Raises:
        WikiModuleNotFoundError: If the wiki module with the given ID is not found.
    """
    wiki_module_id = PyObjectId(ObjectId(wiki_module_id))
    wiki_module = await WikiModule.get(wiki_module_id)
    if not wiki_module:
        raise WikiModuleNotFoundError(wiki_module_id)
    try:
        return await wiki_module.delete()
    except Exception as e:
        exception_name = e.__class__.__name__
        match exception_name:
            case BeanieExceptionNames.DOCUMENT_NOT_FOUND.value:
                raise WikiModuleNotFoundError(wiki_module_id)
            case BeanieExceptionNames.COLLECTION_WAS_NOT_INITIALIZED.value:
                raise WikiModuleDatabaseError(
                    message=BeanieExceptionNames.COLLECTION_WAS_NOT_INITIALIZED.value
                )
            case _:
                raise Exception(e)
