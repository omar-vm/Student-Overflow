from .extensions import db
from datetime import datetime
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash

class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class User(BaseModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)

    answers = db.relationship('Answer', back_populates='user', lazy=True)
    questions = db.relationship('Question', back_populates='user', lazy=True)
    comments = db.relationship('Comment', back_populates='user', lazy=True)
    answer_votes = db.relationship('AnswerVote', back_populates='user', lazy=True)
    question_votes = db.relationship('QuestionVote', back_populates='user', lazy=True)

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address, "Dirección de correo inválida"
        return address

    @validates('username')
    def validate_username(self, key, username):
        assert len(username) > 2, "El nombre de usuario debe tener más de 2 caracteres"
        return username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

class Question(BaseModel):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='questions')

    answers = db.relationship('Answer', back_populates='question', lazy=True)
    tags = db.relationship('Tag', secondary='question_tags', back_populates='questions')
    votes = db.relationship('QuestionVote', back_populates='question', lazy=True)
    comments = db.relationship('Comment', back_populates='question', lazy=True)


class Answer(BaseModel):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='answers')
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    question = db.relationship('Question', back_populates='answers')

    comments = db.relationship('Comment', back_populates='answer', lazy=True)
    votes = db.relationship('AnswerVote', back_populates='answer', lazy=True)


class Comment(BaseModel):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='comments')

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    question = db.relationship('Question', back_populates='comments')

    answer_id = db.Column(db.Integer, db.ForeignKey('answers.id'), nullable=True)
    answer = db.relationship('Answer', back_populates='comments')


class Tag(BaseModel):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    questions = db.relationship('Question', secondary='question_tags', back_populates='tags')

class AnswerVote(BaseModel):
    __tablename__ = 'answer_votes'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)  # -1 para downvote, 1 para upvote
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='answer_votes')
    answer_id = db.Column(db.Integer, db.ForeignKey('answers.id'), nullable=False)
    answer = db.relationship('Answer', back_populates='votes')

class QuestionVote(BaseModel):
    __tablename__ = 'question_votes'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)  
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='question_votes')
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    question = db.relationship('Question', back_populates='votes')


question_tags = db.Table(
    'question_tags',
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)
