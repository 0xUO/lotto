from application import app
from flask import request, jsonify
from random import choice

prizes = dict(1 = '£100', 2 = '£200', 3 = '£300', 4 = '£400', 5 = '£500')

@app.route('/prize', methods=['POST'])
def prize():
    draw_json = request.get_json()
    draw = draw_json["lotto"]
    return jsonify(prize=prizes[draw])