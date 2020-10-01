class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        info = collections.defaultdict(list)
        for i, e in enumerate(groupSizes):
            info[e].append(i)
        
        answer = []
        for key, value in info.items():
            if key == len(value):
                answer.append(value)
            else:
                # divide! 
                while value:
                    answer.append(value[:key])
                    value = value[key:]
                    
        return answer