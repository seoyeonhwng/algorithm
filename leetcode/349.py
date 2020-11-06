class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        
        nums1.sort()
        nums2.sort()
        i = j = 0
        
        # 투 포인터를 오른쪽으로 이동하며 일치 여부를 판별
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        
        return result