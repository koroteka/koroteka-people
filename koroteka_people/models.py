from __future__ import annotations
from typing import Annotated, Optional
from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base

str255 = Annotated[str, 255]
str64 = Annotated[str, 64]


class Person(Base):
    __tablename__ = "persons"

    person_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    person_name: Mapped[str255]
    person_birthday: Mapped[Optional[date]]
    person_appeal: Mapped[Optional[str64]]
    notes: Mapped[str]

    contacts: Mapped[list[Contact]] = relationship(back_populates="person")


class ContactType(Base):
    __tablename__ = "contact_types"

    contact_type_id: Mapped[int] = mapped_column(primary_key=True)
    contact_type_name: Mapped[str64]
    contact_type_engl_name: Mapped[str64]


class Contact(Base):
    __tablename__ = "contacts"

    contact_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    person_id: Mapped[int] = mapped_column(ForeignKey("persons.person_id"))
    contact_type_id: Mapped[int] = mapped_column(
        ForeignKey("contact_types.contact_type_id")
    )
    contact_text: Mapped[str255]

    person: Mapped[Person] = relationship(back_populates="contacts")
    contact_type: Mapped[ContactType] = relationship()
