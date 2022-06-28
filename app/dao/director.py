from app.dao.model.movie import Movie
from app.dao.model.genre import Genre
from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, dir_id):
        return self.session.query(Director).get(dir_id)

    def get_all(self):
        return self.session.query(Director).all()
