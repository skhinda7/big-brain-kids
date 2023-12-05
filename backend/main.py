from flask import Flask, request, jsonify
from flask_cors import CORS
import file
import uuid
from bkt import checkSkill
import content

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

@app.route('/create-user', methods=['PUT'])
def create_user():
    id = uuid.uuid4()
    data = request.get_json()
    token = file.saveUser(list(data.values()), id) # data = ['First Name', 'Last Name', 'Email', 'Password', 'ID']
    return jsonify({'id': str(token)})

@app.route('/check-login', methods=['POST'])
def check_login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    validLogin = file.checkUser(email, password)

    returnValue = jsonify({'authenticated': validLogin})

    if validLogin:
        token = file.getID(email)
        returnValue = jsonify({'authenticated': validLogin, 'token': token})

    return returnValue
    
@app.route('/check-session', methods=['GET'])
def check_session():
    token = request.args.get('token')

    response = jsonify({'authenticated': True if file.checkID(token) else False})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/get-scores', methods=['GET'])
def get_scores():
    token = request.args.get('token')
    return file.getScore(token)

@app.route('/process-score', methods=['PUT'])
def process_score():
    data = request.get_json()
    id = data['id']
    operation = data['operation']
    answerList = data['answerList']
    
    updateScore = checkSkill(answerList, file.getScore(id)[operation], 0.3, 0.2)
    
    print(file.appendScore(id, operation, updateScore))
    
    return file.appendScore(id, operation, updateScore)


@app.route('/get-question', methods=['GET']) # Fix
def get_question():
    operation = request.args.get('operation')
    dynamic = request.args.get('dynamic')
    id = request.args.get('id')    
   
    
    if int(dynamic) == 0:
            question = content.getDynamicQuestion(operation, file.getScore(id)[operation])
    else:
            question = content.getQuestion(operation)

    return {"equation": question[0], "answer": question[1]} # example: ('$22+16=$', '$38$')



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)