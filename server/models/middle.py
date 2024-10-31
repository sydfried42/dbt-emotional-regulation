from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from . import db

class Middle(db.Model, SerializerMixin):
    __tablename__ = 'middles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    core_id = db.Column(db.Integer, db.ForeignKey('cores.id'))

    # relationships
    core = db.relationship('Core', back_populates='middle_emotions')
    outer_emotions = db.relationship('Outer', back_populates='middle')

    # serialize rules
    serialize_rules = ['-outer_emotions.middle_id', '-core.middle_emotions']

    def __repr__(self):
        return f"<Middle Emotion {self.name}>"