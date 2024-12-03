from app import create_app
from models import db

from models.core import Core
from models.middle import Middle
from models.outer import Outer
from models.vulnerability import Vulnerability
from models.biology import Biology
from models.physiology import Physiology

# Create the Flask app using the factory function
app = create_app()

# Open the app context so that database operations can occur
with app.app_context():
    # Clear existing data from relevant tables only
    db.session.query(Vulnerability).delete()
    db.session.query(Biology).delete()
    db.session.query(Physiology).delete()
    db.session.query(Core).delete()
    db.session.query(Middle).delete()
    db.session.query(Outer).delete()

    # Helper functions to create data for each table
    def create_core_emotions():
        cores = [
            Core(id=1, name="Joy"),
            Core(id=2, name="Trust"),
            Core(id=3, name="Fear"),
            Core(id=4, name="Surprise"),
            Core(id=5, name="Sadness"),
            Core(id=6, name="Disgust"),
            Core(id=7, name="Anger"),
            Core(id=8, name="Anticipation"),
        ]
        return cores

    def create_middle_emotions():
        middles = [
            Middle(id=1, name="Optimism", core_id=1),
            Middle(id=2, name="Love", core_id=1),
            Middle(id=3, name="Ecstasy", core_id=1),
            Middle(id=4, name="Acceptance", core_id=2),
            Middle(id=5, name="Admiration", core_id=2),
            Middle(id=6, name="Approval", core_id=2),
            Middle(id=7, name="Apprehension", core_id=3),
            Middle(id=8, name="Worry", core_id=3),
            Middle(id=9, name="Terror", core_id=3),
            Middle(id=10, name="Amazement", core_id=4),
            Middle(id=11, name="Distraction", core_id=4),
            Middle(id=12, name="Wonder", core_id=4),
            Middle(id=13, name="Grief", core_id=5),
            Middle(id=14, name="Sorrow", core_id=5),
            Middle(id=15, name="Disappointment", core_id=5),
            Middle(id=16, name="Loathing", core_id=6),
            Middle(id=17, name="Contempt", core_id=6),
            Middle(id=18, name="Revulsion", core_id=6),
            Middle(id=19, name="Annoyance", core_id=7),
            Middle(id=20, name="Hostility", core_id=7),
            Middle(id=21, name="Fury", core_id=7),
            Middle(id=22, name="Interest", core_id=8),
            Middle(id=23, name="Vigilance", core_id=8),
            Middle(id=24, name="Excitement", core_id=8),
        ]
        return middles

    def create_outer_emotions():
        outers = [
            Outer(id=1, name="Hopefulness", middle_id=1),
            Outer(id=2, name="Enthusiasm", middle_id=1),
            Outer(id=3, name="Affection", middle_id=2),
            Outer(id=4, name="Compassion", middle_id=2),
            Outer(id=5, name="Delight", middle_id=3),
            Outer(id=6, name="Bliss", middle_id=3),
            Outer(id=7, name="Tolerance", middle_id=4),
            Outer(id=8, name="Openness", middle_id=4),
            Outer(id=9, name="Respect", middle_id=5),
            Outer(id=10, name="Appreciation", middle_id=5),
            Outer(id=11, name="Endorsement", middle_id=6),
            Outer(id=12, name="Support", middle_id=6),
            Outer(id=13, name="Nervousness", middle_id=7),
            Outer(id=14, name="Unease", middle_id=7),
            Outer(id=15, name="Anxiety", middle_id=8),
            Outer(id=16, name="Concern", middle_id=8),
            Outer(id=17, name="Panic", middle_id=9),
            Outer(id=18, name="Horror", middle_id=9),
            Outer(id=19, name="Astonishment", middle_id=10),
            Outer(id=20, name="Shock", middle_id=10),
            Outer(id=21, name="Confusion", middle_id=11),
            Outer(id=22, name="Disorientation", middle_id=11),
            Outer(id=23, name="Curiosity", middle_id=12),
            Outer(id=24, name="Fascination", middle_id=12),
            Outer(id=25, name="Despair", middle_id=13),
            Outer(id=26, name="Melancholy", middle_id=13),
            Outer(id=27, name="Misery", middle_id=14),
            Outer(id=28, name="Regret", middle_id=14),
            Outer(id=29, name="Disillusionment", middle_id=15),
            Outer(id=30, name="Frustration", middle_id=15),
            Outer(id=31, name="Abhorrence", middle_id=16),
            Outer(id=32, name="Detestation", middle_id=16),
            Outer(id=33, name="Scorn", middle_id=17),
            Outer(id=34, name="Disdain", middle_id=17),
            Outer(id=35, name="Nausea", middle_id=18),
            Outer(id=36, name="Repulsion", middle_id=18),
            Outer(id=37, name="Irritation", middle_id=19),
            Outer(id=38, name="Agitation", middle_id=19),
            Outer(id=39, name="Hatred", middle_id=20),
            Outer(id=40, name="Resentment", middle_id=20),
            Outer(id=41, name="Rage", middle_id=21),
            Outer(id=42, name="Wrath", middle_id=21),
            Outer(id=43, name="Curiosity", middle_id=22),
            Outer(id=44, name="Inquisitiveness", middle_id=22),
            Outer(id=45, name="Alertness", middle_id=23),
            Outer(id=46, name="Watchfulness", middle_id=23),
            Outer(id=47, name="Enthusiasm", middle_id=24),
            Outer(id=48, name="Eagerness", middle_id=24),
        ]
        return outers

    def create_vulnerabilities():
        vulnerabilities = [
            Vulnerability(id=1, name="Physical Illness"),
            Vulnerability(id=2, name="Eating"),
            Vulnerability(id=3, name="Drugs"),
            Vulnerability(id=4, name="Sleep"),
            Vulnerability(id=5, name="Exercise"),
        ]
        return vulnerabilities

    def create_biology():
        biologies = [
            Biology(id=1, name="Heart Rate Changes"),
            Biology(id=2, name="Blood Pressure Fluctuations"),
            Biology(id=3, name="Respiratory Changes"),
            Biology(id=4, name="Muscle Tension"),
            Biology(id=5, name="Gastrointestinal Distress"),
            Biology(id=6, name="Hormonal Imbalance"),
            Biology(id=7, name="Immune System Suppression"),
            Biology(id=8, name="Skin Reactions"),
            Biology(id=9, name="Changes in Body Temperature"),
            Biology(id=10, name="Chest Tightness or Pressure"),
        ]
        return biologies

    def create_physiology():
        physiologies = [
            Physiology(id=1, name="Facial Expressions"),
            Physiology(id=2, name="Posture"),
            Physiology(id=3, name="Flushed Face"),
            Physiology(id=4, name="Gestures and Body Movements"),
            Physiology(id=5, name="Vocal Tone and Pitch"),
            Physiology(id=6, name="Eye Movements"),
            Physiology(id=7, name="Impulsive Speech"),
            Physiology(id=8, name="Trembling or Shaking"),
            Physiology(id=9, name="Breathing Patterns"),
            Physiology(id=10, name="Quick or Sudden Movements"),
        ]
        return physiologies

    # Add the seed data for the specified models
    db.session.add_all(create_vulnerabilities())
    db.session.add_all(create_biology())
    db.session.add_all(create_physiology())
    db.session.add_all(create_core_emotions())
    db.session.add_all(create_middle_emotions())
    db.session.add_all(create_outer_emotions())

    # Commit the session to save changes to the database
    db.session.commit()

    print("Database seeded successfully!")
