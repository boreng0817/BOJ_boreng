import sys
"""
Python
15654번 N과 M (5)
Back tracking
"""
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
arr = list(map(str, arr))


def solve(arr, n, cache=[]):
    if n == 0:
        sys.stdout.write(" ".join(cache) + "\n")
        return

    for i in range(len(arr)):
        solve(arr[:i] + arr[i+1:], n - 1, cache + [arr[i]])

solve(arr, M)
