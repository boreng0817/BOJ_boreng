import sys
from collections import deque
"""
Python
2206번 벽 부수고 이동하기
BFS
"""
DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]
INF = 1234567890

N, M = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().strip() for _ in range(N)]
visited = [[[INF] * M for _ in range(N)] for _ in range(2)]

# x, y, cost, wall
deq = deque([(0, 0, 0)])
visited[0][0][0] = 1

while len(deq):
    x, y, wall = deq.popleft()
    for dx, dy in zip(DX, DY):
        _x = x + dx
        _y = y + dy

        if 0 <= _x < N and 0 <= _y < M:
            if wall == 0:
                if arr[_x][_y] == '1':
                    if visited[0][_x][_y] > visited[0][x][y] + 1:
                        visited[1][_x][_y] = visited[0][x][y] + 1
                        deq.append((_x, _y, 1))
                else:
                    if visited[0][_x][_y] > visited[0][x][y] + 1:
                        visited[0][_x][_y] = visited[0][x][y] + 1
                        deq.append((_x, _y, 0))
            else:
                if arr[_x][_y] == '0' and visited[wall][_x][_y] > visited[wall][x][y] + 1:
                    visited[wall][_x][_y] = visited[wall][x][y] + 1
                    deq.append((_x, _y, wall))

ans = min(visited[0][N-1][M-1], visited[1][N-1][M-1])
print(ans if ans != INF else -1)
