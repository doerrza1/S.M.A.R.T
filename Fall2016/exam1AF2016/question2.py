# Fall 2016 Exam 1A Problem 2

import random, math

def generate(data):

    F = random.randint(10,40)

    data['params']['F'] = F

    # Answers

    M = 1.2*F*math.cos(math.radians(40)) + 0.6*F*math.sin(math.radians(40))

    data['correct_answers']['mk'] = M
    data['correct_answers']['units'] = 'kN*m'