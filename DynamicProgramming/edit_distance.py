# Uses python3
def edit_distance(s, t, n=0, m=0, d={}):
    if len(s) - n == 0 or len(t) - m == 0:
        return len(s) - n + len(t) - m
    elif (n, m) in d.keys():
        pass
    else:
        cost = []

        cost.append(edit_distance(s, t, n + 1, m + 1, d))
        if s[n] != t[m]:
            cost.append(edit_distance(s, t, n, m + 1, d) + 1)
            cost.append(edit_distance(s, t, n + 1, m, d) + 1)
            cost[0] += 1
        
        min_cost = min(cost)
        d[(n, m)] = min_cost
    
    return d[(n, m)]


if __name__ == "__main__":
    # print(edit_distance(input(), input()))
    print(edit_distance("editing", "distance"))
