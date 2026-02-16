from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from app.db.session import get_session

DBSessionDep = Annotated[Session, Depends(get_session)]
