import sys
from collections import deque

N = int(input())

graph = []
visited = [[0]*N for _ in range(N)]
count = 0
result = []

for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))



def dfs(i,j):
    global count
    if i<0 or i>=N or j<0 or j>=N:
        return

    if visited[i][j] == 0 and graph[i][j]==1:
        visited[i][j] = 1
        count += 1
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i+1,j)
        dfs(i,j-1)




for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j]==0:
            count = 0
            dfs(i,j)
            result.append(count)

print(len(result))
result.sort()
for i in result:
    print(i)


