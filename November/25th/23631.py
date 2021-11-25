from sys import stdin
"""
Python
23631번 진심 좌우 반복뛰기
Math, Implementation
"""
T = int(stdin.readline())
sigma = lambda x: int(x * (x + 1) / 2)

while T:
    N, K = map(int, stdin.readline().split())
    n = int((2 * (N - 1) / K) ** 0.5)

    direction = None
    distance = None
    offset = None
    while K * sigma(n) > N - 1:
        n -= 1

    offset = N - 1 - K * sigma(n)
    if n % 2 == 0:
        distance = -K * (n // 2) + offset
    else:
        distance = K * (n // 2 + 1) - offset

    direction = "R" if n % 2 == 0 else "L"
    print(distance, direction)

    T -= 1
