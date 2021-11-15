from collections import deque
import sys
"""
Python
16928번 뱀과 사다리 게임
BFS
"""

n = sum(map(int, sys.stdin.readline().split()))
portal = dict([map(int, sys.stdin.readline().split()) for _ in range(n)])

def solve():
    deq = deque([(1, 0)])
    visited = [0] * 101

    while len(deq):
        n, step = deq.popleft()
        num = None
        for i in range(1, 7):
            if n + i in portal:
                num = portal[n + i]
            else:
                num = n + i
            if num == 100:
                return step + 1
            if visited[num] == 0:
                visited[num] = 1
                deq.append((num, step + 1))

