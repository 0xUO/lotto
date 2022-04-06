from application import app, db
from application.models import Results
from flask import render_template
import requests

@app.route('/')
def index():
    lottoDraw = requests.get('http://lotto-api:5000/get-draw')
    lottoDraw2 = requests.get('http://lotto-api:5000/get-draw2')
    prizes = requests.get('http://prize-api:5000/prize', json=lottoDraw.json(), json=lottoDraw2.json())
    db.session.add(Results(lottoDraw.json()["lotto"],lottoDraw2.json()["lotto"], prize.json()["prize"]))
    db.session.commit()
    results = Results.query.all()

    return render_template('index.html', results = results)