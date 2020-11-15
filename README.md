## 그리디
* 글로벌 최적을 찾기 위해 각 단계에서 로컬 최적의 선택을 하는 알고리즘
* 최적해를 찾을 수도 있고, 그렇지 않으면 최적에 가까운 해를 찾는다.

#### 어떤 문제에 사용해야할까?
* 최적화 문제 ex) 다익스트라, 허프만 코딩
* 그 중에서도 그리디 알고리즘으로 최적해가 보장되기 위해서는 2가지를 만족해야 한다.
  1. 탐욕 선택 속성 : 앞의 선택이 이후 선택에 영향을 주지 않는 것 (다시 고려하지 않음)
  2. 최적 부분 구조 : 문제의 최적 해결 방법이 부분 문제에 대한 최적 해결 방법으로 구성되는 것


## 기타
* 이차원 배열에서 column별로 볼때는 zip을 이용한다.
``` A = [[1,2,3], [4,5,6], [7,8,9]]
for col in zip(*A):
    print(col) # (1,4,7) (2,5,8) (3,6,9)
```

* 단조 감소 배열인지 확인
```
all(x>=y for x, y in zip(L, L[1:]))
```

