import sys
"""
Python
3273번 두 수의 합
implementation
"""
N = int(input())
my_set = set(map(int, sys.stdin.readline().split()))
target = int(input())

ans = 0

while len(my_set):
    n = my_set.pop()
    if target - n in my_set:
        ans += 1

print(ans)
