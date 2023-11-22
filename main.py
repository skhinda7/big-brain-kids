from flask import Flask, request, jsonify
import file
import uuid
from bkt import checkSkill

app = Flask(__name__)

@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Simar Khinda",
        "email": "email.com",
    }

    extra = request.args.get('extra')
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200

@app.route('/create-user', methods=['PUT'])
def create_user():
    id = uuid.uuid4()
    data = request.get_json()
    file.saveUsers(list(data.values()), id)
    return str(id), 200

@app.route('/find-user', methods=['GET'])
def find_user():
    data = request.get_json()
    retrieved_user = file.getUser(data['id'])
    return ('Welcome ' + retrieved_user['FirstName'] + ' ' + retrieved_user['LastName']), 201

@app.route('/get-scores', methods=['GET'])
def get_scores():
    data = request.get_json()
    return file.getScore(data['id'])

@app.route('/process-score', methods=['POST'])
def process_score():
    data = request.get_json()
    id = data['id']
    operation = data['operation']
    answerList = data['answerList']
    
    updateScore = checkSkill(answerList, file.getScore(id)[operation], (len(answerList) / 100), 0.3, 0.2)
    
    return file.appendScore(id, operation, updateScore)
    

if __name__ == '__main__':
    app.run(debug=True)