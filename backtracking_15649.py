import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * n
result = []

def backtracking(k, n, m):
    if k == m:
        print(*result)
        return
    
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            result.append(i+1)
            backtracking(k+1, n, m)
            visited[i] = False
            result.pop()

backtracking(0, n, m)