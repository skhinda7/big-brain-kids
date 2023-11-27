import mathgenerator as mg

# Documentation: https://lukew3.github.io/mathgenerator/mathgenerator.html

def getQuestion(operation):
  if(operation == 'addition'):
    return mg.addition()
  elif(operation == 'subtraction'):
    return mg.subtraction()
  elif(operation == 'multiplication'):
    return mg.multiplication()
  elif(operation == 'division'):
    return mg.division()

# def getDynamicQuestion(operation, known):
  # if()