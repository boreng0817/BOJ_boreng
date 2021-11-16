import sys
"""
Python
15650번 N과 M (2)
Backtracking
"""

N, M = map(int, sys.stdin.readline().split())
arr = list(range(1, N + 1))
arr = list(map(str, arr))


def solve(arr, n, cache=[]):
    if n == 0:
        sys.stdout.write(" ".join(cache) + "\n")
        return

    for i in range(len(arr)):
        solve(arr[i + 1:], n - 1, cache + [arr[i]])


solve(arr, M)
