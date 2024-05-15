# Spring 2018 Exam 3A Problem 8

def generate(data):

    # Given Values
    F = 3
    t = 0.25
    r = 1.5
    p = 30

    data['params']['F'] = F
    data['params']['t'] = t
    data['params']['r'] = r
    data['params']['p'] = p

    # Answers

    fx = 577.8
    tauf = 252.8
    fy = 0

    px = 1080
    taup = 0
    py = 2160

    sigx = 1660
    sigy = 2160
    tauxy = 253

    data['correct_answers']['fx'] = fx
    data['correct_answers']['tauf'] = tauf
    data['correct_answers']['fy'] = fy

    data['correct_answers']['px'] = px
    data['correct_answers']['taup'] = taup
    data['correct_answers']['py'] = py

    data['correct_answers']['sigx'] = sigx
    data['correct_answers']['sigy'] = sigy
    data['correct_answers']['tauxy'] = tauxy

    data['correct_answers']['units'] = 'psi'
