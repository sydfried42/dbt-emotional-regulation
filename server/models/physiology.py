from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from . import db

class Physiology(db.Model, SerializerMixin):
    __tablename__ = 'physiologies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # relationships
    diaries = db.relationship('Diary', back_populates='physiology')

    # serialize rules
    serialize_rules = ['-diaries.physiology_id']

    def __repr__(self):
        return f"<Physiology {self.name}>"