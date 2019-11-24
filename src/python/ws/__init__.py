from flask import Flask


def create_app(config_filename="src.python.ws.conf.BaseConfig"):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    from src.python.ws.home import home

    app.register_blueprint(home)

    return app


