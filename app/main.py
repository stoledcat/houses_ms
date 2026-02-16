from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.endpoints.houses import houses_router
from app.db.init import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(houses_router)
