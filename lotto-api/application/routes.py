from application import app
from flask import jsonify
from random import choice

lottoGen = ['1', '2', '3', '4', '5']

@app.route('/get-magicnum', methods=['GET'])
def magicNumber():
    magicNum = choice(lottoGen)
    return jsonify(magicNum=magicNum)