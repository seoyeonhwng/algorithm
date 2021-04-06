from bisect import bisect_left, bisect_right
from collections import defaultdict

def solution(words, queries):
    infos = defaultdict(list)
    r_infos = defaultdict(list)
    for w in words:
        len_w = len(w)
        infos[len_w].append(w)
        r_infos[len_w].append(w[::-1])
    
    for i in range(10001):
        infos[i].sort()
        r_infos[i].sort()

    ans = []
    for query in queries:
        length = len(query)
        candi = r_infos[length] if query[0] == '?' else infos[length]
        query = query[::-1] if query[0] == '?' else query

        start = query.replace('?', 'a')
        end = query.replace('?', 'z')
        count = bisect_right(candi, end) - bisect_left(candi, start)
        ans.append(count)
    return ans

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))