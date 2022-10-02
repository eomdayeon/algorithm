
def dfs(): 
    if len(s) == M:
        for ss in s:
            print(ss,end= ' ')
        print()
        return

    for i in range(1,N+1):
        s.append(i)
        dfs()
        s.pop()

N, M = map(int,input().split())
visited= [False] * (N+1)
s=[]
dfs()


    
#4,2