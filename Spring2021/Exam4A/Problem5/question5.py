# Spring 2021 Exam 4A Problem 5

import random, math

def generate(data):
    # Given Values
    P = 40

    data['params']['P'] = P

    # Answers
    Rbx = -13.3
    Rax = -26.7

    data['correct_answers']['Rbx'] = Rbx
    data['correct_answers']['Rax'] = Rax
    data['correct_answers']['units'] = 'kN'