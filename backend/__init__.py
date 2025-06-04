from flask import Flask
from .models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.config.Config')
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    return app
