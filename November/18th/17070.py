import sys
from collections import deque
"""
Python
17070번 파이프 옮기기 1
DP, BFS
"""

N = int(sys.stdin.readline())
arr = [sys.stdin.readline().split() for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
# x, y, state
deq = deque([(0, 1)])
dp[0][1][0] = 1

while len(deq):
    x, y = deq.popleft()
    if sum(dp[x][y]) == 0:
        continue

    if dp[x][y][0]:
        if y + 1 < N:
            if arr[x][y + 1] == '0':
                dp[x][y + 1][0] += dp[x][y][0]
                deq.append((x, y+1))

        if y + 1 < N and x + 1 < N:
            if arr[x][y+1] == '0' and arr[x+1][y+1] == '0' and arr[x+1][y] == '0':
                dp[x+1][y+1][1] += dp[x][y][0]
                deq.append((x+1, y+1))

    if dp[x][y][1]:
        if y + 1 < N:
            if arr[x][y + 1] == '0':
                dp[x][y + 1][0] += dp[x][y][1]
                deq.append((x, y+1))

        if y + 1 < N and x + 1 < N:
            if arr[x][y+1] == '0' and arr[x+1][y+1] == '0' and arr[x+1][y] == '0':
                dp[x+1][y+1][1] += dp[x][y][1]
                deq.append((x + 1, y + 1))

        if x + 1 < N:
            if arr[x+1][y] == '0':
                dp[x+1][y][2] += dp[x][y][1]
                deq.append((x + 1, y))

    if dp[x][y][2]:
        if y + 1 < N and x + 1 < N:
            if arr[x][y+1] == '0' and arr[x+1][y+1] == '0' and arr[x+1][y] == '0':
                dp[x+1][y+1][1] += dp[x][y][2]
                deq.append((x + 1, y + 1))
        if x + 1 < N:
            if arr[x+1][y] == '0':
                dp[x+1][y][2] += dp[x][y][2]
                deq.append((x + 1, y))

    if not (x == N - 1 and y == N -1):
        dp[x][y] = [0, 0, 0]

print(sum(dp[N-1][N-1]))
