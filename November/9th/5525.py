"""
Python
5525번 IOIOI
string
"""
n = int(input())
length = int(input())
string = input()
match = 0
count = 0
i = 0

for _ in range(length):
    if "IOI" == string[i:i+3]:
        match += 1
        i += 1
    else:
        match = 0
    if match == n:
        count += 1
        match -= 1

    i += 1

print(count)
