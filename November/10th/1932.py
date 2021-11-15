import sys
"""
Python
1932번 정수 삼각형
DP
"""

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for n in range(1, n + 1)]

dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if 0 <= j < i:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + arr[i][j])
        if 0 <= j - 1 < i:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i][j])

print(max(dp[n - 1]))
