from sqlmodel import asc, desc, select, or_
from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import House


def get_active_houses(session: AsyncSession) -> Sequence[House]:
    stmt = select(House).where(House.active)
    return session.execute(stmt).all()


async def get_filtered_active_houses(session: AsyncSession, filters=None, order_by="id", order="asc"):
    stmt = select(House).where(House.active)

    if filters.search:
        # stmt = stmt.where(House.description.icontains(search) | House.name.icontains(search))
        stmt = stmt.where(or_(House.description.icontains(filters.search), House.name.icontains(filters.search)))

    if filters.min_price is not None:
        stmt = stmt.where(House.price >= filters.min_price)

    if filters.max_price is not None:
        stmt = stmt.where(House.price <= filters.max_price)

    ordering = desc if order == "desc" else asc
    stmt = stmt.order_by(ordering(order_by))

    result = await session.execute(stmt)
    return result.scalars().all()


async def get_house(session: AsyncSession, house_id: int):
    stmt = select(House).where(House.active).where(House.id == house_id)
    result = await session.execute(stmt)
    return result.scalars().first()
