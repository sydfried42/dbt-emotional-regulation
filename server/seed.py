from models import db, Core, Middle, Outer, Vulnerability, Biology, Physiology  # Import the database instance and models
from app import app  # Import the Flask app to set the app context for the database

def seed_emotions():
    # Core emotions
    core_emotions = [
        {"id": 1, "name": "Joy"},
        {"id": 2, "name": "Trust"},
        {"id": 3, "name": "Fear"},
        {"id": 4, "name": "Surprise"},
        {"id": 5, "name": "Sadness"},
        {"id": 6, "name": "Disgust"},
        {"id": 7, "name": "Anger"},
        {"id": 8, "name": "Anticipation"}
    ]

    # Populate Core emotions
    for core in core_emotions:
        if not Core.query.get(core['id']):
            db.session.add(Core(**core))

    # Commit core emotions before adding middle emotions
    db.session.commit()

    # Middle emotions with core_id references
    middle_emotions = [
        {"id": 1, "name": "Optimism", "core_id": 1},
        {"id": 2, "name": "Love", "core_id": 1},
        {"id": 3, "name": "Ecstasy", "core_id": 1},
        {"id": 4, "name": "Acceptance", "core_id": 2},
        {"id": 5, "name": "Admiration", "core_id": 2},
        {"id": 6, "name": "Approval", "core_id": 2},
        {"id": 7, "name": "Apprehension", "core_id": 3},
        {"id": 8, "name": "Worry", "core_id": 3},
        {"id": 9, "name": "Terror", "core_id": 3},
        {"id": 10, "name": "Amazement", "core_id": 4},
        {"id": 11, "name": "Distraction", "core_id": 4},
        {"id": 12, "name": "Wonder", "core_id": 4},
        {"id": 13, "name": "Grief", "core_id": 5},
        {"id": 14, "name": "Sorrow", "core_id": 5},
        {"id": 15, "name": "Disappointment", "core_id": 5},
        {"id": 16, "name": "Loathing", "core_id": 6},
        {"id": 17, "name": "Contempt", "core_id": 6},
        {"id": 18, "name": "Revulsion", "core_id": 6},
        {"id": 19, "name": "Annoyance", "core_id": 7},
        {"id": 20, "name": "Hostility", "core_id": 7},
        {"id": 21, "name": "Fury", "core_id": 7},
        {"id": 22, "name": "Interest", "core_id": 8},
        {"id": 23, "name": "Vigilance", "core_id": 8},
        {"id": 24, "name": "Excitement", "core_id": 8}
    ]

    # Populate Middle emotions
    for middle in middle_emotions:
        if not Middle.query.get(middle['id']):
            db.session.add(Middle(**middle))

    db.session.commit()

    # Outer emotions with middle_id references
    outer_emotions = [
        {"id": 1, "name": "Hopefulness", "middle_id": 1},
        {"id": 2, "name": "Enthusiasm", "middle_id": 1},
        {"id": 3, "name": "Affection", "middle_id": 2},
        {"id": 4, "name": "Compassion", "middle_id": 2},
        {"id": 5, "name": "Delight", "middle_id": 3},
        {"id": 6, "name": "Bliss", "middle_id": 3},
        {"id": 7, "name": "Tolerance", "middle_id": 4},
        {"id": 8, "name": "Openness", "middle_id": 4},
        {"id": 9, "name": "Respect", "middle_id": 5},
        {"id": 10, "name": "Appreciation", "middle_id": 5},
        {"id": 11, "name": "Endorsement", "middle_id": 6},
        {"id": 12, "name": "Support", "middle_id": 6},
        {"id": 13, "name": "Nervousness", "middle_id": 7},
        {"id": 14, "name": "Unease", "middle_id": 7},
        {"id": 15, "name": "Anxiety", "middle_id": 8},
        {"id": 16, "name": "Concern", "middle_id": 8},
        {"id": 17, "name": "Panic", "middle_id": 9},
        {"id": 18, "name": "Horror", "middle_id": 9},
        {"id": 19, "name": "Astonishment", "middle_id": 10},
        {"id": 20, "name": "Shock", "middle_id": 10},
        {"id": 21, "name": "Confusion", "middle_id": 11},
        {"id": 22, "name": "Disorientation", "middle_id": 11},
        {"id": 23, "name": "Curiosity", "middle_id": 12},
        {"id": 24, "name": "Fascination", "middle_id": 12},
        {"id": 25, "name": "Despair", "middle_id": 13},
        {"id": 26, "name": "Melancholy", "middle_id": 13},
        {"id": 27, "name": "Misery", "middle_id": 14},
        {"id": 28, "name": "Regret", "middle_id": 14},
        {"id": 29, "name": "Disillusionment", "middle_id": 15},
        {"id": 30, "name": "Frustration", "middle_id": 15},
        {"id": 31, "name": "Abhorrence", "middle_id": 16},
        {"id": 32, "name": "Detestation", "middle_id": 16},
        {"id": 33, "name": "Scorn", "middle_id": 17},
        {"id": 34, "name": "Disdain", "middle_id": 17},
        {"id": 35, "name": "Nausea", "middle_id": 18},
        {"id": 36, "name": "Repulsion", "middle_id": 18},
        {"id": 37, "name": "Irritation", "middle_id": 19},
        {"id": 38, "name": "Agitation", "middle_id": 19},
        {"id": 39, "name": "Hatred", "middle_id": 20},
        {"id": 40, "name": "Resentment", "middle_id": 20},
        {"id": 41, "name": "Rage", "middle_id": 21},
        {"id": 42, "name": "Wrath", "middle_id": 21},
        {"id": 43, "name": "Curiosity", "middle_id": 22},
        {"id": 44, "name": "Inquisitiveness", "middle_id": 22},
        {"id": 45, "name": "Alertness", "middle_id": 23},
        {"id": 46, "name": "Watchfulness", "middle_id": 23},
        {"id": 47, "name": "Enthusiasm", "middle_id": 24},
        {"id": 48, "name": "Eagerness", "middle_id": 24}
    ]

    # Populate Outer emotions
    for outer in outer_emotions:
        if not Outer.query.get(outer['id']):
            db.session.add(Outer(**outer))

    db.session.commit()


