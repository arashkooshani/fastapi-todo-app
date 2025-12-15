from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks.routes import router as tasks_routes

tags_metadata=[
{
    "name":"tasks",
    "description":"operations related to tasks."
}
]

@asynccontextmanager
async def lifespan(app: FastAPI) :
    print("Application Startup!")
    yield
    print("Application ShutDown!")





app = FastAPI(lifespan=lifespan,openapi_tags=tags_metadata)
app.include_router(tasks_routes)
