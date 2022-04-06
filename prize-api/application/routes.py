from application import app
from flask import request, jsonify

prizes = dict(one='100', two='200', three='300', four='400', five='500')

@app.route('/prize', methods=['POST'])
def prize():
    magicNumber_json = request.get_json()
    magicNumber = magicNumber_json["magicNumber"]
    return jsonify(prize=prizes[magicNumber])