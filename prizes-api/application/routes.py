from application import app
from flask import request, jsonify

prizes = dict()

@app.route('/prize', methods=['POST'])
def prize():