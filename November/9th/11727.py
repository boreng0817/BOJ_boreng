"""
Python
11727번 2xn 타일링 2
DP
"""

n = int(input())

arr = [0] * (n + 10)
arr[0] = 1

for i in range(n):
    arr[i + 1] += arr[i]
    arr[i + 2] += arr[i] * 2

print(arr[n] % 10_007)
