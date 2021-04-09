# Checking if a binary tree is a perfect binary tree in Python
from binarytree import Node, tree, bst, heap, build


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


# This function traverse the skewed binary tree and
# stores its nodes pointers in vector nodes[]
def storeBSTNodes(root, nodes):

    # Base case
    if not root:
        return

    # Store nodes in Inorder
    storeBSTNodes(root.left, nodes)
    nodes.append(root)
    storeBSTNodes(root.right, nodes)


# Recursive function to construct binary tree
def balanceTreeUtil(nodes, start, end):

    # base case
    if start > end:
        return None

    # Get the middle element and make it root
    mid = (start+end)//2
    node = nodes[mid]

    # Using index in Inorder traversal, construct
    # left and right subtress
    node.left = balanceTreeUtil(nodes, start, mid-1)
    node.right = balanceTreeUtil(nodes, mid+1, end)
    return node


# This functions converts an unbalanced BST to
# a balanced BST
def balanceTree(root):

    # Store nodes of given BST
    nodes = []
    storeBSTNodes(root, nodes)
    
    # Sort nodes
    vals = [n.value for n in nodes]
    nodes = [Node(val) for val in sorted(vals)]
    
    # Constucts BST from nodes[]
    n = len(nodes)
    return balanceTreeUtil(nodes, 0, n-1)


# Driver code
if __name__ == '__main__':
    height = int(input("Enter height of Tree: "))
    vals = enterVals(height)
    root = perfectTree(0, vals)
    root.left.left = Node(1)
    root.left.left.left = Node(2)
    root.left.left.left.left = Node(3)
    root.left.left.left.left.left = Node(4)

    if (is_perfect(root, calculateDepth(root))):
        print("The tree is a perfect binary tree")
    else:
        print("The tree is not a perfect binary tree")

    print(root)

    root = balanceTree(root)

    if (is_perfect(root, calculateDepth(root))):
        print("The tree is a perfect binary tree")
    else:
        print("The tree is not a perfect binary tree")
    print(root)