def seed_vulnerabilities():
    vulnerabilities = [
        {"id": 1, "name": "Physical Illness"},
        {"id": 2, "name": "Eating"},
        {"id": 3, "name": "Drugs"},
        {"id": 4, "name": "Sleep"},
        {"id": 5, "name": "Exercise"}
    ]

    # Populate Vulnerabilities
    for vulnerability in vulnerabilities:
        if not Vulnerability.query.get(vulnerability['id']):
            db.session.add(Vulnerability(**vulnerability))

    db.session.commit()

def seed_biology():
    biology_factors = [
        {"id": 1, "name": "Heart Rate Changes"},
        {"id": 2, "name": "Blood Pressure Fluctuations"},
        {"id": 3, "name": "Respiratory Changes"},
        {"id": 4, "name": "Muscle Tension"},
        {"id": 5, "name": "Gastrointestinal Distress"},
        {"id": 6, "name": "Hormonal Imbalance"},
        {"id": 7, "name": "Immune System Suppression"},
        {"id": 8, "name": "Skin Reactions"},
        {"id": 9, "name": "Changes in Body Temperature"},
        {"id": 10, "name": "Chest Tightness or Pressure"}
    ]

    # Populate Biology
    for bio in biology_factors:
        if not Biology.query.get(bio['id']):
            db.session.add(Biology(**bio))

    db.session.commit()

def seed_physiology():
    physiology_factors = [
        {"id": 1, "name": "Facial Expressions"},
        {"id": 2, "name": "Posture"},
        {"id": 3, "name": "Flushed Face"},
        {"id": 4, "name": "Gestures and Body Movements"},
        {"id": 5, "name": "Vocal Tone and Pitch"},
        {"id": 6, "name": "Eye Movements"},
        {"id": 7, "name": "Impulsive Speech"},
        {"id": 8, "name": "Trembling or Shaking"},
        {"id": 9, "name": "Breathing Patterns"},
        {"id": 10, "name": "Quick or Sudden Movements"}
    ]

    # Populate Physiology
    for phys in physiology_factors:
        if not Physiology.query.get(phys['id']):
            db.session.add(Physiology(**phys))

    db.session.commit()
    

# Run this function when you want to seed the database
if __name__ == "__main__":
    with app.app_context():  # Create an app context to access the database
        db.create_all()  # Ensure tables are created
        seed_emotions()
        seed_vulnerabilities()
        seed_biology()
        seed_physiology()
        print("Database seeded successfully.")
