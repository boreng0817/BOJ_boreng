from sys import stdin
"""
Python
11054번 가장 긴 바이토닉 부분 수열
DP
"""
n = int(stdin.readline())
arr = [0] + list(map(int, stdin.readline().split()))
dp = [[1] * (n+1) for _ in range(2)]

for i in range(1, n + 1):
    index = 1
    while i - index >= 1:
        if arr[i] > arr[i - index]:
            dp[0][i] = max(dp[0][i], dp[0][i - index] + 1)
        index += 1

arr = arr[1:]
arr.reverse()
arr = [0] + arr
for i in range(1, n + 1):
    index = 1
    while i - index >= 1:
        if arr[i] > arr[i - index]:
            dp[1][i] = max(dp[1][i], dp[1][i - index] + 1)
        index += 1

ans = 0
for i in range(1, n + 1):
    ans = max(ans, dp[0][i] + dp[1][n + 1 - i])
print(ans - 1)
