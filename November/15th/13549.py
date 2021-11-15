from collections import deque
"""
Python
13549번 숨바꼭질 3
BFS
 * visited technique
"""
n, k = map(int, input().split())

arr = [100_000_000] * 100_001
visited = [0] * 100_001

deq = deque([(n, 0)])
arr[n] = 0
visited[n] = 1

while len(deq):
    node, step = deq.popleft()
    temp = node * 2
    while temp <= 100_000 and visited[temp] == 0:
        arr[temp] = step
        # Avoid multiple expandation for 2n * temp
        visited[temp] = 1
        deq.append((temp, step))
        temp *= 2

    step += 1
    for next_node in [node - 1, node + 1]:
        if 0 <= next_node <= 100_000 and step <= arr[k]:
            if arr[next_node] > step:
                arr[next_node] = step
                deq.append((next_node, step))

print(arr[k])
