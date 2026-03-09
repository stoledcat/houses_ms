from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query
from fastapi import Request
from fastapi import Depends
from typing import List, Optional, Literal

from app.schemas.house import HouseDetailSchema, HouseItemSchema
from app.api.deps import DBSessionDep
from app.crud import house as crud_house
from app.schemas.filters import HouseFilters


houses_router = APIRouter(prefix="/houses", tags=["houses"])


SortField = Literal["id", "price", "name"]
SortOrder = Literal["asc", "desc"]


@houses_router.get(
    "",
    response_model=List[HouseItemSchema],
    summary="Возвращает дома",
    description="Возвращает список активных домов",
)
async def get_houses(
    session: DBSessionDep,
    request: Request,
    filters: HouseFilters = Depends(),
    order_by: Optional[SortField] = Query("id", title="Поля сортировки", description="Допустимые значения: id, price, name"),
    order: Optional[SortOrder] = Query("asc", title="Порядок сортировки", description="Допустимые значения: asc, desc"),
):
    """
    Функция выводит данные всех активных объявлений
    """

    redis = request.app.state.redis
    await redis.setex(name="TEST", value="TEST VALUE", time=60)

    houses = await crud_house.get_filtered_active_houses(session, filters=filters, order_by=order_by, order=order)
    return houses


@houses_router.get("/{house_id}", response_model=HouseDetailSchema, summary="Возвращает дом")
async def get_house(session: DBSessionDep, house_id: int):
    """
    Возвращает подробную информацию о доме:
       - **id**: идентификатор
       - **name**: название дома
       - **description**: короткое описание дома
       - **price**: цена дома в рублях
    """
    house = await crud_house.get_house(session, house_id)

    if not house:
        raise HTTPException(status_code=404, detail="House not found")

    return house
