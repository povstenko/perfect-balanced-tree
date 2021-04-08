# Checking if a binary tree is a perfect binary tree in Python
from binarytree import Node, tree, bst, heap


# Calculate the depth
def calculateDepth(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.left
    return d


# Check if the tree is perfect binary tree
def is_perfect(root, d, level=0):

    # Check if the tree is empty
    if (root is None):
        return True

    # Check the presence of trees
    if (root.left is None and root.right is None):
        return (d == level + 1)

    if (root.left is None or root.right is None):
        return False

    return (is_perfect(root.left, d, level + 1) and
            is_perfect(root.right, d, level + 1))


def perfectTree(i, vals):
    if i < len(vals):
        return Node(vals[i],
                    left=perfectTree((i+1)*2-1, vals),
                    right=perfectTree((i+1)*2, vals))


def enterVals(height, lvl=0, n=1):
    vals = []
    for i in range(lvl, height):
        print(f"level: {lvl}, nodes: {n}")
        for i in range(n):
            vals.append(int(input(f"{i}: ")))
        n = n*2
    return vals


height = int(input("Enter height of Tree: "))
vals = enterVals(height)
root = perfectTree(0, vals)

if (is_perfect(root, calculateDepth(root))):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")

print(root)
