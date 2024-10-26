from sqlmodel import SQLModel, create_engine, Session


from .models import Departure, Film


class Config:
    ENGINE = create_engine("sqlite:///my_db.db", echo=True)
    SESSION = Session(bind=ENGINE)


    @classmethod
    def mock_up(cls):
        SQLModel.metadata.drop_all(cls.ENGINE)
        SQLModel.metadata.create_all(cls.ENGINE)

        films = Film.mock_data(Departure.mock_data())
        cls.SESSION.add_all(films)
        cls.SESSION.commit()