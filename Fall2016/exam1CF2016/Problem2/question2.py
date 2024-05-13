# Fall 2016 Exam 1C Problem 2

import math, random

def generate(data):

    F = random.randint(20,70)
    theta = random.randint(20,80)

    data['params']['F'] = F
    data['params']['theta'] = theta

    # Answers

    M = 3.6*F*math.sin(math.radians(theta)) - 2.7*F*math.cos(math.radians(theta))

    data['correct_answers']['mk'] = M
    data['correct_answers']['units'] = 'kN*m'