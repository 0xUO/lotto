from application import app
from flask import jsonify
import random

@app.route('/get-draw', methods=['GET'])
def lottoDraw():
    lottoDraw = random.sample(range(1, 45), 5)
        return jsonify(lottoDraw=lottoDraw)