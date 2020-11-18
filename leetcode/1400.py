class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # count가 홀수인 문자의 수가 k보다 작냐 크냐
        if len(s) < k:
            return False
        
        counter = collections.Counter(s)
        check = [1 if v % 2 == 1 else 0 for v in counter.values()]
        return not sum(check) > k