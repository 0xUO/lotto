from application import db

class Results(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    magicNumber = db.Column(db.String(6))
    lottoDraw = db.Column(db.String(20))
    prize = db.Column(db.Integer)
    def __str__(self):
        return f"{self.lottoDraw} is the lottery draw!, Your Magic Number is {self.magicNumber} which wins you a {self.prize} pounds bonus !!!"