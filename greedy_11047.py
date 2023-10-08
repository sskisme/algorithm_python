# 1. 계산대 안에 있는 돈의 수와 거슬러 줄 돈을 구합니다.
N, K = map(int, input().split()) # N : 화폐 종류수, K : 거슬러 줄 돈

# 2. 계산대에 있는 화폐들을 리스트의 형태로 입력받습니다.
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)
# coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

# 3. 만약 '계산대 안에 있는 화폐'보다 '거슬러 줄 돈'이 크다면
# 돈을 거슬러 줍니다.
answer = 0
for coin in coins:
    if K >= coin:
        answer += K // coin #몫만큼 더하기
        K %= coin #나머지 할당
        if K <= 0: # 만약 K가 0이면 반복문을 탈출합니다.
       		break
print(answer) # 거슬러 준 동전 + 화폐의 수