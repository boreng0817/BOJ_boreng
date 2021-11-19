import sys
from collections import deque
from itertools import combinations
"""
Python
15686번 치킨 배달
Brute Force, BFS
"""

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().split() for _ in range(N)]
house = {}
chicken = {}
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            house[(i, j)] = []
        elif arr[i][j] == '2':
            chicken[(i, j)] = len(chicken)


for node in chicken:
    deq = deque([node])
    visited = [[0] * N for _ in range(N)]
    count = 0
    while len(deq):
        x, y = deq.popleft()
        for _dx, _dy in zip(dx, dy):
            _x, _y = x+_dx, y+_dy
            if 0 <= _x < N and 0 <= _y < N:
                if visited[_x][_y] == 0:
                    visited[_x][_y] = visited[x][y] + 1
                    deq.append((_x, _y))
                    if arr[_x][_y] == '1':
                        house[(_x, _y)].append(visited[_x][_y])
                        if count == len(house) - 1:
                            deq = deque([])
                            break
                        count += 1

ans = 1234567890
for combi in combinations(list(range(len(chicken))), M):
    distance = 0
    for _house in house.values():
        temp = 1234567890
        for index in combi:
            temp = min(temp, _house[index])
        distance += temp
    ans = min(ans, distance)

print(ans)
