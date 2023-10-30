from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import secrets

db = SQLAlchemy()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = secrets.token_urlsafe(12)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)
    jwt.init_app(app)

    from app.views.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
