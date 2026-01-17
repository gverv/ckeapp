# app/models/article.py

from datetime import datetime, timezone
from app.extensions import db
from sqlalchemy.orm import relationship

class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(30), default='default_article_image.jpg', nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship("User", back_populates="articles")

    def __repr__(self):
        return f"<Article {self.title}>"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at.isoformat(),
            'user_id': self.author_id
        }
        
    def from_dict(self, data):
        for field in ['title', 'body', 'user_id']:
            if field in data:
                setattr(self, field, data[field])
        return self
    