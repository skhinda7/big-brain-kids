known = 0.4
taught = 0.1
slip = 0.3
guess = 0.2

def correct(known, taught, slip, guess):
    num = (known * (1 - slip))
    den = (known * (1 - slip) + (1 - known) * guess)
    return num/den

def incorrect(known, taught, slip, guess):
    num = (known * slip)
    den = (known * slip + (1 - known) * (1 - guess))
    return num/den

def action(known, taught):
    return known + ((1 - known) * taught)

print("Initial Known: ", known)

altknown = incorrect(known, taught, slip, guess)
known = action(altknown, taught)
print("Incorrect Answer: ", known)

altknown = correct(known, taught, slip, guess)
known = action(altknown, taught)
print("Correct Answer: ", known)

altknown = correct(known, taught, slip, guess)
known = action(altknown, taught)
print("Correct Answer: ", known)

altknown = incorrect(known, taught, slip, guess)
known = action(altknown, taught)
print("Final Probability: ", known)