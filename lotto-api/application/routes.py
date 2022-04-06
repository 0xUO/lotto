from application import app
from flask import jsonify
from random import choice

magicNumbers = ['one', 'two', 'three', 'four', 'five']

@app.route('/get-magicNumber', methods=['GET'])
def magicNumber():
    magicNumber = choice(magicNumbers)
    return jsonify(magicNumber=magicNumber)