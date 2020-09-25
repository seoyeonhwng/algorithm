class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # subarray[L..R] = pref[R] - pref[L-1]
        # subarray[L..R] == k!
        # pref[L-1] = pref[R] - k
        
        answer = 0
        pref = 0
        counter = collections.defaultdict(int)
        counter[0] += 1
        
        for n in nums:
            pref += n
            need = pref - k
            answer += counter[need]
            counter[pref] += 1

        return answer