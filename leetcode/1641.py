class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = collections.defaultdict(list)
        dp[1] = ['a', 'e', 'i', 'o', 'u']
        
        for i in range(2, n+1):
            for elem in dp[i-1]:
                for v in ['a', 'e', 'i', 'o', 'u']:
                    if elem[-1] <= v:
                        dp[i].append(elem+v)
       
        return len(dp[n])
                        
"""
[빠른 풀이]
- 개수만 알면 되니까 마지막으로 끝나는 문자별로 개수를 저장한다

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = collections.defaultdict(list)
        dp[1] = [1, 1, 1, 1, 1] # ['a', 'e', 'i', 'o', 'u']
        
        for i in range(2, n+1):
            s = 0
            for e in dp[i-1]:
                s += e
                dp[i].append(s)
        
        return sum(dp[n])
"""