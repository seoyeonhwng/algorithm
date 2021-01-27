class Tree:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def preorder(node):
    print(node.val, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.val, end='')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.val, end='')

N = int(input())
tree = {}

for _ in range(N):
    node, left, right = input().split(' ')
    tree[node] = Tree(node, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])