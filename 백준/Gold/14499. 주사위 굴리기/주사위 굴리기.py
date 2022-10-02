import sys
input = sys.stdin.readline

def up():
    tmp = dice[0][1]
    dice[0][1] = dice[1][1]
    dice[1][1] = dice[2][1]
    dice[2][1] =  dice[3][1]
    dice[3][1] = tmp

def down():
    tmp = dice[3][1]
    dice[3][1] = dice[2][1]
    dice[2][1] = dice[1][1]
    dice[1][1] =  dice[0][1]
    dice[0][1] = tmp


def left():
    tmp = dice[1][0]
    dice[1][0] = dice[1][1]
    dice[1][1] = dice[1][2]
    dice[1][2] =  dice[3][1]
    dice[3][1] = tmp

def right():
    tmp = dice[1][2]
    dice[1][2] = dice[1][1]
    dice[1][1] = dice[1][0]
    dice[1][0] =  dice[3][1]
    dice[3][1] = tmp


N, M, x, y, K = map(int,input().split())

maps =[]
move = []
dc = [0,+1,-1, 0, 0]  #1: 동, 2:서 ,3: 북, 4: 남
dr = [0, 0, 0,-1,+1]
dice = [[0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]]

# dice = [[0]*3 for _ in range(4)]
answer = []

for i in range(N):
        maps.append(list(map(int,input().split())))

move = list(map(int,input().split()))

for m in move:
    nx = x + dr[m]
    ny = y + dc[m]
    if nx<0 or ny<0 or nx>=N or ny>=M:
        continue


    if m == 1:
        right()
    elif m == 2:
        left()
    elif m == 3:
        up()
    elif m == 4:
        down()

    if maps[nx][ny] != 0:
        #이동하게 되는 칸 위치가 0이 아니라면, 주사위 바닥면에 maps에 적힌 숫자를 복사 그리고 맵의 칸에는 0으로 바꿈
        dice[3][1] = maps[nx][ny]
        maps[nx][ny] = 0

    elif maps[nx][ny] == 0:
        #이동하게 되는 칸이 0이라면, 주사위 바닥면에 아무런 일도 일어나지 않고 맵에 주사위 바닥면을 복사
        maps[nx][ny] = dice[3][1]
        
    x = nx
    y = ny
    answer.append(dice[1][1])
    
for a in answer:
    print(a)
# print(answer)


# 4 2 0 0 8
# 0 2
# 3 4
# 5 6
# 7 8
# 4 4 4 1 3 3 3 2