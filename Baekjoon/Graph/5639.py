import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def preorder_to_postorder(nodes):
    if not nodes:
        return

    mid = nodes[0]
    left, right = nodes[1:], []

    for i in range(1, len(nodes)):
        if nodes[i] > mid:
            left = nodes[1:i]
            right = nodes[i:]
            break

    preorder_to_postorder(left)
    preorder_to_postorder(right)
    print(mid)

nodes = []

while True:
    try:
        nodes.append(int(input()))
    except:
        break

preorder_to_postorder(nodes)