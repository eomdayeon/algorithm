
def dfs(start): 
    if len(s) == M:
        for ss in s:
            print(ss,end= ' ')
        print()

    for i in range(start,N+1):
        if visited[i] == True:
            continue
        visited[i] = True
        s.append(i)
        dfs(i+1)
        s.pop()
        visited[i]=False

N, M = map(int,input().split())
visited= [False] * (N+1)
s=[]
dfs(1)


    
#4,2