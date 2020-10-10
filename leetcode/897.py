# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node.left:
                inorder(node.left)
                
            path.append(node.val)
            
            if node.right:
                inorder(node.right)
                
        path = []
        inorder(root)
        
        p = TreeNode(path[0])
        new_tree = p
        
        for i in range(1, len(path)):
            p.right = TreeNode(path[i])
            p = p.right
            
        return new_tree