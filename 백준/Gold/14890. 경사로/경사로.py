



N, L = map(int,input().split())

road = []
visited = [[False] * N for _ in range(N)]

for i in range(N):
    road.append(list(map(int,input().split())))

high  = []
low = []

count = 0
for i in range(N):
    flag = 0 
    for j in range(N-1):
        high = []
        low = []
        if road[i][j] != road[i][j+1]:
            if road[i][j] > road[i][j+1]:
                hi,hj = i,j
                li,lj = i,j+1
                high.append((hi,hj))
                low.append((li,lj))
            else:
                hi,hj = i,j+1
                li,lj = i,j
                high.append((hi,hj))
                low.append((li,lj))

            if road[hi][hj] - road[li][lj] > 1:
                flag = 1
                continue
            
            dir = ''
            if lj > hj:
                dir = 'right'
            elif lj < hj:
                dir = 'left'

            low.pop()
            ispossible = 1
            if dir == 'right':
                for l in range(1,L+1):
                    nj = hj + l
                    if nj >= N: 
                        ispossible = 0
                        break
                    if visited[i][nj] == True:
                        ispossible = 0
                        break                    
                    if road[i][nj] != road[hi][hj]  - 1:
                        ispossible = 0
                        break
                    else:
                        low.append((i,nj))

            elif dir == 'left':
                for l in range(1,L+1):
                    nj = hj - l
                    if nj < 0: 
                        ispossible = 0
                        break
                    if visited[i][nj] == True:
                        ispossible = 0
                        break                    
                    if road[i][nj] != road[hi][hj]  - 1:
                        ispossible = 0
                        break
                    else:
                        low.append((i,nj))

            if ispossible == 1:
                for v in low:
                    x = v[0]
                    y = v[1]
                    visited[x][y] = True
            else:
                flag = 1

            
        if flag == 1:
            break
    if flag == 0:
        count += 1
        #print(i)
    else:
        for k in range(N):
           visited[i][k] = False            


visited = [[False] * N for _ in range(N)]

for c in range(N):
    flag = 0 
    for r in range(N-1):
        high = []
        low = []
        if road[r][c] != road[r+1][c]:
            if road[r][c] > road[r+1][c]:
                hr,hc = r,c
                lr,lc = r+1,c
                high.append((hr,hc))
                low.append((lr,lc))
            else:
                hr,hc = r+1,c
                lr,lc = r,c
                high.append((hr,hc))
                low.append((lr,lc))

            if road[hr][hc] - road[lr][lc] > 1:
                flag = 1
                continue
            
            dir = ''
            if lr > hr:
                dir = 'down'
            elif lr < hr:
                dir = 'up'

            low.pop()
            ispossible = 1
            if dir == 'down':
                for l in range(1,L+1):
                    nr = hr + l
                    if nr >= N: 
                        ispossible = 0
                        break
                    if visited[nr][c] == True:
                        ispossible = 0
                        break

                    if road[nr][c] != road[hr][hc]  - 1:
                        ispossible = 0
                        break
                    else:
                        low.append((nr,c))

            elif dir == 'up':
                for l in range(1,L+1):
                    nr = hr - l
                    if nr < 0: 
                        ispossible = 0
                        break
                    if visited[nr][c] == True:
                        ispossible = 0
                        break                    
                    if road[nr][c] != road[hr][hc]  - 1:
                        ispossible = 0
                        break
                    else:
                        low.append((nr,c))

            if ispossible == 1:
                for v in low:
                    x = v[0]
                    y = v[1]
                    visited[x][y] = True
            else:
                flag = 1

            
        if flag == 1:
            break
    if flag == 0:
        count += 1
        #print(c)
    else:
        for k in range(N):
           visited[k][c] = False        

    

print(count)
            


# 6 2   #N, L
# 3 2 1 1 2 3
# 3 2 2 1 2 3
# 3 2 2 2 3 3
# 3 3 3 3 3 3
# 3 3 3 3 2 2
# 3 3 3 3 2 2