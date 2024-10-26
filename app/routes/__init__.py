from .. import app
from ..db import (
    Departure,
    Film,
    Config,
)
from sqlmodel import select
from flask import render_template

Config.mock_up()

def get_departure_list():
    return Config.SESSION.scalars(select(Departure)).all()


def get_film_list(departure: Departure | int | None = None):
    if departure:
        if isinstance(departure, Departure):
            Config.SESSION.scalars(select(Film).where(Film.departure == departure)).all()
        elif isinstance(departure, int):
            Config.SESSION.scalars(select(Film).where(Film.departure_id == departure)).all()
    return Config.SESSION.scalars(select(Film)).all()


@app.get("/")
def index():
    url="https://http.cat/images/"
    items = [f"{url}{x}.jpg" for x in [101, 404, 417, 402, 420, 500, 400, 510]]
    return render_template("index.html", items=items, departures=get_departure_list())


from . import departure