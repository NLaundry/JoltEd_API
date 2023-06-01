from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from jolted_mod import create_notebook_module, create_wiki_module, create_curriculum

app = FastAPI()


class CurriculumData(BaseModel):
    topics: List[str]
    subtopics: List[str]


@app.post("/create_notebook_module")
async def api_create_notebook_module(topic: str, identity: Optional[str] = 'professor of computer science',
                                     target_audience: Optional[str] = 'first year computer science students',
                                     model: Optional[str] = 'gpt-3.5-turbo'):
    return await create_notebook_module(topic, identity, target_audience, model)


@app.post("/create_wiki_module")
async def api_create_wiki_module(topic: str, identity: Optional[str] = 'professor of computer science',
                                 target_audience: Optional[str] = 'first year computer science students',
                                 model: Optional[str] = 'gpt-3.5-turbo'):
    return await create_wiki_module(topic, identity, target_audience, model)


@app.post("/create_curriculum")
async def api_create_curriculum(curriculum_data: CurriculumData, identity: Optional[str] = 'Professor of Computer Science',
                                target_audience: Optional[str] = 'first year computer science students',
                                model: Optional[str] = 'gpt-3.5-turbo'):
    return await create_curriculum(curriculum_data.dict(), identity, target_audience, model)
