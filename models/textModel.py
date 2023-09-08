from .db import db

class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __init__(self, content):
        self.content = content