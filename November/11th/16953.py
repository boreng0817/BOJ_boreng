from collections import deque
"""
Python
16953번 A -> B
BFS
"""

a, b = map(int, input().split())

deq = deque([(a, 0)])
ret = None

while len(deq):
    num, depth = deq.popleft()
    if num == b:
        ret = depth + 1
        break
    if num > b:
        continue
    deq.append((num * 2, depth + 1))
    deq.append((num*10 + 1, depth + 1))

if ret:
    print(ret)
else:
    print(-1)
