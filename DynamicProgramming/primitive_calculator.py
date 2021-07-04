# Uses python3
import sys
from typing import Sequence


def shortest_sequence(x):
    if len(x) == 0:
        return float('inf')
    else:
        return len(x)


def optimal_sequence(n, d={}):
    if n in d.keys():
        pass
    elif n == 1:
        d[n] = [1]
    else:
        sequence = []
        if n%2 == 0:
            sequence.append(optimal_sequence(n//2, d))
        if n%3 == 0:
            sequence.append(optimal_sequence(n//3, d))
        if len(sequence) < 2:
            sequence.append(optimal_sequence(n-1, d))
        sequence = (min(sequence, key=shortest_sequence)).copy()
        sequence.append(n)
        d[n] = sequence
    return d[n]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
