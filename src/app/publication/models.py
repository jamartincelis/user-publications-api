"""
Librería con los modelos a utilizar para representar las entidades de la
base de datos.
"""
from .. import db
import datetime
from datetime import datetime
from sqlalchemy import DateTime

class Publication(db.Model):
    """
    Representa una publicación del usuario.
    """    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(60))
    status = db.Column(db.String(20), nullable=False)
    time = db.Column(DateTime, default=datetime.now)    
    user = db.Column(
        db.ForeignKey('user.id'),
        default=lambda: get_current_user().id,
        nullable=False,
    )    
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, title, description, priority, status, user):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.user = user

    def __repr__(self):
        return f'<Publication: {self.title}>'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'user': self.user
        }


