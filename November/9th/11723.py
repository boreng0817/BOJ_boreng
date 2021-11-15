import sys
"""
Python
11723번 집합
Implementation
"""

n = int(input())
all = [True] * 21
empty = [False] * 21
my_set = empty[:]

for _ in range(n):
    op = sys.stdin.readline().split()
    if len(op) == 2:
        val = int(op[1])
        op = op[0]
    else:
        op = op[0]

    if op == 'add':
        my_set[val] = True
    elif op == 'remove':
        my_set[val] = False
    elif op == 'check':
        sys.stdout.write(str(int(my_set[val])) + '\n')
    elif op == 'toggle':
        my_set[val] = not my_set[val]
    elif op == 'all':
        my_set = all[:]
    elif op == 'empty':
        my_set = empty[:]
