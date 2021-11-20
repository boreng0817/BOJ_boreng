import sys
"""
Python
1018번 체스판 다시 칠하기
Brute force
"""

N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline() for _ in range(N)]

white = [[0] * M for _ in range(N)]
black = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if (i+j) % 2 == 0:
            if board[i][j] == 'B':
                white[i][j] = 1
            else:
                black[i][j] = 1
        else:
            if board[i][j] == 'W':
                white[i][j] = 1
            else:
                black[i][j] = 1

def getSum(arr, x, y):
    ret = 0
    if x + 8 <= N and y + 8 <= M:
        for i in range(8):
            ret += sum(arr[x+i][y:(y+8)])
    return ret

ans = 9876543210
for i in range(N - 7):
    for j in range(M - 7):
        ans = min(ans, getSum(black, i, j), getSum(white, i, j))

print(ans)
