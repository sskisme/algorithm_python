'''
구간합(i~j)이 M으로 나누어 떨어질 때 
( Sj - Si ) % M = 0 

Sj % M 값과 Si % M 값이 동일하다고 볼 수 있음. 
나머지가 같은 경우의 수 모두 찾기 !! 
'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = list(map(int,input().split()))
S = [0] * n                         # 합 리스트 
C = [0] * m                         # 같은 나머지를 카운트하는 리스트
S[0] = A[0]     
result = 0                          # 정답

for i in range(1,n):
    S[i] = S[i-1]+A[i]              # 합 배열 만들기 공식

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        result +=1                  # 나머지가 0일 때 0부터 n 값까지의 합이 나누어 떨어짐.
    C[remainder] +=1                # 나머지 같은 인덱스 개수 값 증가

for i in range(m):
    if C[i] > 1:
        result += (C[i]*(C[i]-1)//2) # 조합 공식

print(result)

