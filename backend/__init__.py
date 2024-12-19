from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from .routes import api_bp, signup_bp
from .config import Config
from .extensions import db, jwt, migrate
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError


def create_app():
    app = Flask(__name__)

    # Carga configuración
    app.config.from_object(Config)

    # Inicializa extensiones
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Crea las tablas necesarias si no existen
    with app.app_context():
        db.create_all()

    # Registra los Blueprints
    app.register_blueprint(api_bp)
    app.register_blueprint(signup_bp)

    # Manejo de errores personalizados
    @app.errorhandler(NoAuthorizationError)
    def no_token_manage(error):
        return jsonify({'Mensaje': 'Necesitas un token para acceder', 'Error': str(error)}), 401

    @app.errorhandler(InvalidHeaderError)
    def invalid_token_manage(error):
        return jsonify({'Mensaje': 'Token inválido o mal formado', 'Error': str(error)}), 422

    @jwt.expired_token_loader
    def expired_token_manage(jwt_header, jwt_payload):
        return jsonify({'Mensaje': 'El token ha expirado', 'Error': 'token_expired'}), 401

    return app
