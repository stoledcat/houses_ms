from fastapi import APIRouter
from fastapi import HTTPException
from app.data import houses_list
from app.schemas.house import HouseDetailSchema, HouseItemSchema
from app.api.deps import DBSessionDep
from fastapi import Query

from typing import List, Optional, Literal

from sqlmodel import text

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

    print(session.exec(text("SELECT 1")))

    houses = [h for h in houses_list if h["active"]]

    if min_price is not None:
        houses = [h for h in houses if h["price"] >= min_price]

    if max_price is not None:
        houses = [h for h in houses if h["price"] <= max_price]

    # Сортировка
    reverse = order == "desc"
    houses.sort(key=lambda h: h[order_by], reverse=reverse)

    return houses


@houses_router.get("/{house_id}", response_model=HouseDetailSchema)
async def get_house_detail(house_id: int):
    for house in houses_list:
        if house["id"] == house_id:
            return house
    raise HTTPException(status_code=404, detail="House not found")
