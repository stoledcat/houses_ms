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


@houses_router.get(
    "/",
    response_model=List[HouseItemSchema],
    summary="Возвращает дома",
    description="Возвращает список активных домов",
)
async def get_houses(
    session: DBSessionDep,
    min_price: Optional[int] = Query(None, ge=0, title="Минимальная ацена"),
    max_price: Optional[int] = Query(None, ge=0, title="Максимальная цена"),
    order_by: Optional[SortField] = Query("id", title="Поля сортировки", description="Допустимые значения: id, price, name"),
    order: Optional[SortOrder] = Query("asc", title="Порядок сортировки", description="Допустимые значения: asc, desc"),
    search: Optional[str] = Query(None, min_length=3, description="Поисковый запрос (минимум 3 символа)"),
):
    """
    Функция выводит данные всех активных объявлений
    """

    return crud_house.get_filtered_active_houses(
        session, min_price=min_price, max_price=max_price, order_by=order_by, order=order
    )


@houses_router.get("/{house_id}", response_model=HouseDetailSchema, summary="Возвращает дом")
async def get_house(session: DBSessionDep, house_id: int):
    """
    Возвращает подробную информацию о доме:
       - **id**: идентификатор
       - **name**: название дома
       - **description**: короткое описание дома
       - **price**: цена дома в рублях
    """
    house = crud_house.get_house(session, house_id)

    if not house:
        raise HTTPException(status_code=404, detail="House not found")

    return house
