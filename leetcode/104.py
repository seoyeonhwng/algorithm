# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = collections.deque([root])
        
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                v = queue.popleft()
                if v.left:
                    queue.append(v.left)
                if v.right:
                    queue.append(v.right)
        
        return depth
            
     