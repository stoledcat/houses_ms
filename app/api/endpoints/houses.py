from fastapi import APIRouter

houses_router = APIRouter(prefix="/houses", tags=["houses"])


@houses_router.get("/")
async def houses():
    return {"message": "Дома"}


@houses_router.get("/{house_id}")
async def house_detail(house_id: int):
    return {"message": f"Дом {house_id}"}
