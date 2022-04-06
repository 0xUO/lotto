from application import db

class Results(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    magicNumber = db.Column(db.String(1))
    lottoDraw = db.Colum(db.String(20))
    prize = db.Column(db.String(6))
    def __str__(self):
        return f"{self.lottoDraw} is the Draw, Your Magic Number is {magicNumber} which wins you a Bonus of {self.prize} !!!"