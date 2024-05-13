# Spring 2021 Exam 4B Problem 1

import math, random

def generate(data):

    A = 0.1
    F = 2

    data['params']['A'] = A
    data['params']['F'] = F

    # Answers
    delta = 0.8

    data['correct_answers']['delta'] = delta
    data['correct_answers']['units'] = 'in'