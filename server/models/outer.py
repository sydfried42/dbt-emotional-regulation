from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from . import db

class Outer(db.Model, SerializerMixin):
    __tablename__ = 'outers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    middle_id = db.Column(db.Integer, db.ForeignKey('middles.id'), nullable=False)
    core_id = db.Column(db.Integer, db.ForeignKey('cores.id'))

    # relationships
    middle = db.relationship('Middle', back_populates='outer_emotions')
    core = db.relationship('Core', back_populates='outers')

    # serialize rules
    serialize_rules = ['-middle.outer_emotions', '-core.outers']

    def __repr__(self):
        return f"<Outer Emotion {self.name}>"