from collections import deque
"""
Python
12852번 1로 만들기 2
DP
"""
def solve(num):
    result = [num]
    while num != 1:
        num = arr[num]
        result.append(num)

    print(len(result) - 1)
    print(" ".join(map(str, result)))

n = int(input())
arr = [0] * 1_000_001
arr[1] = 1
deq = deque([1])

while len(deq):
    node = deq.popleft()
    if node == n:
        solve(n)
    for next_node in [node + 1, node * 2, node * 3]:
        if next_node <= 1_000_000 and arr[next_node] == 0:
            arr[next_node] = node
            deq.append(next_node)
