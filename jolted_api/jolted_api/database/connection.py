from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from jolted_api.models import WikiModule, NotebookModule

client = AsyncIOMotorClient("mongodb://localhost:27017")


async def setup_database():
    await init_beanie(database=client.db_name, document_models=[WikiModule, NotebookModule])
