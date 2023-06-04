from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from jolted_api.database import setup_database
from jolted_api.routes import notebook_router, wiki_module_router

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
app.include_router(wiki_module_router, prefix="/wiki_module", tags=["wiki_module"])


@app.on_event("startup")
async def startup_event() -> None:
    """This function is an asynchronous event handler for the "startup" event in FastAPI.

    When the FastAPI application starts up, this function will be called automatically.
    It initializes the database by calling the setup_database function asynchronously.

    Returns:
        None
    """
    await setup_database()
