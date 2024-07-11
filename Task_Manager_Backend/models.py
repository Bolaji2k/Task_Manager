from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'Task'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    status = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text)
    created_date = db.Column(db.Date)
    completed_date = db.Column(db.Date)
    due_date = db.Column(db.Date)

    def __repr__(self) -> str:
        return f'{self.title}'
    
    def serialize(self):
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'created_date': self.created_date.isoformat() if self.created_date else None,
            'completed_date': self.completed_date.isoformat() if self.completed_date else None,
            'due_date': self.due_date.isoformat() if self.due_date else None,
        }
        
        return data