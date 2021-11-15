"""
Python
2164번 카드2
Implementation
"""
n = int(input())
arr = list(range(1,n + 1))

while len(arr) != 1:
    size = len(arr)
    arr = arr[1::2]

    if size % 2 == 1 and len(arr) != 1:
        arr = arr[1:] + arr[:1]

print(arr[0])
