from collections import deque


result = 9999
chicken_idx=[]

# def distance(q):
#     sum = 0
#     while q:
#         temp = []
#         idx = q.popleft()
#         cx, cy = chicken[idx][0], chicken[idx][1]
#         for i in range(N):
#             for j in range(N):
#                 if city[i][j] == 1:
#                     temp.append(abs(cx - i) + abs(cy - j))
#                     sum += min(temp)
#     return sum

def distance(chicken_idx):
    sum = 0
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                temp = []
                for k in chicken_idx:
                    cx = chicken[k][0]
                    cy = chicken[k][1]
                    temp.append(abs(cx - i) + abs(cy - j))
                sum += min(temp)
    return sum


def comb(idx, cnt, M):
    global result, select

    if len(chicken_idx) == M:
        # 치킨 거리 계산해서 작은지 확인한다.
        #print(M, chicken_idx)

        sum = distance(chicken_idx)
        result = min(result, sum)
        return

    for i in range(idx, len(chicken)):
        if select[i] == False:
            select[i] = True
            chicken_idx.append(i)
            comb(i + 1, cnt + 1, M)
            select[i] = False
            chicken_idx.pop()

N, M = map(int, input().split())
city = []

for i in range(N):
    city.append(list(map(int, input().split())))

chicken = []
sum = 0

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))

for m in range(1, M + 1):
    select = [False] * len(chicken)
    comb(0, 0, m)

print(result)


# 0 -> 빈칸, 1-> 집, 2-> 치킨집
# 즉, 2인 것들 중에서 M개를 골라서 도시의 치킨 거리를 계산함.
# => 2(치킨집)의 개수가 K개라 했을 때, K개 중에 M개를 고르는 조합. (이 때, 순서는 고려하지 않는다.)
# 도시의 치킨 거리가 가장 작을 때를 출력함.

