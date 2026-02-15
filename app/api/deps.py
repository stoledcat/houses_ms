from sqlmodel import Session
from fastapi import Depends
from typing import Annotated
from app.db.session import get_session

DBSessionDep = Annotated[Session, Depends(get_session)]
