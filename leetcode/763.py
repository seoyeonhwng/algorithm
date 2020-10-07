class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        index = collections.defaultdict(list)
        for i, c in enumerate(S):
            index[c].append(i)
    
        left, right, i = 0, 0, 0
        answer = []
        
        while left < len(S):
            right = index[S[left]][-1]
            
            while left < right:
                if index[S[left]][-1] > right:
                    right = index[S[left]][-1]
                left += 1
            
            answer.append(right - i + 1)
            i, left = left + 1, right + 1
        
        return answer

"""
[빠른 풀이]
- 문제 풀이 아이디어는 맞았는데 내 풀이에 쓸데없는 과정이 많이 들어갔다ㅠㅠ
- i == j일때가 구간 끝이라는 것을 알아내지 못함

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c:i for i, c in enumerate(S)}
        
        j, anchor = 0, 0
        answer = []
        
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                answer.append(j - anchor + 1)
                anchor = i + 1
                
        return answer
"""