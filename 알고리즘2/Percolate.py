import random
import math
import statistics

n = 0
t = 0
N = 0
ids = []
size = []  # size[i]: size of tree rooted at i


def root(i):
    while i != ids[i]:
        i = ids[i]
    return i

def connected(p, q):
    return root(p) == root(q)

def union(p, q):
    id1, id2 = root(p), root(q)
    if id1 == id2: return
    if size[id1] <= size[id2]:
        ids[id1] = id2
        size[id2] += size[id1]
    else:
        ids[id2] = id1
        size[id1] += size[id2]


def simulate(n, t):
    global N
    N = n * n
    global ids
    global size
    for idx in range(N):
        ids.append(idx)
        size.append(1)

    count = []
    for time in range(t):

        array = [[0] * n for i in range(n)]

        ids = [idx for idx in range(N)]
        size = [1 for i in range(N)]

        for i in range(2):
            ids.append(N + i)
            size.append(1)

        for i in range(n):
            union(i, N)
            union((n - 1) * n + i, N + 1)

        while True:
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            if array[i][j] == 0:  #close
                array[i][j] = 1  #change open
                #four check
                if i - 1 >= 0 and array[i - 1][j] == 1:  # up
                    union(i * n + j, (i - 1) * n + j)  #union
                if i + 1 < n and array[i + 1][j] == 1:  # down
                    union(i * n + j, (i + 1) * n + j)  #union
                if j - 1 >= 0 and array[i][j - 1] == 1:  # left
                    union(i * n + j, i * n + (j - 1))  #union
                if j + 1 < n and array[i][j + 1] == 1:  # right
                    union(i * n + j, i * n + (j + 1))  #union
            else:
                continue
            if connected(N, N + 1):
                break

        c = 0
        for i in range(n):
            for j in range(n):
                if array[i][j] == 1:
                    c += 1

        count.append(c / N)


    mean = statistics.mean(count)
    stdev = statistics.stdev(count)
    mininterval = mean - (1.96 * stdev / math.sqrt(t))
    maxinterval = mean + (1.96 * stdev / math.sqrt(t))
    print("mean = ", '%.10f' % mean)
    print("stdev    = ", '%.10f' % stdev)
    print("95% confidence interval  =   [", '%.10f'%mininterval, ",   ", '%.10f'%maxinterval,"]")

    return mean, stdev

