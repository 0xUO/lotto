from application import app
from flask import request, jsonify
from random import choice

prizes = ['£50', '£70', '£100']

@app.route('/prize', methods=['GET'])
def prize():
    prize = choice(prizes)
    return jsonify(prize=prize)

def prize():
    if lottoDraw + lottoDraw2 > 60:
        prize == '£50'
    else:
        prize == '£100'
    return jsonift(prize=prize)