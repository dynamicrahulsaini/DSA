# Uses python3

# An inversion of a sequence 𝑎[0], 𝑎[1], . . . , 𝑎[𝑛−1] is a pair of indices 0 ≤ 𝑖 < 𝑗 < 𝑛 
# such that 𝑎[𝑖] > 𝑎[𝑗]. The number of inversions of a sequence in some sense measures how 
# close the sequence is to being sorted. For example, a sorted (in non-descendingorder) 
# sequence contains no inversions at all, while in a sequence sorted in de-scending order
# any two elements constitute an inversion (for a total of 𝑛(𝑛−1)/2 inversions).

import sys

def merge(a, b, left, ave, right):
    num_of_inversions = 0
    i, j, k = left, ave + 1, left
    while i <= ave and j <= right:
        if a[i] > a[j]:
            num_of_inversions += (ave - i) + 1
            b[k] = a[j]
            j += 1
        else:
            b[k] = a[i]
            i += 1
        k += 1
    
    while i <= ave:
        b[k] = a[i]
        k += 1
        i += 1
    
    while j <= right:
        b[k] = a[j]
        k += 1
        j += 1
    
    a[left:right+1] = b[left:right+1]
    
    return num_of_inversions


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left < 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave + 1, right)
    #write your code here
    number_of_inversions += merge(a, b, left, ave, right)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a) - 1))
