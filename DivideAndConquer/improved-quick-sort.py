# Uses python3

# The goal in this problem is to redesign a given implementation of the randomized quick
# sort algorithm so that it works fast even on sequences containingmany equal elements.

import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] == x:
            j += 1
            a[i], a[j] = a[j], a[i]
    return j

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, low, high):
    if low >= high:
        return
    k = random.randint(low, high)
    a[low], a[k] = a[k], a[low]
    
    #use partition3
    lessthanpivot = partition2(a, low, high)
    greaterthanpivot = partition3(a, lessthanpivot, high)

    randomized_quick_sort(a, low, lessthanpivot -1)
    randomized_quick_sort(a, greaterthanpivot + 1, high)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
