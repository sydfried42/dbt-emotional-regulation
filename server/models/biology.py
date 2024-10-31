from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from . import db

class Biology(db.Model, SerializerMixin):
    __tablename__ = 'biology'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # relationships
    diaries = db.relationship('Diary', back_populates='biology')

    # serialize rules
    serialize_rules = ['-diaries.biology_id']

    def __repr__(self):
        return f"<Biology {self.name}>"