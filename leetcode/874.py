class Solution:
    answer = 0
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def turn_direction(direction, cmd):
            if cmd == -2: # left
                if direction == 'u':
                    return 'l'
                if direction == 'l':
                    return 'd'
                if direction == 'd':
                    return 'r'
                if direction == 'r':
                    return 'u'
            else:
                if direction == 'u':
                    return 'r'
                if direction == 'r':
                    return 'd'
                if direction == 'd':
                    return 'l'
                if direction == 'l':
                    return 'u'
        
        def move(pos, cmd, direction):
            m = {'u': (0,1), 'd':(0,-1), 'l':(-1,0), 'r':(1,0)}
            unit = m[direction]
            
            for i in range(cmd):
                if (pos[0]+unit[0], pos[1]+unit[1]) in obstacles:
                    return pos
                pos = (pos[0]+unit[0], pos[1]+unit[1])
                self.answer = max(self.answer, pos[0] ** 2 + pos[1] ** 2)
            return pos
                    
        direction, pos = 'u', (0, 0)
        obstacles = set(map(tuple, obstacles))
        
        for cmd in commands:
            if cmd in [-1, -2]:
                direction = turn_direction(direction, cmd)
            else:
                pos = move(pos, cmd, direction)

        return self.answer

"""
* 멤버십 체크는 set으로 하면 속도가 빠르기 때문에 obstacles를 set으로 바꿔주는 작업 필수!
* 이차원 배열에서 방향성까지 고려해서 움직일때
di = [0, 1, 2, 3] # 'up', 'right', 'down', 'left'
di = (di - 1) % 4 # 왼쪽 회전
di = (di + 1) % 4 # 오른쪽 회전

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

[빠른 풀이]
class Solution:
    answer = 0
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        di, answer = 0, 0
        x, y = 0, 0
        obstacles = set(map(tuple, obstacles))
        
        for cmd in commands:
            if cmd == -2:
                di = (di - 1) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacles:
                        x += dx[di]
                        y += dy[di]
                        answer = max(answer, x ** 2 + y ** 2)
        return answer
"""