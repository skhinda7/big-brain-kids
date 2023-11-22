import csv
import json

def saveUsers(data, id):
    data.append(id)
    file_path = 'users.csv'
    with open(file_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data) # Data should be like this: ['First Name', 'Last Name', 'ID']

    print(f"Data saved to {file_path}")

def getUser(id):
    found_row = None
    with open('users.csv', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['ID'] == str(id):
                found_row = row
                break  # Stop searching after the target ID is found

    if found_row:
        return found_row
    else:
        return 'Not found'
    
def getScore(id):
    with open('scores.json', 'r') as file:
        data = json.load(file)

    for entry in data['data']:
        if entry['id'] == id:
            return entry['scores']
    return None 

def appendScore(id, operation, score):
    with open('scores.json', 'r') as file:
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