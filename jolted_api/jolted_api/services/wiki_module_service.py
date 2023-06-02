from jolted_api.models.wiki_module import WikiModule, WikiModuleInDB, WikiModuleCreate
from jolted_api.models.types import PyObjectId
from jolted_mod import create_wiki_module
from bson import ObjectId


async def create_and_save_wiki_module(wiki_request: WikiModuleCreate):
    holder = await create_wiki_module(**wiki_request.dict())
    wiki_module = WikiModule(name=wiki_request.topic, content=holder)
    wiki_module_db = WikiModuleInDB(**wiki_module.dict())
    await wiki_module_db.save()
    return wiki_module


async def get_all_wiki_modules():
    return await WikiModuleInDB.all().to_list()


async def get_wiki_module_by_id(wiki_module_id: str):
    wiki_module_id = PyObjectId(wiki_module_id)
    wiki_module = await WikiModuleInDB.get(wiki_module_id)
    return wiki_module


async def update_wiki_module_by_id(wiki_module_id: str, wiki_content: str):
    wiki_module_id = PyObjectId(ObjectId(wiki_module_id))
    wiki_module = await WikiModuleInDB.get(wiki_module_id)
    updated_wiki_module = wiki_module.copy(
        update={"content": wiki_content})
    return await updated_wiki_module.save()

async def delete_wiki_module_by_id(wiki_module_id: str):
    wiki_module_id = PyObjectId(ObjectId(wiki_module_id))
    wiki_module = await WikiModuleInDB.get(wiki_module_id)
    await wiki_module.delete()
    return {"message": f"WikiModule with ID {wiki_module_id} has been deleted"}
