"""
Python
11444번 피보나치 수 6
Math, implementation
"""
"""
Note. Fibonacci
[1, 1] ^ n  -->  [F_n+1, F_n]
[1, 0]           [F_n, F_n-1]
"""
MOD = 1_000_000_007


def matmul(A, B):
    ret = [[0, 0],
           [0, 0]]
    ret[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD
    ret[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
    ret[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD
    ret[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD

    return ret


def fibo(n):
    ans = [[1, 1], [1, 0]]
    count = 2

    while n > 0:
        block = [[1, 1], [1, 0]]
        while n - count >= 0:
            block = matmul(block, block)
            count *= 2
        ans = matmul(ans, block)
        n -= count // 2
        count = 2
    return ans[1][1]


print(fibo(int(input())))
