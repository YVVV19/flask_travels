import time 
import random
from sqlmodel import Field, Relationship
from .helpers import AutoincrementID
from .departure import Departure
from decimal import Decimal


class Film(AutoincrementID, table=True):
    name:str
    desc:str
    departure:Departure = Relationship(back_populates="films")
    departure_id: int = Field(foreign_key=f"{Departure.__tablename__}.id")
    price: Decimal


    @staticmethod
    def mock_data(departures: list[Departure]) -> list["Film"]:
        random.seed(time.time())
        return[
            Film(
                name=f"Тур №{film}({departure.name})",
                desc="Тестовий набір даних",
                departure=departure,
                price=Decimal(f"{random.random()*100}").quantize(Decimal("1.00")),
            )
            for film in range(2)
            for departure in departures
        ]
