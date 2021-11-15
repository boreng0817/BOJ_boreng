"""
Python
1629번 곱셈
Divide & Conquer, math
"""
A, B, C = map(int, input().split())
ret = 1

while B > 0:
    num = A
    num %= C
    n = 2
    while n < B:
        num *= num
        num %= C
        n *= 2
    n = n // 2
    ret *= num
    ret %= C
    B -= n

print(ret)
