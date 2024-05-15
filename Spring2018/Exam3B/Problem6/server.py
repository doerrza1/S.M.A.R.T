# Spring 2018 Exam 3B Problem 6

def generate(data):

    # Given Values
    F = 25
    r = 2
    P = 400
    t = 1

    data['params']['F'] = F
    data['params']['r'] = r
    data['params']['P'] = P
    data['params']['t'] = t

    # Answers

    sigx = -160
    sigy = 80
    tauxy = 0

    primex = 20.1
    primey = 20.1
    primetau = 103.7

    fs = 1.33

    data['correct_answers']['sigx'] = sigx
    data['correct_answers']['sigy'] = sigy
    data['correct_answers']['tauxy'] = tauxy

    data['correct_answers']['primex'] = primex
    data['correct_answers']['primey'] = primey
    data['correct_answers']['primetau'] = primetau

    data['correct_answers']['fs'] = fs

    data['correct_answers']['units'] = 'kPa'
