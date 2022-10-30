check = False

def solution(places):
    answer = []

    dr = [-1,0,1,0]
    dc = [0,-1,0,+1]
    def dfs(arr,r,c,visited,cnt,flag):
        global check
        if cnt >= 2:
            if flag == True:
                check = True
                return True
            return

        if flag == True:
            check = True
            return

        visited[r][c] = True
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr<0 or nc<0 or nc>=5 or nr>=5:
                continue
            if not visited[nr][nc] and arr[nr][nc] != 'X':
                visited[nr][nc] = True
                if arr[nr][nc] == 'P':
                    flag = True
                dfs(arr,nr,nc,visited,cnt+1,flag)
                visited[nr][nc] = False
                    

    def manhatten(room):
        global check
        visited = [[False] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':  #응시자가 앉아있다면
                    check = False
                    dfs(room,i,j,visited,0,False)
                    if check == True:
                        return False
        return True


    for room in places:
        if manhatten(room) == True:
            answer.append(1)
        elif manhatten(room) == False:
            answer.append(0)


    # print(answer)
    return answer

# solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])