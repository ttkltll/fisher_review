from flask import Flask

from app.web.book import web


def creat_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.register_blueprint(web)
    return app
