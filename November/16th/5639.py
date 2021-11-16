import sys
"""
Pyhton
5639번 이진 검색 트리
BST, tree traversal
"""
# Set max recursion depth
sys.setrecursionlimit(10**9)


def make_node(n):
    ret = dict(val=n,
               right=None,
               left=None)
    return ret


def insert(T, n):
    node = T
    parent = node
    while node is not None:
        parent = node
        if node['val'] < n:
            node = node['right']
        else:
            node = node['left']

    if parent is None:
        return make_node(n)
    else:
        if parent['val'] > n:
            parent['left'] = make_node(n)
        else:
            parent['right'] = make_node(n)
        return T


def post(T):
    if T is None:
        return
    post(T['left'])
    post(T['right'])
    print(T['val'])


T = None

while True:
    num = sys.stdin.readline()
    try:
        num = int(num)
    except:
        break
    T = insert(T, num)

post(T)
