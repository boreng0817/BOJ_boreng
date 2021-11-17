from collections import deque
"""
Python
14502번 연구소
BFS, Brute force
"""
N, M = map(int, input().split())
arr = [input().split() for _ in range(N)]
arr = sum(arr, [])
virus = []
result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(M):
        if arr[i*M + j] == '2':
            virus.append((i, j))

for a in range(N * M):
    if arr[a] != '0':
        continue
    for b in range(a + 1, N * M):
        if arr[b] != '0':
            continue
        for c in range(b + 1, N * M):
            if arr[c] != '0':
                continue

            test = arr[:]
            test[a] = test[b] = test[c] = '1'
            # BFS ==============
            deq = deque(virus)
            while len(deq):
                x, y = deq.popleft()
                for _dx, _dy in zip(dx, dy):
                    _x, _y = x + _dx, y + _dy

                    if 0 <=_x < N and 0 <=_y < M:
                        pos = _x*M + _y
                        if test[pos] == '0':
                            test[pos] = '2'
                            deq.append((_x, _y))
            # BFS ==============
            result = max(result, sum(["".join(l).count('0') for l in test]))

print(result)
