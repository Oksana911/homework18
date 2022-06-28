from flask_restx import Resource, Namespace
from app.container import director_service
from app.dao.model.director import director_schema, directors_schema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_dir = director_service.get_all()
        return directors_schema.dump(all_dir)


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id: int):
        dir = director_service.get_one(director_id)
        return director_schema.dump(dir), 200
