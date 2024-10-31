DBT Emotional Regulation Diary

FRONTEND:

1. Landing page is a login that asks for email and password
2. MEDITATION PAGE - full screen https://www.youtube.com/watch?v=OMlf71t2oV0
3. EVALUATION PAGE
    a. prompting event 1: attention/awareness 
    b. interpretation
    c. preexisting vulnerabilities
        1. sick?
        2. eating?
        3. drugs?
        4. sleep?
        5. exercised?
    d. internal expressions/changes
    e. external expressions/changes
    f. emotion name
        1. inner
        2. middle
        3. outer
    g. after effects
    h. prompting event 2: attention/awareness
4. DIARY PAGE - Each diary entry will be displayed in a drop down accordion style way with a date/time and face on the outside and all entry information on the inside.

Stretch goal is to have answers fit to a scale so the diary can have an easy view


BACKEND:

STEP 1: CREATE BACKEND

This will be an 8 model/table structure:


USER
id = db.Column(db.Integer, primary_key=True)
Email = str
Password = str
Diary_id = id

DIARY
id = db.Column(db.Integer, primary_key=True)
Date/time = date/time
Prompting_event_one = str
Belief = str
Vulnerability_id = id
Biology_id = id
Physiology_id = id
Primary_emotion_id = tertiary_id
Secondary_emotion_id = tertiary_id || null
Prompting_event_two = str || null


VULNERABILITY 
id = db.Column(db.Integer, primary_key=True)
Physical_illness = 1
Eating = 2
Drugs = 3
Sleep = 4
Exercise = 5

BIOLOGY
id = db.Column(db.Integer, primary_key=True)
Heart Rate Changes = 1
Blood Pressure Fluctuations = 2
Respiratory Changes = 3
Muscle Tension = 4
Gastrointestinal Distress = 5
Hormonal Imbalance = 6
Immune System Suppression  = 7
Skin Reactions = 8
Changes in Body Temperature = 9
Chest Tightness or Pressure = 10

PHYSIOLOGY
id = db.Column(db.Integer, primary_key=True)
Facial Expressions = 1
Posture = 2
Flushed Face = 3
Gestures and Body Movements = 4
Vocal Tone and Pitch = 5
Eye Movements = 6
Impulsive Speech = 7
Trembling or Shaking = 8
Breathing Patterns = 9
Quick or Sudden Movements = 10

CORE EMOTION
id = db.Column(db.Integer, primary_key=True)
Joy = 1
Trust = 2
Fear = 3
Surprise = 4
Sadness = 5
Disgust = 6
Anger = 7
Anticipation = 8

MIDDLE EMOTION
id = db.Column(db.Integer, primary_key=True)
Optimism = 1, core_id 1
Love = 2, core_id 1
Ecstasy = 3, core_id 1
Acceptance = 4, core_id 2
Admiration = 5, core_id 2
Approval = 6, core_id 2
Apprehension = 7, core_id 3
Worry = 8, core_id 3
Terror = 9, core_id 3
Amazement = 10, core_id 4
Distraction = 11, core_id 4
Wonder = 12, core_id 4
Grief = 13, core_id 5
Sorrow = 14, core_id 5
Disappointment = 15, core_id 5
Loathing = 16, core_id 6
Contempt = 17, core_id 6
Revulsion = 18, core_id 6
Annoyance = 19, core_id 7
Hostility = 20, core_id 7
Fury = 21, core_id 7
Interest = 22, core_id 8
Vigilance = 23, core_id 8
Excitement = 24, core_id 8


TERTIARY EMOTION
id = db.Column(db.Integer, primary_key=True)
Hopefulness = 1, middle_id 1
Enthusiasm = 2, middle_id 1
Affection = 3, middle_id 2
Compassion = 4, middle_id 2
Delight = 5, middle_id 3
Bliss = 6, middle_id 3
Tolerance = 7, middle_id 4
Openness = 8, middle_id 4
Respect = 9, middle_id 5
Appreciation = 10, middle_id 5
Endorsement = 11, middle_id 6
Support = 12, middle_id 6
Nervousness = 13, middle_id 7
Unease = 14, middle_id 7
Anxiety = 15, middle_id 8
Concern = 16, middle_id 8
Panic = 17, middle_id 9
Horror = 18, middle_id 9
Astonishment = 19, middle_id 10
Shock = 20, middle_id 10
Confusion = 21, middle_id 11
Disorientation = 22, middle_id 11
Curiosity = 23, middle_id 12
Fascination = 24, middle_id 12
Despair = 25, middle_id 13
Melancholy = 26, middle_id 13
Misery = 27, middle_id 14
Regret = 28, middle_id 14
Disillusionment = 29, middle_id 15
Frustration = 30, middle_id 15
Abhorrence = 31, middle_id 16
Detestation = 32, middle_id 16
Scorn = 33, middle_id 17
Disdain = 34, middle_id 17
Nausea = 35, middle_id 18
Repulsion = 36, middle_id 18
Irritation = 37, middle_id 19
Agitation = 38, middle_id 19
Hatred = 39, middle_id 20
Resentment = 40, middle_id 20
Rage = 41, middle_id 21
Wrath = 42, middle_id 21
Curiosity = 43, middle_id 22
Inquisitiveness = 44, middle_id 22
Alertness = 45, middle_id 23
Watchfulness = 46, middle_id 23
Enthusiasm = 47, middle_id 24
Eagerness = 48, middle_id 24



