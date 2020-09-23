# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def bfs(v):
            queue = collections.deque([root])
            
            while queue:
                discovered = []
                for _ in range(len(queue)):
                    v = queue.popleft()
                    
                    if v and v not in discovered:
                        discovered.append(v.val)
                        
                        if v.left:
                            queue.append(v.left)
                        if v.right:
                            queue.append(v.right)
                            
                result.append(discovered)
        
        if not root:
            return []
        
        result = []
        bfs(root)
        
        return result