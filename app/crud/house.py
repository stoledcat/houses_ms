from sqlmodel import Session, asc, desc, select, or_
from typing import Sequence

from app.models import House


def get_active_houses(session: Session) -> Sequence[House]:
    stmt = select(House).where(House.active)
    return session.exec(stmt).all()


def get_filtered_active_houses(session: Session, search=None, min_price=None, max_price=None, order_by="id", order="asc"):
    stmt = select(House).where(House.active)

    if search:
        # stmt = stmt.where(House.description.icontains(search) | House.name.icontains(search))
        stmt = stmt.where(or_(House.description.icontains(search), House.name.icontains(search)))

    if min_price:
        stmt = stmt.where(House.price >= min_price)

    if max_price:
        stmt = stmt.where(House.price <= max_price)

    ordering = desc if order == "desc" else asc
    stmt = stmt.order_by(ordering(order_by))

    return session.exec(stmt).all()


def get_house(session: Session, house_id: int):
    stmt = select(House).where(House.active).where(House.id == house_id)
    return session.exec(stmt).first()
