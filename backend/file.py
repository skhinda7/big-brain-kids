import csv
import json

userDB = 'backend/users.csv'
scoresDB = 'backend/scores.json'


def saveUser(data, id):
    data.append(id)
    with open(userDB, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data) # Data should be like this: ['First Name', 'Last Name', 'Email', 'Password', 'ID']

    
    new_item = {
        "id": str(id),
        "scores": {
            "addition": 0,
            "subtraction": 0,
            "multiplication": 0,
            "division": 0
        }
    }
    
    with open(scoresDB, 'r') as file:
        scoreData = json.load(file)
    
    scoreData["data"].append(new_item)
    
    with open(scoresDB, 'w') as file:
        json.dump(scoreData, file, indent=4)
    

    print(f"Data saved to {userDB}")

def getID(email):
    with open(userDB, mode='r') as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            if row[2] == email:  # Assuming email is in the third column (index 2)
                return row[4]  # Return the ID (assuming it's in the fifth column, index 4)
    return None  # Return None if email is not found

def checkID(id):
    with open(userDB, mode='r') as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            if row[4] == str(id):
                return True
        return False

def checkUser(email, password):
    emailFound = passwordFound = False
    with open(userDB, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['Email'] == str(email):
                emailFound = True  
                if row['Password'] == str(password):
                    passwordFound = True
            if emailFound and passwordFound == True:
                return True
    return False
    
def getScore(id):
    with open(scoresDB, 'r') as file:
        data = json.load(file)

    for entry in data['data']:
        if entry['id'] == id:
            return entry['scores']
    return 'Null' 

def appendScore(id, operation, score):
    with open(scoresDB, 'r') as file:
        data = json.load(file)

    for entry in data['data']:
        if entry['id'] == id:
            if operation in entry['scores']:
                entry['scores'][operation] = score
                with open(scoresDB, 'w') as file:
                    json.dump(data, file, indent=4)
                return {"result": f"Updated {operation} score for {id} to {score}"}
            else:
                return {"result": f"{operation} operation not found for ID {id}"}
    
    