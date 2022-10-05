from collections import deque

dx =[-1,0,+1,0]
dy =[0,+1,0,-1]

blocks = []
N, M = map(int,input().split())
for i in range(N):
    blocks.append(list(map(int,input().split())))
visited = [[False]*N for _ in range(N)]
score = 0


def bfs(i,j):
    queue = deque()
    queue.append([i,j])

    block, rainbow = [], []
    block.append([i,j])

    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if blocks[nx][ny] == -1:
                #검정 블록이면 패스
                continue
            if visited[nx][ny] == True:
                continue

            elif blocks[nx][ny] == 0 :
                #무지개 블록이라면 그룹에 추가
                queue.append([nx,ny])
                visited[nx][ny] = True #그룹 블록 체크
                rainbow.append([nx,ny])
            elif blocks[nx][ny] == blocks[i][j]:
                #숫자가 같은(색깔이 같은) 일반 블록이라면 블록그룹에 추가
                queue.append([nx,ny])
                visited[nx][ny] = True  #그룹 블록 체크, 일반 블록 방문처리
                block.append([nx,ny])

    for x, y in rainbow:
        visited[x][y] = False
    
    return [len(rainbow + block), len(rainbow),i,j, block+rainbow]



def gravity():
    for i in range(N-2, -1, -1):  # 밑에서 부터 체크
        for j in range(N):
            if blocks[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0<=r+1<N and blocks[r+1][j] == -2:  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        blocks[r+1][j] = blocks[r][j]
                        blocks[r][j] = -2
                        r += 1
                    else:
                        break

def rotate():
    temp = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            temp[N-c-1][r] = blocks[r][c]

    return temp



while True: 
    g = []
    group = []   #while문 실행마다 블록그룹은 새로 찾아야 하므로, 초기화 필수다
    visited = [[False]*N for _ in range(N)]  #while문 실행마다 블록그룹은 새로 찾아야 하므로, 방문 배열 역시 초기화 필수다


    #크기가 가장 큰 블록 그룹을 찾음
    for i in range(N):
        for j in range(N):
            if 0 < blocks[i][j] and visited[i][j] == False:
                #방문안한 일반 블록일 경우 그룹 찾는 bfs 수행
                visited[i][j] = True
                g = bfs(i,j)
                if g[0] >= 2: 
                    group.append(g)
    #group = sorted(group, key = lambda x: (-x[0],-x[1],-x[2],-x[3]))
    group.sort(reverse=True)

    if len(group) == 0:
        break
    

    score += group[0][0]**2
    #선택된 블록 그룹(group[0])을 맵에서 제거. score 더해줌
    for rm in group[0][4]:  #maxblock 리스트: [x,y]
        blocks[rm[0]][rm[1]] = -2


    #격자에 중력 작용
    gravity()


    #격자 반시계 회전
    blocks = rotate()


    #격자에 중력 작용
    gravity()




print(score)