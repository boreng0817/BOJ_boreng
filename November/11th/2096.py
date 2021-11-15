import sys
"""
Python
2096번 내려가기
DP
"""
n = int(sys.stdin.readline())
_max = list(map(int, sys.stdin.readline().split()))
_min = _max[:]

for i in range(n - 1):
    val = list(map(int, sys.stdin.readline().split()))
    temp_max = _max[:]
    _max[0] = max(val[0] + temp_max[0], val[0] + temp_max[1])
    _max[1] = max(val[1] + temp_max[0], val[1] + temp_max[1], val[1] + temp_max[2])
    _max[2] = max(val[2] + temp_max[1], val[2] + temp_max[2])
    temp_min = _min[:]
    _min[0] = min(val[0] + temp_min[0], val[0] + temp_min[1])
    _min[1] = min(val[1] + temp_min[0], val[1] + temp_min[1], val[1] + temp_min[2])
    _min[2] = min(val[2] + temp_min[1], val[2] + temp_min[2])

print(max(_max), min(_min))
