# app/models/article.py

from datetime import datetime, timezone
from app.extensions import db
from sqlalchemy.orm import relationship

class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    article_title = db.Column(db.String(150), nullable=False)
    article_body = db.Column(db.Text, nullable=False)
    article_image = db.Column(db.String(30), default='default_article_image.jpg', nullable=False)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship("User", back_populates="articles")

    def __repr__(self):
        return f"<Article {self.article_title}>"

    def to_dict(self):
        return {
            'id': self.id,
            'article_title': self.article_title,
            'article_body': self.article_body,
            'date_created': self.date_created.isoformat(),
            'user_id': self.user_id
        }
        
    def from_dict(self, data):
        for field in ['article_title', 'article_body', 'user_id']:
            if field in data:
                setattr(self, field, data[field])
        return self
    