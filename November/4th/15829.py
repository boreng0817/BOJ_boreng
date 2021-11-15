import sys
"""
python
15829번 Hashing
Hash, Horner's method
"""

A = ord('a') - 1
r = 31
M = 1234567891
n = int(sys.stdin.readline())
string = input()

ret = 0


for a in string[::-1]:
    ret *= r
    ret += ord(a) - A
    ret %= M

print(ret % M)
