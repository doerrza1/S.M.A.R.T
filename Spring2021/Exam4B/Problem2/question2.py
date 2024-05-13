# Spring 2021 Exam 4B Problem 2

import math, random

def generate(data):
    # Given Values
    ep1 = 19.64
    ep2 = 114.7
    ep3 = 117.8

    data['params']['ep1'] = ep1
    data['params']['ep2'] = ep2
    data['params']['ep3'] = ep3

    # Answers
    epx = 19.64
    epy = 117.8
    tau = 91.96

    data['correct_answers']['epx'] = epx
    data['correct_answers']['epy'] = epy
    data['correct_answers']['tau'] = tau