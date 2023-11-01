import mathgenerator as mg
from bkt import checkSkill

# Documentation: https://lukew3.github.io/mathgenerator/mathgenerator.html
answers = []

for question in range(5):
  problem, solution = mg.addition()
  print(problem.replace('$', ''))
  if(input() == solution.replace('$', '')):
    print('Correct!')
    answers.insert(question, 0)
  else:
    print('Incorrect')
    answers.insert(question, 1)

def newStudent(answers):
  return checkSkill(answers, 0, 0.1)

print(answers)

print('Your proficiency is ', newStudent(answers))



