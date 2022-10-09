def binary_search(v, To_Find):
    lo = 0
    hi = len(v) - 1
    

    while hi - lo > 1:
        mid = (hi + lo) // 2
        if v[mid] < To_Find:
            lo = mid + 1
        else:
            hi = mid

    if v[lo] == To_Find:
        print("Found At Index", lo)
    elif v[hi] == To_Find:
        print("Found At Index", hi)
    else:
        print("Not Found")


if __name__ == '__main__':    
    v = [1, 3, 4, 5, 6]

    To_Find = 1
    binary_search(v, To_Find)

    To_Find = 6
    binary_search(v, To_Find)


    To_Find = 10
    binary_search(v, To_Find)