import sys
"""
Python
10830번 행렬 제곱
Math
"""
def identity(N):
    ret = [[0] * N for _ in range(N)]
    for i in range(N):
        ret[i][i] = 1
    return ret

def matmul(arr1, arr2):
    ret = []
    N = len(arr1)

    for i in range(N):
        temp = []
        for j in range(N):
            s = 0
            for k in range(N):
                s += arr1[i][k] * arr2[k][j]
            temp.append(s%1000)
        ret.append(temp)
    return ret


def copy(arr):
    return [l[:] for l in arr]

N, B = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = identity(N)

count = 2
while B > 0:
    temp = copy(arr)
    while B - count > 0:
        temp = matmul(temp, temp)
        count *= 2
    B -= count // 2
    count = 2
    ans = matmul(ans, temp)

for l in ans:
    print(" ".join(map(str, l)))
