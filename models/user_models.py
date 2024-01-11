
from app import db

from werkzeug.security import generate_password_hash, check_password_hash


followers = db.Table( 'followers',
  db.Column('follower_id', db.Integer, db.ForeignKey('users.id')),
  db.Column('followed_id', db.Integer, db.ForeignKey('users.id'))  
)

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique= True)
    email = db.Column(db.String(75), nullable = False, unique= True)
    password_hash = db.Column(db.String(250), nullable = False)
    first_name =  db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    followed = db.relationship('UserModel',
                            secondary = 'followers',
                            primaryjoin = followers.c.follower_id == id,
                            secondaryjoin = followers.c.followed_id == id,
                            backref = db.backref('followers', lazy = 'dynamic')
                            )
    posts = db.relationship('PostModel',back_populates ='user', lazy='dynamic', cascade= 'all, delete')


    def __repr__(self):
        return f'<User: {self.username}>'

    def commit(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, user_dict):
        for k, v in user_dict.items():
            if k != 'password':
                setattr(self, k, v)
            else:
                setattr(self, 'password_hash', generate_password_hash(v))