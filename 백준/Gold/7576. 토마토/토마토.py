
from collections import deque


M, N = map(int,input().split())

box = []
dx=[-1,0,+1,0]
dy=[0,+1,0,-1]

for i in range(N):
    box.append(list(map(int,input().split())))

queue = deque([])

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i,j])

while queue:
    cx, cy = queue.popleft()
    for k in range(4):
        nx = cx + dx[k]
        ny = cy + dy[k]

        if 0<=nx<N and 0<=ny<M:
            if box[nx][ny] == 0 :
                queue.append([nx,ny])
                box[nx][ny] = box[cx][cy] + 1
            

m = max((map(max,box))) - 1


for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            m = -1
            break
print(m)
