import sys
"""
Python
12865번 평범한 배낭
Knap-sack
"""
n, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0] * (k+5)



for weight, value in arr:
    for i in range(k, -1, -1):
        if i + weight > k:
            continue
        dp[i + weight] = max(dp[i + weight], dp[i] + value)
