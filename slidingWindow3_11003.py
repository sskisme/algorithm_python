from collections import deque
N, L = map(int, input().split())
mydeque = deque()       # N, L 의 최대 범위가 5,000,0000 이므로 정렬을 사용할 수 없음.
                        # 자동으로 정렬이 되는 덱 자료구조 이용 !! ★
                        
now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]: #mydeque 존재해야하고 넣는 값보다 큰수는 제거 /// [-1][0] ==> 맨 오른쪽 데이터 값 의미 
        mydeque.pop()                          # 오른쪽 제거
    mydeque.append((now[i],i))                  # 현재 데이터 값과 인덱스 덱에 추가
    if mydeque[0][1] <= i - L :                 # /// [0][1] ==> 맨 왼쪽 인덱스 의미 
        mydeque.popleft()                       # 왼쪽 제거
    print(mydeque[0][0], end=' ')



