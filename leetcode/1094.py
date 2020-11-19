class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        infos = collections.defaultdict(list)
        for trip in trips:
            infos[trip[1]].append((trip[0], trip[2]))
        
        seats = 0
        incar = collections.defaultdict(int)
        for start, onboard in sorted(infos.items(), key=lambda x:x[0]):
            # v에 있는 인원 다 태워
            for psn, end in onboard:
                seats += psn
                incar[end] += psn
            
            # 내릴 애들 다 내려
            for end, psn in incar.items():
                if end <= start:
                    seats -= psn
                    incar[end] -= psn
                    
            # capacity랑 비교
            if seats > capacity:
                return False
        return True

"""
[빠른 풀이]
- pickup, drop을 언제 몇 명 내려야하는지로 정리 -> 순서대로 처리!

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickup, drop = collections.defaultdict(int), collections.defaultdict(int)
        for psn, start, end in trips:
            pickup[start] += psn
            drop[end] += psn
        
        # sort
        pickup = sorted(pickup.items(), key=lambda x:x[0])
        drop = sorted(drop.items(), key=lambda x:x[0])
        
        time, last_time = 0, drop[-1][0]
        seats = 0
        
        while pickup and drop and time <= last_time:
            if time == pickup[0][0]:
                seats += pickup.pop(0)[1]
            if time == drop[0][0]:
                seats -= drop.pop(0)[1]
            if seats > capacity:
                return False
            time += 1
        return True
"""