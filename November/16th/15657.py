import sys
"""
Python
15657번 N과 M (8)
Backtracking
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
        solve(arr[i:], n - 1, cache + [arr[i]])

solve(arr, M)
