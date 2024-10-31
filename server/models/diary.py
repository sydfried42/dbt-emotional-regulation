from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from . import db

class Diary(db.Model, SerializerMixin):
    __tablename__ = 'diaries'

    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False)
    prompting_event_one = db.Column(db.String, nullable=False)
    belief = db.Column(db.String, nullable=False)
    prompting_event_two = db.Column(db.String, nullable=True)

    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    vulnerability_id = db.Column(db.Integer, db.ForeignKey('vulnerabilities.id'))
    biology_id = db.Column(db.Integer, db.ForeignKey('biology.id'))
    physiology_id = db.Column(db.Integer, db.ForeignKey('physiology.id'))
    primary_emotion_id = db.Column(db.Integer, db.ForeignKey('outers.id'))
    secondary_emotion_id = db.Column(db.Integer, db.ForeignKey('outers.id'), nullable=True)

    # relationships
    user = db.relationship('User', back_populates='diaries')
    vulnerability = db.relationship('Vulnerability')
    biology = db.relationship('Biology')
    physiology = db.relationship('Physiology')
    primary_emotion = db.relationship('Outer', foreign_keys=[primary_emotion_id])
    secondary_emotion = db.relationship('Outer', foreign_keys=[secondary_emotion_id])

    # serialize rules
    serialize_rules = [
        '-user.diaries',
        '-vulnerability.diaries',
        '-biology.diaries',
        '-physiology.diaries',
        '-primary_emotion.middle',
        '-secondary_emotion.middle',
        '-primary_emotion.core',
        '-secondary_emotion.core'
    ]

    def __repr__(self):
        return f"<Diary {self.date_time}>"