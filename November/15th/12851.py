from collections import deque
"""
Python
12851번 숨바꼭질 2
BFS, dp
"""
n, k = map(int, input().split())

arr = [100_000_000] * 100_001
visited = [0] * 100_001

deq = deque([(n, 0)])
arr[n] = 0
visited[n] = 1

while len(deq):
    node, step = deq.popleft()
    step += 1

    for next_node in [node - 1, node + 1, node * 2]:
        if 0 <= next_node <= 100_000 and step <= arr[k]:
            if arr[next_node] == step:
                visited[next_node] += visited[node]
            elif arr[next_node] > step:
                visited[next_node] = visited[node]
                arr[next_node] = step
                deq.append((next_node, step))

print(arr[k])
print(visited[k])
