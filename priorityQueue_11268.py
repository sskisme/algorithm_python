from queue import PriorityQueue                 
# 데이터가 새로 삽입될 때마다 절댓값과 관련된 정렬이 필요하므로 우선순위 큐로 문제 해결 !! ★
import sys
print = sys.stdout.write
input = sys.stdin.readline
N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else :
            temp = myQueue.get()                    # get() 메소드 이용
            print(str((temp[1]))+'\n')              # 절댓값이 아닌 원래의 값 가져와야하므로 temp[1]
    else:
        myQueue.put((abs(request), request))        # 절댓값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성 ★
