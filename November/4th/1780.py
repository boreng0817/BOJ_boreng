import sys
"""
Python
1780번 종이의 개수
divide and conquer (recursive)
"""
ret = [0, 0, 0]


def check(x, y, size):
    symbol = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != symbol:
                return False

    return True

def solve(x, y, size):
    if size == 1:
        ret[arr[x][y]] += 1
        return

    if check(x, y, size):
        ret[arr[x][y]] += 1
    else:
        size = int(size/3)
        for i in range(3):
            for j in range(3):
                solve(x + size*i, y + size*j, size)

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

solve(0, 0, n)

print(ret[-1])
print(ret[0])
print(ret[1])
