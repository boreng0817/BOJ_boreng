import sys
from collections import deque
"""
Python
11725번 트리의 부모 찾기
BFS
"""

n = int(sys.stdin.readline())
parent = [0] * (n+1)
visited = [0] * (n+1)
edge = {}
for _ in range(n - 1):
    s, e = map(int, sys.stdin.readline().split())
    if s not in edge:
        edge[s] = []
    if e not in edge:
        edge[e] = []

    edge[s].append(e)
    edge[e].append(s)

deq = deque([1])
visited[1] = 1
while len(deq):
    node = deq.popleft()
    for end in edge[node]:
        if not visited[end]:
            parent[end] = node
            deq.append(end)
            visited[end] = 1

for i in range(2, n + 1):
    sys.stdout.write(str(parent[i]) + '\n')
