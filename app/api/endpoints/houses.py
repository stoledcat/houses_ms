from fastapi import APIRouter

houses_router = APIRouter(prefix="/houses", tags=["houses"])


@houses_router.get("/")
async def root():
    return {"message": "Hello World"}


@houses_router.get("/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
