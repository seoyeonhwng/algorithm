class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1. (1, n-1), (2, n-2) ... 모든 조합
        # 2. ( + n-1의 모든 요소 + )
        
        def sub_generate(num):
            # num개로 만들수 있는 조합을 구해서 memo에 저장한다.
            if num == 1:
                memo[num] = set(['()'])
                return
            
            # 가능한 모든 조합을 구한다
            combination = []
            for i in range(1, num):
                combination.append([i, num - i])

            for a, b in combination:
                for m1 in memo[a]:
                    for m2 in memo[b]:
                        memo[num].add(m1 + m2)
                        memo[num].add(m2 + m1)
            
            for m in memo[num - 1]:
                memo[num].add('(' + m + ')')
                              
        
        memo = collections.defaultdict(set)
        for i in range(1, n+1):
            sub_generate(i)
        
        return list(memo[n])
            
# dfs를 이용해서 풀 수 도 있다!