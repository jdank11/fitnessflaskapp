
from app import db

class Workouts(db.Model):

    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key = True)
    exercise = db.Column(db.String, nullable = False)
    weight = db.Column(db.String, nullable = False)
    reps = db.Column(db.String, nullable = False)
    notes = db.Column(db.String, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    user = db.relationship('UserModel', back_populates = 'posts')

    def __repr__(self):
        return f'<Post: {self.exercise}{self.weight}{self.reps}{self.notes}>'

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()