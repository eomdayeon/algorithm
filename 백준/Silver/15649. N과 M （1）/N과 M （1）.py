import itertools

N, M = map(int,input().split())
nums =[]

for i in range(N):
    nums.append(i+1)

perm = itertools.permutations(nums,M)

for p in perm:
    for pp in p:
        print(pp,end=' ')
    print()