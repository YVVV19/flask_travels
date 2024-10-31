from sqlmodel import select, delete
import asyncio
from flask import (
    render_template,
    redirect,
    url_for,
    request
)
from . import (
    Departure,
    Film,
    app,
    Config
)

@app.get("/films")
async def films():
    with Config.SESSION.begin() as session:
        smth = select(Film)
        films = Config.SESSION.scalars(smth).all()
        return await render_template(
            "index.html",
            films=[Film(
                id=x.id,
                name=x.name,
                desc=x.desc,
                departure=x.departure,
                price=x.price,
            )
            for x in films
            ],
        )
    

@app.post("/films")
async def create_film():
    form = await request.form
    if form:
        with Config.SESSION.begin() as session:
            film = Film(
                **form,
                price="150.00"
            )
            Config.SESSION.add_all(film)
    return redirect(url_for("film"))


@app.get("/films/<int:index>/details")
async def film_details(index:int):
    await asyncio.sleep(1)

    return "Hello world"


@app.get("/films/<int:index>/delete")
async def delete_films(index: int):
    return await render_template("delete_film.html", index=index,)


@app.post("/films/delete")
async def delete_film():
    film_id = await request.form.get("film_id")
    if film_id:
        with Config.SESSION.begin() as session:
            Config.SESSION.exec(delete(Film).where(Film.id == film_id))