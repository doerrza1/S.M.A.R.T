# Fall 2016 Exam 3C Problem 5

def generate(data):

    # Given Values
    d = 12
    t = 0.3
    T = 15
    p = 300

    data['params']['d'] = d
    data['params']['t'] = t
    data['params']['T'] = T
    data['params']['p'] = p

    # Answers

    sigx = 3000
    sigz = 6000
    tauxz = -0.238

    data['correct_answers']['sigx'] = sigx
    data['correct_answers']['sigz'] = sigz
    data['correct_answers']['tauxz'] = tauxz
    data['correct_answers']['units'] = 'psi'