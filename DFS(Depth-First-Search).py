'''
● DFS
- 스택 자료구조(혹은 재귀 함수) 이용
- 동작 과정
1. 탐색 시작 노드를 스택에 삽입하고 방문처리
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리합니다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.
'''
# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],          # 0번 노드 존재 x
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)

# 정의된 DFS 함수 호출
dfs(graph, 1, visited) # 1 2 7 6 8 3 4 5

'''
문제 알고리즘
1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0' 이면서 아직 방문하지
않은 지점이 있다면 해당 지점 방문
2. 방문한 지점에서 다시 상,하,좌,우 를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점 방문할 수있음
3. 모든 노드에 대하여 1 ~ 2 번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트합니다. 

'''
n,m = map(int, input().split())

ice_board = []
for i in range(n):
    ice_board.append(list(map(int,input())))

# 상하좌우 진행용 방향 리스트
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 아이스크림 개수
count = 0 

# dfs 를 통해 현재 노드를 방문한 뒤, 연결된 모든 노드들을 방문
def dfs(start_x, start_y):

    # 현재 노드를 방문 처리
    ice_board[start_x][start_y] = 1

    #현재 노드와 인접한 노드들을 탐색하며, 방문 가능할 경우 방문
    for i in range(4):

        # 인접 노드 좌표
        nx = start_x + dx[i]
        ny = start_y + dy[i]

        # 인접 노드가 얼음판 내부에 위치할 경우
        if(nx >= 0 and nx < n and ny >= 0 and ny <m):

            # 인접 노드에 음료수를 채울 수 있는지 확인
            if(ice_board[nx][ny] == 0):
                # 인접 노드 방문
                dfs(nx, ny)

# 모든 위치에 음료수 채우기
for i in range(n):
    for j in range(m):
        # 해당 노드에 음료수를 채울 수 있다면
        if(ice_board[i][j] ==0):
            # 해당 노드에서 dfs 탐색 시작
            dfs(i,j)
            count += 1

print(count)