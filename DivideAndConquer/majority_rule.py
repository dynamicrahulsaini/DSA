# Uses python3

# Majority rule is a decision rule that selects the alternative which has a majority,that is,
# more than half the votes.Given a sequence of elements 𝑎1, 𝑎2, . . . , 𝑎𝑛, you would like to
# check whether it contains an element that appears more than 𝑛/2 times

import sys

def get_majority_element(a):
    d = {}
    for i in a:
        try:
            d[i] += 1
        except:
            d[i] = 1

    max = 0
    for i in d.keys():
        if d[i] > len(a)/2:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
