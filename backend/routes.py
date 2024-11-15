from flask import Blueprint, request, jsonify
from .extensions import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .models import User, Question, Answer, Tag, Comment

api_bp = Blueprint('api', __name__)
signup_bp = Blueprint('signup', __name__)

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se recibieron datos"}), 400

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Correo y contraseña requeridos"}), 400

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify({
            "message": "Inicio de sesión exitoso",
            "access_token": access_token,
            "user": {"name": user.name, "email": user.email}
        }), 200

    return jsonify({"error": "Credenciales inválidas"}), 401



@api_bp.route('/dashboard/questions/<int:question_id>', methods=['GET'])
@jwt_required()
def get_question(question_id):
    try:
        question = Question.query.get(question_id)
        if not question:
            return jsonify({"error": "Pregunta no encontrada"}), 404

        return jsonify({
            'id': question.id,
            'title': question.title,
            'content': question.content,
            'user': question.user.username,
            'created_at': question.created_at.isoformat(),
            'comments': [
                {'user': comment.user.username, 'content': comment.content, 'created_at': comment.created_at.isoformat()}
                for comment in question.comments
            ],
            'tags': [tag.name for tag in question.tags]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route('/dashboard/questions/<int:question_id>/comments', methods=['POST'])
@jwt_required()
def add_comment(question_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    content = data.get('content')

    if not content:
        return jsonify({'error': 'El contenido del comentario es requerido'}), 400

    question = Question.query.get(question_id)
    if not question:
        return jsonify({'error': 'Pregunta no encontrada'}), 404

    comment = Comment(content=content, user_id=user_id, question_id=question_id)
    db.session.add(comment)
    db.session.commit()

    return jsonify({'message': 'Comentario agregado exitosamente'}), 201


@api_bp.route('/dashboard/questions/<int:question_id>/tags', methods=['POST'])
@jwt_required()
def add_tag(question_id):
    data = request.get_json()
    tag_name = data.get('tag')

    if not tag_name:
        return jsonify({'error': 'El nombre del tag es requerido'}), 400

    question = Question.query.get(question_id)
    if not question:
        return jsonify({'error': 'Pregunta no encontrada'}), 404

    tag = Tag.query.filter_by(name=tag_name).first()
    if not tag:
        tag = Tag(name=tag_name)
        db.session.add(tag)

    question.tags.append(tag)
    db.session.commit()

    return jsonify({'message': 'Tag agregado exitosamente'}), 201


@api_bp.route('/dashboard/questions', methods=['POST'])
@jwt_required()
def create_question():
    user_id = get_jwt_identity()
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({'error': 'Título y contenido son requeridos'}), 400

    try:
        question = Question(title=title, content=content, user_id=user_id)
        db.session.add(question)
        db.session.commit()

        return jsonify({'message': 'Pregunta creada exitosamente', 'id': question.id}), 201
    except Exception as e:
        return jsonify({'error': f'Error interno del servidor: {str(e)}'}), 500

@api_bp.route('/dashboard/questions', methods=['GET'])
@jwt_required()
def get_all_questions():
    questions = Question.query.all()
    result = []
    for question in questions:
        result.append({
            'id': question.id,
            'title': question.title,
            'content': question.content,
            'user': question.user.username,
            'created_at': question.created_at.isoformat()
        })
    return jsonify(result), 200



@signup_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    username = data.get('username')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if not all([name, username, email, password, confirm_password]):
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    if password != confirm_password:
        return jsonify({"error": "Las contraseñas no coinciden"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "El correo ya está registrado"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "El nombre de usuario ya está en uso"}), 400

    new_user = User(name=name, username=username, email=email, phone=phone)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuario registrado con éxito"}), 201