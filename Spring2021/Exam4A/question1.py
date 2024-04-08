# Spring 2021 Exam 4A Problem 1

import random, math

def generate(data):
    # Given Values
    Tb = 100
    phi = 0.2
    ra = 30
    rb = 40

    data['params']['Tb'] = Tb
    data['params']['phi'] = phi
    data['params']['ra'] = ra
    data['params']['rb'] = rb

    # Answers
    Ta = 75
    phia = 0.267

    data['correct_answers']['Ta'] = 75 
    data['correct_answers']['phia'] = 0.267 
    data['correct_answers']['unitsT'] = 'Nm'
    data['correct_answers']['unitsP'] = 'rad'
    
