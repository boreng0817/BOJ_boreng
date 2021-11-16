import sys
"""
PyPy
15666번 N과 M (12)
Backtracking
"""

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
arr = list(map(str, arr))
hash = []


def solve(arr, n, cache=[]):
    if n == 0:
        ret = " ".join(cache)
        if ret not in hash:
            hash.append(ret)
            sys.stdout.write(ret + "\n")
        return

    for i in range(len(arr)):
        solve(arr[i:], n - 1, cache + [arr[i]])

solve(arr, M)
