import sys
from collections import deque
"""
Python
1260번 DFS와 BFS
BFS, DFS
"""

n, m, s = map(int, sys.stdin.readline().split())
edge = {}
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    if start not in edge:
        edge[start] = []
    if end not in edge:
        edge[end] = []
    edge[start].append(end)
    edge[end].append(start)

for e in edge:
    edge[e] = sorted(edge[e])

# dfs
visited = [0] * (n + 1)
print_queue = deque([s])
deq = deque([s])
visited[s] = 1

def dfs():
    while len(deq) and len(print_queue) != n:
        node = deq.pop()

        if node in edge:
            for e in edge[node]:
                if visited[e] == 0:
                    print_queue.append(e)
                    deq.append(e)
                    visited[e] = 1
                    dfs()

dfs()

print(" ".join(map(str, (print_queue))))

# bfs
visited = [0] * (n + 1)
print_queue = deque([s])
deq = deque([s])
visited[s] = 1

while len(deq) and len(print_queue) != n:
    node = deq.popleft()

    if node in edge:
        for e in edge[node]:
            if visited[e] == 0:
                print_queue.append(e)
                deq.append(e)
                visited[e] = 1

print(" ".join(map(str, (print_queue))))
