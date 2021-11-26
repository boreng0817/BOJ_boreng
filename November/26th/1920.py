from sys import stdin, stdout
"""
Python
1920번 수 찾기
Set
"""

N = int(stdin.readline())
arr = set(stdin.readline().split())
M = stdin.readline()

for n in stdin.readline().split():
    stdout.write("1\n" if n in arr else "0\n")
