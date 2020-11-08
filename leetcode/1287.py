class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        target = len(arr) // 4

        counter = collections.Counter(arr)
        for k, v in counter.items():
            if v > target:
                return k