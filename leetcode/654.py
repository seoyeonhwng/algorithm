# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def sub_construct(array):
            if not array:
                return
            
            # divide
            pivot = array.index(max(array))
            l = array[:pivot]
            r = array[pivot+1:]
            
            # conquer
            left = sub_construct(l)
            right = sub_construct(r)
            
            # combine
            return TreeNode(array[pivot], left, right)
        
        return sub_construct(nums)

"""
[divide & conquer 문제]

1) divide (작은 문제로 분할)
2) conquer (작은 문제 각각 해결)
- return 조건에 맞을때까지 재귀 호출
3) combine (해결한 작은 문제를 합친다)
"""