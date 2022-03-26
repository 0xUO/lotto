from application import app, db
from application.models import Results
from flask import render_template
import requests

@app.route('/')
def index():
    lottoDraw = requests.get('http://lotto-api:5000/get-draw')
    prizes = requests.post('http://prize-api:5000/prize', json=lottoDraw.json())
    db.session.add(Results(lottoDraw.json()["lotto"], prize.json()["prize"]))
    db.session.commit()
    results = Results.query.all()

    return render_template('index.html', results = results)