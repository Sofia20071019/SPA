from flask import Flask
from flask_migrate import Migrate
from api.app.config.setting import Config
from api.app.database.database import db, bcrypt, jwt
from api.app.routes.auth_routes import auth_bp

migrate = Migrate()
import api.app.models

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(
        auth_bp,
        url_prefix = "/api"
    )

    return app