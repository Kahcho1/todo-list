from application import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(30), nullable=True)
    comp = db.Column(db.Boolean, nullable=False, default=False)