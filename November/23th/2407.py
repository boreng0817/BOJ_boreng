"""
Python
2407번 조합
Memoization
"""
N, R = map(int, input().split())


def comb(n, r, cache):
    r = min(r, n - r)
    if (n, r) in cache:
        return cache[(n, r)]
    else:
        if r == 1:
            return n
        if r == 0 or n == 0:
            return 1
        cache[(n, r)] = comb(n - 1, r - 1, cache) + comb(n - 1, r, cache)
        return cache[(n, r)]


print(comb(N, R, {}))
