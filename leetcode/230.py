# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def travel(node):
            if not node:
                return
            
            heapq.heappush(heap, node.val)
            travel(node.left)
            travel(node.right)
            
        heap = []
        travel(root) # 전위순회로 힙에 다 넣는다
        
        for _ in range(k - 1):
            heapq.heappop(heap)
        return heap[0]
        
# k번째 작은 원소 = 중위 순회에서 k번째 원소  
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        return inorder(root)[k - 1]