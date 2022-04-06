from application import app
from flask import jsonify
from random import sample
import random

@app.route('/get-draw', methods=['GET'])
def lottoDraw():
    lottoDraw = random.sample(range(10, 45), 5)
    return jsonify(lottoDraw=lottoDraw)