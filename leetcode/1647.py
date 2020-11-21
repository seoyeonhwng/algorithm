class Solution:
    def minDeletions(self, s: str) -> int:
        counter = collections.Counter(s)
        freq = defaultdict(list)
        for k, v in counter.items():
            freq[v].append(k)
        
        answer = 0
        for k, v in freq.items():
            if len(v) == 1:
                continue
            
            for element in v[1:]:
                # 가장 적게 삭제!
                count = counter[element]
                while count > 0 and count in set(counter.values()):
                    count -= 1
                
                answer += (counter[element] - count)
                counter[element] = count
        
        return answer

"""
[빠른 풀이]
- freq를 저장하는 set만 유지해도 됨!!!

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt, res, used = collections.Counter(s), 0, set()
        for ch, freq in cnt.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return resㄴ
"""