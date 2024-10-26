from . import (
    app,
    Departure,
    select,
    Config,
    get_departure_list,
    index,
    get_film_list,
)
from flask import render_template, url_for


@app.get("/departure/<int:item_id>")
def departure(item_id: int):
    return render_template(
        "index.html", items=get_film_list(item_id), departures=get_departure_list()
        )
