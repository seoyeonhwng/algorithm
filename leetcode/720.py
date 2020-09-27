class Solution:
    def longestWord(self, words: List[str]) -> str:
        longest = -sys.maxsize
        result = []
        prefix = set()
        
        for word in sorted(words):
            if len(word) == 1:
                prefix.add(word)
            elif prefix and word[:len(word)-1] in prefix:
                if len(word) > longest:
                    longest = len(word)
                    result = [word]
                elif len(word) == longest:
                    result.append(word)
                prefix.add(word)
                
        if not result:
            return list(prefix)[0]
        return sorted(result)[0]

"""
[빠른 풀이]
- 정렬을 했기 때문에 >로 비교하면 순서 보장
- prefix에 ''을 넣고 시작하면 word의 길이가 1인 경우도 한번에 해결된다!

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        prefix = set([""])
        answer = ''
        
        for word in words:
            if word[:-1] in prefix:
                if len(word) > len(answer):
                    answer = word
                prefix.add(word)
                
        return answer
"""