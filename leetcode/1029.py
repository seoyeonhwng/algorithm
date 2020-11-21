class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        gap = {i:c[0]-c[1] for i, c in enumerate(costs)}
        n = len(costs) // 2
        A = sorted(gap.items(), key=lambda x:x[1])[:n]
        A_idx = set([a[0] for a in A])
        
        A_sum, B_sum = 0, 0
        for i, c in enumerate(costs):
            if i in A_idx:
                A_sum += c[0]
            else:
                B_sum += c[1]
        return A_sum + B_sum

"""
- 단순히 첫번째 값이 작은 원소를 선택하는 것이 최적이 아니고 
    c[0]-c[1]이 작은 수일수록 A로 선택하는 것이 최적
"""