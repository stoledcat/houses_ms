from fastapi import APIRouter
from fastapi import HTTPException
from app.schemas.house import HouseDetailSchema, HouseItemSchema
from app.api.deps import DBSessionDep
from app.crud import house as crud_house
from fastapi import Query

from typing import List, Optional, Literal


houses_router = APIRouter(prefix="/houses", tags=["houses"])

SortField = Literal["id", "price", "name"]
SortOrder = Literal["asc", "desc"]


@houses_router.get("/", response_model=List[HouseItemSchema])
async def get_houses(
    session: DBSessionDep,
    min_price: Optional[int] = Query(None, ge=0),
    max_price: Optional[int] = Query(None, ge=0),
    order_by: Optional[SortField] = Query("id"),
    order: Optional[SortOrder] = Query("asc"),
):

    return crud_house.get_filtered_active_houses(
        session, min_price=min_price, max_price=max_price, order_by=order_by, order=order
    )


@houses_router.get("/{house_id}", response_model=HouseDetailSchema)
async def get_house(session: DBSessionDep, house_id: int):
    house = crud_house.get_house(session, house_id)
    if not house:
        raise HTTPException(status_code=404, detail="House not found")

    return house
