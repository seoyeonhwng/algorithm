class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 너비 * 높이가 최대!
        # 너비가 최대인 상태에서 너비를 줄이면서 확인한다!
        left = 0
        right = len(height) - 1
        max_area = -sys.maxsize
        
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, w * h)
            
            if h == height[left]:
                left += 1
            else:
                right -= 1
                
        return max_area
            