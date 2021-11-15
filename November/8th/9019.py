from collections import deque
import sys
"""
pypy
9019번 DSLR
BFS
"""

T = int(input())
dslr = 'DSLR'
visit = [-1] * 10_001
pred = [0] * 10_001
c = [0] * 10_001


def bt(node):
    ret = ""

    while True:
        if pred[node] == -1:
            pred[node] = 0
            return ret[::-1]
        ret += dslr[c[node]]
        node = pred[node]


for t in range(1, T + 1):
    A, B = map(int, sys.stdin.readline().split())
    node = A

    deq = deque()
    deq.append(node)
    pred[node] = -1
    visit[node] = t
    while len(deq):
        n = deq.popleft()
        if n == B:
            print(bt(n))
            break

        D = 2 * n % 10_000
        S = n - 1 if n != 0 else 9999
        L = (n % 1_000) * 10 + int(n / 1_000)
        R = (n % 10) * 1_000 + int(n / 10)

        for i, num in enumerate([D, S, L, R]):
            if visit[num] != t:
                visit[num] = t
                deq.append(num)
                pred[num] = n
                c[num] = i
