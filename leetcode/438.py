class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # window = len(p)
        # 속도를 위해 sort하지 않고 counter를 이용한다!
        
        window = len(p)
        target = collections.Counter(p)
        answer = []
        
        for i in range(len(s)-window+1):
            if i == 0:
                candidate = collections.Counter(s[:window])
            else:
                candidate[s[i-1]] -= 1
                candidate[s[i+window-1]] += 1
                
            if len(target - candidate) == 0:
                answer.append(i)
          
            
        return answer
        