from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from . import db

class Core(db.Model, SerializerMixin):
    __tablename__ = 'cores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # relationships
    middle_emotions = db.relationship('Middle', back_populates='core')
    outers = db.relationship('Outer', back_populates='core')

    # serialize rules
    serialize_rules = ['-middle_emotions.core_id', '-outers.core_id']

    def __repr__(self):
        return f"<Core Emotion {self.name}>"