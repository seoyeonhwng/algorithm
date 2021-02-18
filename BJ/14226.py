from collections import deque

def bfs():
    queue = deque([(1, 0, 0)]) # 화면, 클립보드, 초
    visited = set([(1, 0)]) # 화면, 클립보드

    while queue:
        monitor, clip, count = queue.popleft()
        if monitor == S:
            return count

        # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
        if (monitor, monitor) not in visited:
            queue.append((monitor, monitor, count + 1))
            visited.add((monitor, monitor))
        # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 
        if clip > 0 and (monitor + clip, clip) not in visited:
            queue.append((monitor + clip, clip, count + 1))
            visited.add((monitor + clip, clip))
        # 화면에 있는 이모티콘 중 하나를 삭제
        if monitor > 0 and (monitor-1, clip) not in visited:
            queue.append((monitor-1, clip, count + 1))
            visited.add((monitor-1, clip))


S = int(input())
# 1에서 S까지의 최단 거리 -> bfs!!
print(bfs())