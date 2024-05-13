# Fall 2016 Exam 3A Problem 5

def generate(data):

    # Given values
    d = 10
    t = 0.25
    F = 15
    p = 300

    data['params']['d'] = d
    data['params']['t'] = t
    data['params']['F'] = F
    data['params']['p'] = p

    # Answers

    sigx = -1.91

    sig1 = 6
    sig2 = 3

    superx = 1.09
    superz = 6

    data['correct_answers']['sigx'] = sigx
    data['correct_answers']['sig1'] = sig1
    data['correct_answers']['sig2'] = sig2
    data['correct_answers']['superx'] = superx
    data['correct_answers']['superz'] = superz
    data['correct_answers']['units'] = 'ksi'