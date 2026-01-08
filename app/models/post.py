# app/models/post.py
from datetime import datetime
from app.extensions import db
from sqlalchemy.orm import relationship

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = relationship('User', back_populates='posts')

    def __repr__(self):
        return f"<Post {self.title}>"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'author_id': self.author_id
        }
        
    def from_dict(self, data):
        for field in ['title', 'content', 'author_id']:
            if field in data:
                setattr(self, field, data[field])
        return self
    