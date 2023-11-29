from flask import Flask, request, jsonify
from flask_cors import CORS
import file
import uuid
from bkt import checkSkill
import content

app = Flask(__name__)
CORS(app)

@app.route('/create-user', methods=['PUT'])
def create_user():
    id = uuid.uuid4()
    data = request.get_json()
    file.saveUser(list(data.values()), id)
    return jsonify({'id': str(file.saveUser(list(data.values()), id))})

@app.route('/check-login', methods=['POST'])
def check_login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    print(file.checkUser(email, password))
    
    return jsonify({'authenticated': file.checkUser(email, password)})

@app.route('/get-scores', methods=['GET'])
def get_scores():
    data = request.get_json()
    return file.getScore(data['id'])

@app.route('/process-score', methods=['PUT'])
def process_score():
    data = request.get_json()
    id = data['id']
    operation = data['operation']
    answerList = data['answerList']
    
    updateScore = checkSkill(answerList, file.getScore(id)[operation], (len(answerList) / 100), 0.3, 0.2)
    
    return file.appendScore(id, operation, updateScore)

@app.route('/get-question', methods=['GET'])
def get_question():
    data = request.get_json()
    operation = data['operation']
    question = content.getQuestion(operation)
    
    return question # example: ('$22+16=$', '$38$')


if __name__ == '__main__':
    app.run(debug=True)