'''
대체 이 방법을 어떻게 생각하지? 
처음에 용량이 큰 가방순으로 보석을 담아야한다고 생각했는데,  그렇게 하면 큰 용량의 가방부터 보석을 담다가
작은 용량의 가방에는 보석을 담지 못하는 경우가 발생한다. 따라서, 용량이 작은 가방부터 value가 큰 보석을 넣어줘야 한다.
이때, 용량이 작은 가방순으로 담아주기 위해 bag 배열을 한번 정렬해준후, for문을 사용한다.
그후, 
'''
import sys
import heapq

N, K = map(int,sys.stdin.readline().split())
jewel = []   #보석 N개
bag = []     #가방 K개
answer = 0

for i in range(N):
    M, V = map(int,sys.stdin.readline().split())
    heapq.heappush(jewel,[M,V])   #무게 M, 가격 V

for i in range(K):
    C = int(sys.stdin.readline())
    bag.append(C)         #가방에 담을 수 있는 최대 무게 C

bag.sort()



tempjewel = [] 
for capacity in bag:
    while jewel:
        if jewel[0][0] <= capacity:
            m,v = heapq.heappop(jewel)
            heapq.heappush(tempjewel,-v)
        else:
            break
    if tempjewel:
        answer -= heapq.heappop(tempjewel)


print(answer)