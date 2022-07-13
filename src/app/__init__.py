from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

def create_app():
    app = Flask(__name__)
    # se carga la configuración por defecto
    app.config.from_object("config.Config")
    # por ahora se carga la configuración de desarrollo
    app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .user.resources.routes import initialize_user_routes
        from .publication.resources.routes import initialize_publication_routes
        initialize_user_routes(api)
        initialize_publication_routes(api)
        app.register_blueprint(api_bp)

        return app