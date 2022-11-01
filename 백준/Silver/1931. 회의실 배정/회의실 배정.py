
N = int(input())
info = []

for _ in range(N):
    start, end = map(int, input().split())
    info.append([start,end])

info = sorted(info, key = lambda x: (x[1],x[0]))
# print(info)

cnt = 1
curend = info[0][1]
for idx, i in enumerate(info):
    if idx == 0:
        continue
    if i[0]>=curend:
        cnt += 1
        curend = i[1]

print(cnt)
