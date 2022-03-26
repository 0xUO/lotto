from application import app
from flask import request, jsonify
from random import choice

prizes = ['£50', '£70', '£100']

@app.route('/prizes', methods=['POST'])
def prize():
    prize = choice(prizes)
    return jsonify(prize=prize)