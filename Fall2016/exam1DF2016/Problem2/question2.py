# Fall 2016 Exam 1D Problem 2

import random, math

def generate(data):

    F = random.randint(30,80)

    data['params']['F'] = F

    # Answers

    M = 0.16*F*math.sin(math.radians(20)) -0.3*F*math.cos(math.radians(20))

    data['correct_answers']['mk'] = M
    data['correct_answers']['units'] = 'N*m'