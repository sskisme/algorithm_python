from collections import deque
N = int(input())
myQueue = deque()

for i in range(1, N+1):
    myQueue.append(i)

while len(myQueue) > 1:                 # 카드가 1장 남을 때 까지
    myQueue.popleft()
    myQueue.append(myQueue.popleft())

print(myQueue[0])                       # 마지막 남은 카드 출력