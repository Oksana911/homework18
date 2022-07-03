from flask import request
from flask_restx import Resource, Namespace
from app.dao.model.movie import movie_schema, movies_schema
from app.container import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")

        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }

        all_movies = movie_service.get_all(filters)
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        new_movie = movie_service.create(req_json)
        return f'Новый фильм c id {new_movie.id} успешно добавлен в БД', 201, {
            'location': f'{movie_ns.path}/{new_movie.id}'}


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
        movie = movie_service.get_one(movie_id)
        return movie_schema.dump(movie), 200

    def put(self, movie_id: int):
        req_json = request.json
        req_json['id'] = movie_id
        movie_service.update(req_json)
        return f'Фильм с id {movie_id} обновлен', 204

    def patch(self, movie_id: int):
        req_json = request.json
        req_json['id'] = movie_id
        movie_service.update_partial(req_json)
        return f'Фильм с id {movie_id} обновлен', 204

    def delete(self, movie_id: int):
        movie_service.delete(movie_id)
        return f'Фильм с id {movie_id} удален', 204
