import mathgenerator as mg
import random


# Documentation: https://lukew3.github.io/mathgenerator/mathgenerator.html

def getQuestion(operation):
  if(operation == 'addition'):
    print('test')
    question = mg.addition()
  elif(operation == 'subtraction'):
    question = mg.subtraction()
  elif(operation == 'multiplication'):
    question = mg.multiplication()
  elif(operation == 'division'):
    question = mg.division()
  return (question[0].replace('$', ''), question[1].replace('$', ''))

def getDynamicQuestion(operation, known):
  if(operation == 'addition'):
    a = random.randint(int(known * 10), int(known * 100))
    b = random.randint(int(known * 10), int(known * 100))
    c = a + b
    sign = '+'
  elif(operation == 'subtraction'):
    a = random.randint(int(known * 71), int(known * 150))
    b = random.randint(int(known * 10), int(known * 70))
    c = a - b
    sign = '-'
  elif(operation == 'multiplication'):
    a = random.randint(int(known * 10), int(known * 20))
    b = random.randint(int(known * 10), int(known * 20))
    c = a * b
    sign = 'x'  
  elif(operation == 'division'):
    numOne = random.randint(1, int(known * 20))
    numTwo = random.randint(1, int(known * 20))
    a = numOne * numTwo
    b = random.choice([numOne, numTwo])
    c = int(a / b)
    sign = '&divide;'  
  return (f'{str(a)} {str(sign)} {str(b)}', f'{str(int(c))}')
