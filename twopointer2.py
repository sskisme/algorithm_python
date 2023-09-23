'''
두 숫자의 합이 특정한 수를 만들게 함. 
두 포인터가 양 끝에서 시작해서 점차 가운데로 모여지는 방법
-> 처음에 오름차순으로 정렬 해주어야함.
'''
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
A = list(map(int,input().split()))
A.sort()
count = 0
i = 0
j = N-1

while i < j: # 양끝에서 시작할 경우 조건식을 이렇게 사용
    if A[i] + A[j] < M:     # 두 수 합이 입력한 값보다 작을 때 
        i+=1                # 시작 포인터 증가
    elif A[i] + A[j] > M:   # 두 수 합이 입력한 값보다 클 때
        j-=1                # 끝 포인터 감소
    else:                   # 두 수 합이 입력한 값과 같을 때 
        count +=1           # count 증가
        i +=1               # 시작, 끝 포인터 감소
        j -=1

print(count)