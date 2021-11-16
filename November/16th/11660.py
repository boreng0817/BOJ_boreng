import sys
"""
Python
11660번 구간 합 구하기 5
DP
"""
n, m = map(int, sys.stdin.readline().split())
arr = [[]] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(1, n + 1):
        arr[j][i + 1] += arr[j][i]

for i in range(1, n):
    for j in range(1, n + 1):
        arr[i + 1][j] += arr[i][j]



for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = arr[x2][y2]
    if x1 - 1 >= 1:
        result -= arr[x1 - 1][y2]
    if y1 - 1 >= 1:
        result -= arr[x2][y1 - 1]
    if x1 - 1 >= 1 and y1 - 1 >= 1:
        result += arr[x1 - 1][y1 - 1]
    print(result)
