'''
백준 2644_ 촌수 계산 풀이 1)
'''
import sys
input = sys.stdin.readline

n = int(input())
A,B = map(int, input().split())
m = int(input())

# 크기 하나 더 큰 그래프 생성
graph = [[] for _ in range(n+1)]
# 방문 여부 확인 리스트 생성
visited = [False] * (n+1)
res = [0] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    # 서로의 그래프에 노드 추가
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        # 자식으로 뻗어나가는 방향만 있게 함
        if not visited[i]:
            res[i] = res[v] + 1
            dfs(i)

dfs(A)

if res[B]>0:
    print(res[B])
else : 
    print(-1)

