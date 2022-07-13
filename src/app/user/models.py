"""
Librería con los modelos a utilizar para representar las entidades de la
base de datos.
"""
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """
    Representa un usuario de la base de datos.
    """    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(200))
    email = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    status = db.Column(db.String(20))

    def __init__(self, full_name, email, password, status):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.status = status


    @staticmethod
    def _generate_password_hash(password_plaintext):
        return '123456'

    def set_password(self, password_plaintext: str):
        self.password = self._generate_password_hash(password_plaintext)

    def get_id(self):
        """Return the user ID as a unicode string (`str`)."""
        return str(self.id)

    def __repr__(self):
        return f'<User: {self.email}>'

    def to_json(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email
        }

"""class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    type = db.Column(db.String(16), nullable=False)
    user_id = db.Column(
        db.ForeignKey('user.id'),
        default=lambda: get_current_user().id,
        nullable=False,
    )
    created_at = db.Column(
        db.DateTime,
        server_default=func.now(),
        nullable=False,
    )"""



