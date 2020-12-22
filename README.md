*코드 스니펫을 정리합니다.*

## 플로이드 와샬
* 그래프에서 가능한 모든 노드 쌍에 대한 최단 거리를 구할때 사용한다. (N * N matrix를 생각하자!)
```
1. N * N matrix 선언 (N = 정점의 개수)

2. 노드 간의 거리 표시

3. 최단 거리 계산
for k in range(N):
  for i in range(N):
    for j in range(N):
      if matrix[i][j] > matrix[i][k] + matrix[k][j]:
        matrix[i][j] = matrix[i][k] + matrix[k][j]
```

## 이차원 배열
* 이차원 배열에서 column별로 볼때는 zip을 이용한다.
``` 
A = [[1,2,3], [4,5,6], [7,8,9]]
for col in zip(*A):
    print(col) # (1,4,7) (2,5,8) (3,6,9)
```

* 이차원 배열 모든 원소 합
```
from itertools import chain

A = [[1,2,3], [4,5,6], [7,8,9]]
total_sum = sum(chain(*A)) # chain은 리스트를 연결해줌
```


* 이차원 배열 탐색
```
di = [0, 1, 2, 3] # 'up', 'right', 'down', 'left'
di = (di - 1) % 4 # 왼쪽 회전
di = (di + 1) % 4 # 오른쪽 회전

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
(x, y) -> (x + dx[di], y + dy[di])로 이동
```

## counter
* 값이 0이하인 원소 없애기
```
counter += collections.Counter() # 빈 counter를 더한다
```

## 기타
* 단조 감소 배열인지 확인
```
all(x>=y for x, y in zip(L, L[1:]))
```

