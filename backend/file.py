import csv
import json

userDB = 'backend/users.csv'
scoresDB = 'backend/scores.json'


def saveUser(data, id):
    data.append(id)
    with open(userDB, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data) # Data should be like this: ['First Name', 'Last Name', 'Email', 'Password', 'ID']

    print(f"Data saved to {userDB}")

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
                with open('scores.json', 'w') as file:
                    json.dump(data, file, indent=4)
                return f"Updated {operation} score for {id} to {score}"
            else:
                return f"{operation} operation not found for ID {id}"
    
    return f"ID {id} not found"