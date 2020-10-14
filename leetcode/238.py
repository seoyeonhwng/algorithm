class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        out = []
        
        # 왼쪽 곱셈
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
            
        return out