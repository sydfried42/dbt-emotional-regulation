from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from . import db

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    # relationships
    diaries = db.relationship('Diary', back_populates='user')

    # serialize rules
    serialize_rules = ['-diaries.user']

    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError("Please enter a valid email address")
        return address

    def __repr__(self):
        return f"<User {self.email}>"