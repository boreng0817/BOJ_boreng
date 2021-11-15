from collections import deque
"""
Python
9935번 문자열 폭발
Stack
"""

string = deque(input())
bomb = input()
stack = deque()
index = 0

while len(string):
    ch = string.popleft()
    stack.append(ch)
    if ch == bomb[index]:
        index += 1
    else:
        index = 0
        if ch == bomb[index]:
            index = 1
    if index == len(bomb):
        for i in range(index):
            stack.pop()
        for i in range(min(len(stack), len(bomb))):
            ch = stack.pop()
            string.appendleft(ch)
            if ch == bomb[0]:
                break
        index = 0

answer = "".join(stack)
if len(answer):
    print(answer)
else:
    print("FRULA")
