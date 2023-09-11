'''
구간 합 구하기
* 구간 합 공식 (i 에서 j까지 구간 합)
--> S[j] - S[i-1] (합 배열을 따로 생성)
'''

import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())  # 데이터 갯수, 질의 갯수
numbers = list(map(int, input().split())) # 구간 합을 구할 대상 배열

prefix_sum = [0] # 만들 합 배열
temp=0

# 합배열 생성
for i in numbers:
    temp = temp +i
    prefix_sum.append(sum)

for i in range(quizNo):
    s,e = map(int,input().split())
    print(prefix_sum[e]-prefix_sum[s-1])