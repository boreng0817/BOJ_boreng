import sys
from collections import deque

"""
PyPy
7579번 토마토
BFS
"""
DX = [0, 0, 1, -1, 0, 0]
DY = [1, -1, 0, 0, 0, 0]
DH = [0, 0, 0, 0, 1, -1]
M, N, H = map(int, sys.stdin.readline().split())
arr = [[sys.stdin.readline().split() for _ in range(N)] for _ in range(H)]
count = 0
date = -1
ones = []


for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == '1':
                ones.append((i, j, k, 0))
            elif arr[i][j][k] == '0':
                count += 1

deq = deque(ones)

while len(deq) and count != 0:
    z, x, y, cost = deq.popleft()
    date = cost
    for dx, dy, dz in zip(DX, DY, DH):
        _x, _y, _z = x + dx, y + dy, z + dz
        if 0 <= _x < N and 0 <= _y < M and 0 <= _z < H:
            if arr[_z][_x][_y] == '0':
                arr[_z][_x][_y] = '1'
                count -= 1
                deq.append((_z, _x, _y, cost + 1))

if count == 0:
    print(date + 1)
else:
    print(-1)
