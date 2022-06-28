from flask import Flask
from flask_restx import Api
from app.config import Config
from app.dao.model.movie import Movie
from app.setup_db import db
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns


# функция создания основного объекта application
def create_app(config: Config):  # привязываем конфиги
    application = Flask(__name__)
    application.config.from_object(config)  # привязываем конфиги
    application.app_context().push()  # применяет конфигурацию во все будущие компоненты
    return application


# функция конфигурации приложения
def configure_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


# функция загрузки новых данных в таблицы
# def load_data():
#     movie_1 = Movie(id=21, title="Kolobok1", description='Укатился колобок', trailer='http', year=1800, rating=10,
#                     genre_id=1, director_id=1)
#
#
#     db.drop_all()
#     db.create_all()
#     with db.session.begin():
#         db.session.add(movie_1)


if __name__ == "__main__":
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    # load_data()
    app.run(host="localhost", port=5000)
