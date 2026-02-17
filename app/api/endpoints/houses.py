from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from typing import List, Optional, Literal

from app.schemas.house import HouseDetailSchema, HouseItemSchema
from app.api.deps import DBSessionDep
from app.crud import house as crud_house


houses_router = APIRouter(prefix="/houses", tags=["houses"])


SortField = Literal["id", "price", "name"]
SortOrder = Literal["asc", "desc"]


@houses_router.get("/", response_model=List[HouseItemSchema], summary="Все дома", description="Данные обо всех активных бъявления")
async def get_houses(
        session: DBSessionDep,
        min_price: Optional[int] = Query(None, ge=0, description="Минимальная цена"),
        max_price: Optional[int] = Query(None, ge=0, description="Максимальная цена"),
        order_by: Optional[SortField] = Query("id", description="Выбор поля для сортировки"),
        order: Optional[SortOrder] = Query("asc", description="Порядок сортировки")
    ):
    """
    Функция выводит данные всех активных объявлений
    """

    return crud_house.get_filtered_active_houses(session, min_price=min_price, max_price=max_price, order_by=order_by, order=order)


@houses_router.get("/{house_id}", response_model=HouseDetailSchema, summary="Информация о доме", description="Полная информация о запрошенном доме")
async def get_house(session: DBSessionDep, house_id: int):
    house = crud_house.get_house(session, house_id)

    if not house:
        raise HTTPException(status_code=404, detail="House not found")

    return house