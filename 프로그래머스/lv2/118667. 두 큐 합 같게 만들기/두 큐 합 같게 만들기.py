from collections import deque


def solution(queue1, queue2):
    answer = -1

    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    cnt, mincnt = 0, len(q1)*4

    while True:
        if cnt == mincnt:
            break

        if sum1 == sum2:
            answer = cnt
            break

        if sum1 > sum2:
            temp = q1.popleft()
            q2.append(temp)
            sum1 -= temp
            sum2 += temp
            cnt += 1
        elif sum2 > sum1:
            temp = q2.popleft()
            q1.append(temp)
            sum2 -= temp
            sum1 += temp    
            cnt += 1       

    # print(answer)

    return answer

# solution([3, 2, 7, 2], [4, 6, 5, 1])