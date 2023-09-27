N = int(input())            # 수열 개수
A = [0] * N
for i in range(N):
    A[i] = int(input())     # 수열 리스트 채우기 

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i]
    if su >= num:
        while su >= sum:    # 현재 수열 값 >= 오름차순 자연수 : 값이 같아질 때까지 append() 수행
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()         # 같아질 때 pop() 실행
        answer += "-\n"
    else:                    # 현재 수열 값 < 오름차순 자연수 : pop()을 수행해 수열 원소를 꺼냄 
        n = stack.pop()
        # 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열을 출력할 수 있음 
        if n > su:
            print("NO")     # 후입선출 불가
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)