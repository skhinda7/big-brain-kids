taught = 0.005
slip = 0.005
guess = 0.005

def correct(known, slip, guess):
    num = (known * (1 - slip))
    den = (known * (1 - slip) + (1 - known) * guess)
    return num/den

def incorrect(known, slip, guess):
    num = (known * slip)
    den = (known * slip + (1 - known) * (1 - guess))
    return num/den

def action(known, taught):
    return known + ((1 - known) * taught)

def checkSkill(answerList, known, taught, slip, guess):
    print("Initial Known", known)
    for i in range(len(answerList)):
        if(answerList[i] == 0): # Correct Answer
            known = action(correct(known, slip, guess), taught)
        if(answerList[i] == 1): # Incorrect Answer
            known = action(incorrect(known, slip, guess), taught)
    return known
    
# testList = [1, 0, 0, 0, 0, 0, 1, 1, 1] # Test Array of Correct/Incorrect Answers
# overall_proficency = checkSkill(testList, known, taught)
# print('Skill Proficency: ', overall_proficency)

# if(overall_proficency >= 0.95):
  #  print("Skill has been mastered: ", overall_proficency)