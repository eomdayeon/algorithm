import sys
from collections import deque

dx = [-1,0,+1,0]
dy = [0,+1,0,-1]

def dfs(x,y):
    if x<0 or y<0 or x>=M or y>=N:   
        return
    if visited[x][y]==1:
        return False

    if visited[x][y]==0 and board[x][y]==1:
        visited[x][y] = 1
        for d in range(4):
            dfs(x+dx[d],y+dy[d])     
        return True

    return False


def bfs(x,y):
    queue = deque()
    queue.append([x,y])

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if board[nx][ny] == 1:
                queue.append([nx,ny])
                board[nx][ny] = 0

    


T = int(input())
for t in range(T):
    count = 0
    M, N, K = map(int,sys.stdin.readline().rstrip().split())

    board = [[0]*N for _ in range(M)]
    visited = [[0]*N for _ in range(M)]


    for i in range(K):
        X, Y = map(int,sys.stdin.readline().rstrip().split())
        board[X][Y] = 1

    for i in range(M):
        for j in range(N):
            if board[i][j] == 1:
                bfs(i,j)
                count += 1
    print(count)


