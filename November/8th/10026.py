from collections import deque
import sys
"""
pypy
10026번 적록색약
BFS
"""

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())

arr = [sys.stdin.readline() for _ in range(n)]
visit1 = [[0] * n for _ in range(n)]
visit2 = [[0] * n for _ in range(n)]

def bfs(i, j, option):
    deq = deque([(i, j)])

    while len(deq):
        i, j = deq.popleft()
        color = arr[i][j]
        if option == 1:
            visit1[i][j] = 1
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if not 0 <= x < n or not 0 <= y < n:
                    continue
                if arr[x][y] == color and visit1[x][y] == 0:
                    visit1[x][y] = 1
                    deq.append((x, y))
        else:
            visit2[i][j] = 1
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if not 0 <= x < n or not 0 <= y < n:
                    continue
                if color == arr[x][y] or color in ['R', 'G'] and arr[x][y] in ['R', 'G']:
                    if visit2[x][y] == 0:
                        visit2[x][y] = 1
                        deq.append((x, y))

rgb = 0
rrb = 0

for i in range(n):
    for j in range(n):
        if visit1[i][j] == 0:
            bfs(i, j, 1)
            rgb += 1
        if visit2[i][j] == 0:
            bfs(i, j, 2)
            rrb += 1

print(rgb, rrb)
