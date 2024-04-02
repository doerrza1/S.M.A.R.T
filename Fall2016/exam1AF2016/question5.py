# Fall 2016 Exam 1A Problem 5

import random, math

def generate(data):

    P_list = [30,45,60,75,90,105]

    P = random.choice(P_list)

    data['params']['F'] = P

    # Answers

    Btau = .09375*P
    Atau = 0

    data['correct_answers']['Btau'] = Btau
    data['correct_answers']['Atau'] = Atau
    data['correct_answers']['units'] = 'ksi'