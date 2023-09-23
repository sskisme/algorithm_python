import sys
input = sys.stdin.readline
N = int(input())                     # N 개의 수 
Result = 0
A = list(map(int, input().split()))  # 주어진 수를 리스트에 담음
A.sort()                             # 오름차순 정렬

for k in range(N) : 
    find = A[k] 
    i = 0                            # 양 끝에서 투 포인터 시작
    j = N - 1
    while i < j:
        if A[i] + A[j] == find:
            if i!=k and j!=k:  # 서로 다른 두 수의 합이므로 K+0 이 더해지는 상황은 예외 처리 해주어야 함.
                Result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i]+A[j] < find:
            i += 1
        else :
            j -= 1