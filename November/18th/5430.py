import sys
"""
Python
5430번 AC
implementation
"""

T = int(sys.stdin.readline())
for _ in range(T):
    op = sys.stdin.readline().strip()
    length = int(sys.stdin.readline())
    right = left = 0
    count_R = 0

    for ch in op:
        if ch == 'R':
            count_R += 1
        else:
            if count_R % 2 == 0:
                left += 1
            else:
                right += 1

    if left + right > length:
        print("error")
        sys.stdin.readline()
    else:
        arr = sys.stdin.readline()[1:-2].split(',')
        if count_R % 2 == 0:
            print("[" + ",".join(arr[left:length-right]) + "]")
        else:
            print("[" + ",".join(arr[left:length - right][::-1]) + "]")
