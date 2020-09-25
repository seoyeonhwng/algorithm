# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def pathSum(self, root: TreeNode, target: int) -> int:
        def dfs(node, path): 
            if not node:
                return
            
            if sum(path) == target:
                self.count += 1
            
            if node.left:
                dfs(node.left, path + [node.left.val])
            if node.right:
                dfs(node.right, path + [node.right.val])
        
        
        if not root:
            return 0
        
        stack = [root]
        while stack:
            v = stack.pop()
            dfs(v, [v.val])
            if v.left:
                stack.append(v.left)
            if v.right:
                stack.append(v.right)
                
        return self.count
            
"""
[빠른 풀이]
- targets : 만약 node.val이 여기 안에 있다면 찾는 path야
- 이러한 역할을 하는 targets를 계속 갱신하면서 dfs 한다

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def pathSum(self, root: TreeNode, k: int) -> int:
        def dfs(node, targets): 
            if not node:
                return 0
            
            new_targets = [targets[0]] + [t - node.val for t in targets]
            return targets.count(node.val) + dfs(node.left, new_targets) + dfs(node.right, new_targets)
        
        return dfs(root, [k])
"""