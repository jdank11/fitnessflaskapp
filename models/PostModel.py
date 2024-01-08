from datetime import datetime

from app import db

class PostModel(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    workout = db.Column(db.String, nullable = False)
    weight = db.Column(db.String, nullable = False)
    timestamp = db.Column(db.String, default = datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    def __repr__(self):
        return f'<Post: {self.title}>'

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()