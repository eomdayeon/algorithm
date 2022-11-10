
from heapq import heappop, heappush
import sys
from collections import deque
N = int(sys.stdin.readline())
info = []

for i in range(N):
    S, T = map(int,sys.stdin.readline().split())
    info.append((S,T))

info.sort()

room = []
heappush(room, info[0][1])  #강의실 종료시간을 PQ에 push

for i in range(1,N):
    if info[i][0] < room[0]:
        #종료시간보다 빠른 경우 새로운 룸이 필요함
        heappush(room, info[i][1])
    else:
        #종료시간보다 늦기 떄문에 기존 룸 사용 가능
        heappop(room)
        heappush(room,info[i][1])

print(len(room))