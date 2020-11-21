class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        counter = collections.Counter(nums)
        for _ in range(len(nums) // k):
            # find k consecutive numbers
            candi = sorted(counter.items(), key=lambda x:(x[0],x[1]))[:k]
            if len(candi) < k:
                return False
            
            if not all(a[0] == b[0] - 1 for a, b in zip(candi, candi[1:])):
                return False
            
            for key, _ in candi:
                counter[key] -= 1
            counter += collections.Counter()
        
        return True
            