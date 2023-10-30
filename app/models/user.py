from app import db
from bcrypt import hashpw, gensalt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)

    def set_password(self, password):
        salt = gensalt()
        hashed_password = hashpw(password.encode('utf-8'), salt)

        self.password_hash = hashed_password.decode('utf-8')

    def check_password(self, password):
        return hashpw(password.encode('utf-8'), self.password_hash.encode('utf-8')) == self.password_hash.encode('utf-8')
