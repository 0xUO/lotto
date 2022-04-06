from application import app
from flask import jsonify
import random

# @app.route('/get-draw', methods=['GET'])
# def lottoDraw():
#     lottoDraw = random.sample(range(1, 20), 3)
#         return jsonify(lottoDraw=lottoDraw)

@app.route('/get-draw2', methods=['GET'])
def lottoDraw2():
    lottoDraw2 = random.sample(range(23, 40), 2)
        return jsonify(lottoDraw2=lottoDraw2)