from sqlmodel import Session, create_engine

from app.core.config import settings

connect_args = {}
engine = create_engine(settings.database_url, connect_args=connect_args, echo=settings.DB_ECHO)


def get_session():
    with Session(engine) as session:
        yield session
