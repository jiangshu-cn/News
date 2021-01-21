from flask import Blueprint

news_index = Blueprint("index", __name__, url_prefix="", template_folder="templates")


@news_index.route('/')
def index():
    return '<h1>Hello, this is admin blueprint</h1>'
