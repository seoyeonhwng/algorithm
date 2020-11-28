class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        not_judge = set()
        trust_cnt = collections.defaultdict(int)
        for a, b in trust:
            not_judge.add(a)
            trust_cnt[b] += 1

        for i in range(1, N+1):
            if i in not_judge:
                continue
            if trust_cnt[i] == N - 1:
                return i
        return -1
        
"""
- 지목을 하면 -, 지목을 당하면 +로만 해도 구분할 수 있음!

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        score = collections.defaultdict(int)
        for a, b in trust:
            score[a] -= 1
            score[b] += 1
        
        for i in range(1, N+1):
            if score[i] == N - 1:
                return i
        return -1
        
"""