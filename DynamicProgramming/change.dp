# Uses python3
import sys

def get_change(m, d={}, denominations=[1, 3, 4]):
    if m < 0:
        return None
    elif m == 0:
        return 0
    else:
        if m in d.keys():
            return d[m]
        else:
            cost = []
            for i in denominations:
                cost.append(get_change(m - i, d))
            d[m] = min([i + 1 for i in cost if i is not None])
            return d[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
