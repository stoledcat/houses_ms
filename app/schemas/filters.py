from typing import Optional
from fastapi import Query
from dataclasses import dataclass
from sqlmodel import or_

from app.models import House


@dataclass
class HouseFilters:
    search: Optional[str] = Query(None, min_length=3, description="Поиск по названию")
    min_price: Optional[int] = Query(None, ge=0, title="Минимальная цена")
    max_price: Optional[int] = Query(None, ge=0, title="Максимальная цена")

    def build_query(self, base_query):
        query = base_query

        if self.search:
            query = query.where(or_(House.description.icontains(self.search), House.name.icontains(self.search)))

        if self.min_price is not None:
            query = query.where(House.price >= self.min_price)

        if self.max_price is not None:
            query = query.where(House.price <= self.max_price)

        return query
