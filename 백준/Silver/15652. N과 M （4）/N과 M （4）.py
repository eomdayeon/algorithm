
def dfs(start): 
    if len(s) == M:
        for ss in s:
            print(ss,end= ' ')
        print()
        return

    for i in range(start,N+1):
        s.append(i)
        dfs(i)
        s.pop()

N, M = map(int,input().split())
s=[]
dfs(1)


    
#4,2