from .models import User
from flask_jwt_extended import create_access_token
from datetime import timedelta

def user_register(name, email, phone, password):
    existent_user = User.query.filter_by(email=email).first()
    if existent_user:
        return {'Error': 'El usuario ya está registrado'}, 403

    new_user = User(name=name, email=email, phone=phone)
    new_user.password_hash(password)
    new_user.save()

    return {'status': 'Usuario registrado', 'email': email, 'phone': phone}, 200

def user_login(email, password):
    existent_user = User.query.filter_by(email=email).first()
    if not existent_user:
        return {'status': 'El correo o la contraseña son incorrectos'}, 500
    
    if existent_user.check_password(password=password):
        caducidad = timedelta(minutes=2)
        access_token = create_access_token(identity=existent_user.name, expires_delta=caducidad)
        return {'status': 'Sesión iniciada', 'token': access_token}, 200
    
    return {'status': 'El correo o la contraseña son incorrectos'}, 400
