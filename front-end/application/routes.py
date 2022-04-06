from application import app, db
from application.models import Results
from flask import render_template
import requests

@app.route('/')
def index():
    magicNumber = requests.get('http://lotto-api:5000/get-magicNumber')
    lottoDraw = requests.get('http://lottodraw-api:5000/get-draw')
    prize = requests.post('http://prize-api:5000/prize', json=magicNumber.json())
    db.session.add(Results(magicNumber=magicNumber.json()["magicNumber"], lottoDraw=lottoDraw.json()["lottoDraw"], prize=prize.json()["prize"]))
    db.session.commit()
    results = Results.query.all()

    return render_template('index.html', results = results)