import math
"""
Python
1016번 제곱 ㄴㄴ 수
Math
"""
MIN, MAX = map(int, input().split())
arr = [1] * (MAX - MIN + 1)


for div in range(2, int(MAX ** 0.5)+ 1):
    n = (div ** 2) * math.ceil(MIN / (div **2))
    while MIN <= n <= MAX:
        arr[n - MIN] = 0
        n += div ** 2

print(sum(arr))
