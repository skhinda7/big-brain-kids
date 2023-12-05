initialTaught = 0.0001
slip = 0.0001
guess = 0.0001

def getTaught(known):
    return initialTaught / (1 + known)

def correct(known, slip, guess):
    num = (known * (1 - slip))
    den = (known * (1 - slip) + (1 - known) * guess)
    return num/den

def incorrect(known, slip, guess):
    num = (known * slip)
    den = (known * slip + (1 - known) * (1 - guess))
    return num/den

def action(known):
    return known + ((1 - known) * getTaught(known))

def checkSkill(answerList, known, slip, guess):
    print("Initial Known", known)
    for i in range(len(answerList)):
        if(answerList[i] == 0): # Correct Answer
            known = action(correct(known, slip, guess))
        if(answerList[i] == 1): # Incorrect Answer
            known = action(incorrect(known, slip, guess))
    return known
    
# testList = [1, 0, 0, 0, 0, 0, 1, 1, 1] # Test Array of Correct/Incorrect Answers
# overall_proficency = checkSkill(testList, known, taught)
# print('Skill Proficency: ', overall_proficency)

# if(overall_proficency >= 0.95):
  #  print("Skill has been mastered: ", overall_proficency)