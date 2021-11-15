import sys
"""
Python
1991번 트리 순회
Binary tree traversal problem
"""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

tree = {}
n = int(input())
for _ in range(n):
    node, l_child, r_child = sys.stdin.readline().split()
    l_child = l_child if l_child in alphabet else None
    r_child = r_child if r_child in alphabet else None

    tree[node] = [l_child, r_child]

def preorder(node):
    if node is None:
        return ""

    return node + preorder(tree[node][0]) + preorder(tree[node][1])


def postorder(node):
    if node is None:
        return ""

    return postorder(tree[node][0]) + postorder(tree[node][1]) + node


def inorder(node):
    if node is None:
        return ""

    return inorder(tree[node][0]) + node + inorder(tree[node][1])

print(preorder("A"))
print(inorder("A"))
print(postorder("A"))
