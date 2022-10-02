
def dfs():
    if len(s) == M:
        for num in s:
            print(num, end = ' ')
        print()
        
    for i in range(1,N+1):
        if visited[i] == True:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False

N, M = map(int,input().split())
s =[]
visited=[False] * (N+1)

dfs()

