from typing import Annotated
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends

from .settings import settings

engine = sqlalchemy.create_engine(settings.database_url)
Base = declarative_base()


def get_session():
    with Session(engine, autocommit=False) as session:
        yield session


UseSession = Annotated[Session, Depends(get_session)]
