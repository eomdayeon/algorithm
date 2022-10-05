n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

def catch_block(s):
    global maps,n
    area = 1
    visited=[[0]*n for _ in range(n)]
    color = maps[s[0]][s[1]]
    blocks = [(s[0],s[1])]
    stack = [s]
    visited[s[0]][s[1]]=1
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    r_b = []
    num_rainbow  = 0
    while(stack):
        cur_x,cur_y =stack.pop()
        for i in range(4):
            nx = cur_x+dx[i]
            ny = cur_y+dy[i]
            if(nx>=n or ny>=n or nx<0 or ny<0):
                continue
            if(visited[nx][ny]==0):
                visited[nx][ny]=1
                if(maps[nx][ny]!='-'):
                    if(maps[nx][ny]==color or maps[nx][ny]==0):
                        if(maps[nx][ny]==0):
                            num_rainbow +=1
                        blocks.append((nx,ny))
                        stack.append((nx,ny))
                        area+=1
    if(area>=2):
        blocks = sorted(blocks,key=lambda x : (x[0],x[1]))
        for i in blocks:
            if(maps[i[0]][i[1]]!=0):
                r_b = [i[0],i[1]]
                break
        return area,blocks,num_rainbow,r_b
    else:
        return 0,[],0,[-1,-1]


def max_area():
    global maps,n

    max_area =0
    b = []
    max_rainbow=-1
    r_b = [-1,-1]
    score =0
    temp_area = 0
    temp_blocks =[]
    temp_rainbow=0
    temp_r_b = [-1,-1]

    for j in range(n):
        for i in range(n):
            if(maps[i][j]!=-1 and maps[i][j]!='-' and maps[i][j]!=0):
                temp_area ,temp_blocks,temp_rainbow,temp_r_b = catch_block((i,j))
                if(temp_area>max_area):
                    max_area=temp_area
                    b=temp_blocks
                    max_rainbow = temp_rainbow
                    r_b = temp_r_b
                elif(temp_area==max_area):
                    if(temp_rainbow>max_rainbow):
                        max_rainbow=temp_rainbow
                        b=temp_blocks
                        max_area = temp_area
                        r_b = temp_r_b
                    elif(temp_rainbow == max_rainbow):
                        if(temp_r_b[0]>r_b[0]):
                            b= temp_blocks
                            #max_area =temp_area
                            #max_rainbow = temp_rainbow
                            r_b = temp_r_b
                        elif(temp_r_b[0]==r_b[0]):
                            if(temp_r_b[1]>r_b[1]):
                                b= temp_blocks
                                #max_area =temp_area
                                #max_rainbow = temp_rainbow
                                r_b = temp_r_b
    for i,j in b:
        maps[i][j]='-'
    score = max_area**2
    return score,b

def show_maps():
    global maps,n
    for i in range(n):
        for j in range(n):
            print(maps[i][j],end='\t')
        print()

def gravity():
    global maps,n
    for j in range(n):
        for i in range(n-1,-1,-1):
            if(maps[i][j]!=-1 and maps[i][j]!='-'):
                cur_val = maps[i][j]
                maps[i][j]='-'
                cur_loc = i
                while(True):
                    if(cur_loc==n-1):
                        maps[cur_loc][j]=cur_val
                        break
                    n_loc = cur_loc+1
                    if(n_loc==n-1):
                        if(maps[n_loc][j]=='-'):
                            maps[n_loc][j]=cur_val
                            break
                        else:
                            maps[cur_loc][j]=cur_val
                            break
                    else:
                        if(maps[n_loc][j]!='-'):
                            maps[cur_loc][j]=cur_val
                            break
                    cur_loc = n_loc


def rotation_mat():
    global maps,n
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[n-j-1][i]=maps[i][j]
    maps = res


ans = 0
while(True):
    temp_score,b = max_area()
    #print(temp_score,b)
    if(temp_score>0):
        ans+= temp_score
    else:
        break
    #show_maps()
    #print()
    gravity()
    #show_maps()
    #print()
    rotation_mat()
    #show_maps()
    #print()
    gravity()
    #show_maps()
    #print()

print(ans)