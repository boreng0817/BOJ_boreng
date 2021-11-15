"""
pypy
11047번 동전 0
DP
"""

n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]
n = 0

for v in reversed(c):
    while k >= v:
        k -= v
        n += 1
print(n)
