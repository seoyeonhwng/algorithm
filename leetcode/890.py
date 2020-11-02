class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def convert(word):
            table = {}
            count, converted = 0, ''
            
            for w in word:
                if w in table:
                    converted += table[w]
                else:
                    converted += str(count)
                    table[w] = str(count)
                    count += 1
            return converted
        
        p = convert(pattern)
        answer = []
        for word in words:
            if p == convert(word):
                answer.append(word)
        
        return answer

"""
[빠른 풀이]
- zip을 이용해서 길이만 비교!!!

class Solution:
    def findAndReplacePattern(self, w: List[str], p: str) -> List[str]:
					return [i for i in w if len(set(zip(p,i)))==len(set(p))==len(set(i))]
"""