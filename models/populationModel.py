from .db import db  

class PopulationRecord(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)

    def __init__(self, year, population):
        self.year = year
        self.population = population
0