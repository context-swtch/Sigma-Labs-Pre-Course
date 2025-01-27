def digitize(n):
    n = str(n)
    n = n[::-1]
    l = list(n)
    l = [int(c) for c in l]
    return l