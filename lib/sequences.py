#!/usr/bin/env python3

def print_fibonacci(length):
    answer = []
    f = 0
    s = 1

    while len(answer) < length:
        answer.append(f)
        t = f
        f = s
        s = t + s

    print(answer)

print_fibonacci(3)