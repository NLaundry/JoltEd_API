from fastapi import FastAPI
from starlette.requests import Request
from pydantic import BaseModel
from typing import List, Optional
from jolted_mod import create_notebook_module, create_wiki_module, create_curriculum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  # Your frontend server origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allowing all methods
    allow_headers=["*"],
)


class CurriculumData(BaseModel):
    topics: List[str]
    subtopics: List[str]


@app.post("/create_notebook_module")
async def api_create_notebook_module(request: Request):
    body = await request.json()
    return await create_notebook_module(**body)


@app.post("/create_wiki_module")
async def api_create_wiki_module(request: Request):
    body = await request.json()
    return await create_wiki_module(**body)


@app.post("/create_curriculum")
async def api_create_curriculum(curriculum_data: CurriculumData, identity: Optional[str] = 'Professor of Computer Science',
                                target_audience: Optional[str] = 'first year computer science students',
                                model: Optional[str] = 'gpt-3.5-turbo'):
    return await create_curriculum(curriculum_data.dict(), identity, target_audience, model)
