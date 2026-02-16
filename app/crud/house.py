from app.models.house import House
from sqlmodel import Session, select, desc, asc


def get_active_houses(session: Session):
    stmt = select(House).where(House.active)
    return session.exec(stmt).all()