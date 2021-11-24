import sys
from collections import deque
"""
Python
14938번 서강그라운드
BFS
"""

N, M, R = map(int, sys.stdin.readline().split())
item_cost = [0] + list(map(int, sys.stdin.readline().split()))
edges = {}
for _ in range(R):
    s, e, w = map(int, sys.stdin.readline().split())
    if s not in edges:
        edges[s] = []
    if e not in edges:
        edges[e] = []

    edges[s].append((e, w))
    edges[e].append((s, w))

for e in edges:
    edges[e].sort(key=lambda x: x[1])

best = 0
for i in range(1, N+1):
    deq = deque([(i, 0)])
    visited = [0] * (N+1)
    ans = 0
    while len(deq):
        node, cost = deq.popleft()
        if visited[node] == 0:
            ans += item_cost[node]
            visited[node] = 1
        if node in edges:
            for end, weight in edges[node]:
                if cost + weight <= M:
                    deq.append((end, cost + weight))
    best = max(best, ans)

print(best)
