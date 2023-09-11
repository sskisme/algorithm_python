import sys
input = sys.stdin.readline
n,m = map(int, input().split())
A = [[0]*(n+1)] # 길이가 n+1 인 1차원 배열 생성 ==> [[0,0,0,0 ~ ]]
D = [[0]*(n+1) for _ in range(n+1)] # 길이가 (n+1) * (n+1) 인 2차원 배열 생성 [[0,0,0,0],[0,0,0,0],[0,0,0~]]

for i in range(n):
    A_row = [0]+[int(x) for x in input().split()]  #[0,1,2,3] --> 0 이후에는 입력한 값 차례대로 들어감
    A.append(A_row) # 한 줄씩 append 

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j]= D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j] # 2차원 합배열 구하는 공식 

for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    result = D[x2][y2]- D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1] # 2차원 구간합 공식
