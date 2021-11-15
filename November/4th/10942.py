import sys
"""
pypy
10941번 펠린드롬?
dp
"""

arr = [[0 for _ in range(2001)] for _ in range(2001)]

n = int(input())
string = input().split()
m = int(input())

# Build arr
for s in range(n - 1):
    arr[s][s] = 1
    string_to_cmp = string[s:s+2]
    if string_to_cmp == string_to_cmp[::-1]:
        arr[s][s+1] = 1

arr[n-1][n-1] = 1

for s in range(n):
    if arr[s][s]:
        for i in range(1, n):
            if s - i >= 0 and s + i < n and string[s+i] == string[s-i]:
                arr[s-i][s+i] = 1
            else:
                break

    if arr[s][s+1]:
        for i in range(1, n):
            if s - i >= 0 and s + 1 + i < n and string[s+1+i] == string[s-i]:
                arr[s-i][s+1+i] = 1
            else:
                break


for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(arr[s-1][e-1])
