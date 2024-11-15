from flask import Flask
from backend.routes import api_bp, signup_bp
from backend.extensions import db, jwt
from backend.models import User, Question, Answer

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:contraseña@localhost/tu_base_de_datos'
    app.config['SECRET_KEY'] = 'tu_clave_secreta'
    app.config['JWT_SECRET_KEY'] = 'clave_jwt_secreta'

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(api_bp)
    app.register_blueprint(signup_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
