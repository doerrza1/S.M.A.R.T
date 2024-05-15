# Fall 2016 Exam 4C Problem 8

def generate(data):

    # Given Values

    P = 600
    L = 4
    
    data['params']['P'] = P
    data['params']['L'] = L

    # Answers

    rby = 1900
    ray = 725
    rcy = -225

    mmax = -525
    x = 3

    fs = 1.98

    data['correct_answers']['rby'] = rby
    data['correct_answers']['rcy'] = rcy
    data['correct_answers']['ray'] = ray

    data['correct_answers']['mmax'] = mmax
    data['correct_answers']['x'] = x

    data['correct_answers']['fs'] = fs

    data['correct_answers']['unitsr'] = 'N'
    data['correct_answers']['unitsm'] = 'Nm'
    data['correct_answers']['unitsx'] = 'm'