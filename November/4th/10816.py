"""
Python
10816번 숫자 카드 2
map
"""
def main():
    a = {}
    
    # garbage line
    input()
    
    for num in input().split():
        if not num in a:
            a[num] = 0
        a[num] += 1
    
    # garbage line
    input()
    
    for num in input().split():
        if not num in a:
            print(0, end=" ")
        
        else:
            print(a[num], end=" ")

if __name__ == "__main__":
    main()
