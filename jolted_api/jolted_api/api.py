from fastapi import FastAPI
from starlette.requests import Request
from pydantic import BaseModel
from typing import List, Optional
from jolted_mod import create_notebook_module, create_wiki_module, create_curriculum
from fastapi.middleware.cors import CORSMiddleware

from jolted_api.routes import notebook_router
from jolted_api.routes import wiki_module_router

from jolted_api.database import setup_database

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

app.include_router(notebook_router, prefix="/notebook", tags=["notebook"])
app.include_router(wiki_module_router,
                   prefix="/wiki_module", tags=["wiki_module"])


@app.on_event("startup")
async def startup_event():
    await setup_database()




