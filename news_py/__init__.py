from flask import Flask
from news_py.controllers.news_front import news_index


def create_app():
    app = Flask(__name__)
    app.register_blueprint(news_index, url_prefix='')
    return app
