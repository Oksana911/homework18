from flask_restx import Resource, Namespace
from app.dao.model.genre import genre_schema, genres_schema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres)


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id: int):
        movie = genre_service.get_one(genre_id)
        return genre_schema.dump(movie), 200
