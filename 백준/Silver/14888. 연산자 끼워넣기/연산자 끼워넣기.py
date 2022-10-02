from ast import Return
import sys

input = sys.stdin.readline




def dfs(num,idx,add,sub,mul,div):
    global max_num, min_num, number

    if idx == N:
        max_num = max(max_num,num)
        min_num = min(min_num,num)
        # return

    if add > 0:
        new_num = int(num + number[idx])
        dfs(new_num, idx+1,add-1,sub,mul,div)

    if sub > 0:
        new_num = int(num - number[idx])
        dfs(new_num, idx+1,add,sub-1,mul,div)      

    if mul > 0:
        new_num = int(num * number[idx])
        dfs(new_num, idx+1,add,sub,mul-1,div)      

    if div > 0:
        new_num = int(num / number[idx])
        dfs(new_num, idx+1,add,sub,mul,div-1)  


N = int(input())
number = list(map(int,input().split()))         # 1 2 3 4 5 6  len(number) == 6
add, sub, mul, div = map(int,input().split())   # +, - , x, // ->  2, 1, 1, 1

max_num = int(-1e9)
min_num = int(1e9)
dfs(number[0],1,add,sub,mul,div)

print(max_num)
print(min_num)
# 6
# 1 2 3 4 5 6
# 2 1 1 1