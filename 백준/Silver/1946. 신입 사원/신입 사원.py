import sys
T = int(input())
answer = []

for t in range(T):

    candi = []
    N = int(input())
    for i in range(N):
        document, interview = map(int,sys.stdin.readline().split())
        candi.append([document,interview])

    candi = sorted(candi, key = lambda x: x[0])

    cnt = 1
    max_interview = candi[0][1]
    for idx,i in enumerate(candi):
        if idx == 0:
            continue
        if i[1] < max_interview:
            max_interview = i[1]
            cnt += 1

    answer.append(cnt)

for a in answer:
    print(a) 