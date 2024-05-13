# Fall 2016 Exam 1D Problem 3
import math, random

def generate(data):
    F = random.randint(20,80)

    Mi = F*(-17.57)
    Mj = F*(-14.86)
    Mk = F*(4.71)

    data['params']['F'] = F

    # Answers

    data['correct_answers']['mi'] = Mi
    data['correct_answers']['mj'] = Mj
    data['correct_answers']['mk'] = Mk
    data['correct_answers']['units'] = 'lb*ins'