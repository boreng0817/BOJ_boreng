import sys
from collections import deque

"""
Python
7576번 토마토
BFS
"""
DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]
M, N = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().split() for _ in range(N)]
count = 0
date = -1
ones = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            ones.append((i, j, 0))
        elif arr[i][j] == '0':
            count += 1

deq = deque(ones)

while len(deq) and count != 0:
    x, y, cost = deq.popleft()
    date = cost
    for dx, dy in zip(DX, DY):
        _x, _y = x + dx, y + dy
        if 0 <= _x < N and 0 <= _y < M:
            if arr[_x][_y] == '0':
                arr[_x][_y] = '1'
                count -= 1
                deq.append((_x, _y, cost + 1))

if count == 0:
    print(date + 1)
else:
    print(-1)
