'''
새로 들어온 문자열, 제거되는 문자열만 반영하여 확인하는 것이 핵심 !!!
'''

checkList = [0]*4    # A, C, G, T 의 최소 개수가 들어있는 체크리스트 
myList = [0]*4       # 슬라이딩  윈도우(부분 문자열)에 들어있는 A, C, G, T  갯수
checkSecret = 0      # 각 문자가 충족될 때 증가되는 변수 (최대 4)

def myadd(c):        # 슬라이딩 시 새로 들어온 문자 처리 함수
    global checkList, myList, checkSecret   # 전역변수 이용 
    if c == 'A':                            # 새로 들어온 문자가 A 일 때  
        myList[0] += 1                      # myList 0번 인덱스 값 1 증가
        if myList[0] == checkList[0]:       # 증가 후 checklist 값과 같을 때 
            checkSecret += 1                # checkSecret 값 1 증가
    elif c == 'C':
        myList[1] +=1 
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] +=1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c):    # 슬라이딩 시 제거되는 문자 처리 함수
    global checkList, myList, checkSecret   # 전역변수 이용
    if c == 'A':
        if myList[0] == checkList[0]:       # 감소 전 checklist값과 같을 때 
            checkSecret -= 1                # checkSecret 값 1 감소
        myList[0] -= 1                      # myList 0번 인덱스 값 1 증가
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret += 1
        myList[1] +=1 
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret += 1
        myList[2] +=1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret += 1
        myList[3] += 1

S, P = map(int,input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0:       # checklist 값이 0 일 경우 처음부터 만족되었다는 뜻.
        checkSecret += 1 

for i in range(P):              # 초기 P 부분 문자열 처리 부분
    myadd(A[i])

if checkSecret == 4:            # 네 문자열 개수가 모두 충족되었을 때
    Result += 1                 # 정답 개수에 1 증가
    

for i in range(P,S):            # for i in range(2,4) -> 맨 끝 인덱스가 마지막에 도달했을 때 까지 반복문
    j = i - P                   # 0 = 2-2   
    myadd(A[i])                 # myadd(A[2]) 
    myremove(A[j])              # myremove(A[0])
    if checkSecret == 4:
        Result += 1

print(Result)

        