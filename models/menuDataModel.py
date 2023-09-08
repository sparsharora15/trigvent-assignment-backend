from .db import db  

class MenuData(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.Text, nullable=False)
    rule = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    params = db.Column(db.JSON, nullable=False)

    def __init__(self, label, rule, type, params):
        self.label = label
        self.rule = rule
        self.type = type
        self.params = params
    