from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped
from .helpers import AutoincrementID


class Departure(AutoincrementID, table=True):
    name:str
    desc:str
    films:list["Film"] = Relationship(back_populates="departure")

    @staticmethod
    def mock_data():
        return[
            Departure(name=f"напрям №{x}", desc="something")
            for x in range(2)
        ]