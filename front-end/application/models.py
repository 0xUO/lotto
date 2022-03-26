from application import db

class Results(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    lottoDraw = db.Column(db.String(10))
    prize = db.Column(db.String(10))
    def __str__(self):
        return f"{self.lottoDraw} is the Draw, With a Bonus of {self.prize} !!!"