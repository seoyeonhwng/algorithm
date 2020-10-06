# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def travel(p):
            if not p:
                return
            
            heapq.heappush(heap, p.val)
            if p.left:
                travel(p.left)
            if p.right:
                travel(p.right)
        
        heap = []
        travel(root1)
        travel(root2)
        
        answer = []
        while heap:
            answer.append(heapq.heappop(heap))
                          
        return answer
        
"""
[빠른 풀이]
- 이 문제의 핵심은 'binary search tree에서 inorder travel을 하면 오름차순으로 방문'
- 따라서 두개의 트리를 inorder한 후 하나씩 값을 비교하면서 merge


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node, lst):
        if not node:
            return
        
        self.inorder(node.left, lst)
        lst.append(node.val)
        self.inorder(node.right, lst)
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr1, arr2 = collections.deque(), collections.deque()
        self.inorder(root1, arr1)
        self.inorder(root2, arr2)
        
        # merge two arr
        answer = []
        while arr1 and arr2:
            answer.append(arr1.popleft() if arr1[0] < arr2[0] else arr2.popleft())
            
        return answer + list(arr1) + list(arr2)
"""