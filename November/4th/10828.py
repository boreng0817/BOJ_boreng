import sys
"""
Python
10828번 스택
stack
"""

arr = [0 for _ in range(10_002)]
arr[-1] = -1
size = 0
op = int(input())


for _ in range(op):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        arr[size] = command[1]
        size += 1
    elif command[0] == 'pop':
        if size == 0:
            print(-1)
        else:
            size -= 1
            print(arr[size])
    elif command[0] == 'size':
        print(size)
    elif command[0] == 'empty':
        print(int(size==0))
    elif command[0] == 'top':
        print(arr[size - 1])
