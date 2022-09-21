import math

def ccw(i,j,k):
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0]) 
    if area2 > 0: 
        return True
    else: 
        return False


def grahamScan(points):
    
    stack= []
    points = sorted(points, key = lambda p:(p[1],-p[0]))

    px = points[0][0]
    py = points[0][1]

    sortedangle = []

    for i in points:
        if i == 0 : 
            continue
        ax = i[0]
        ay = i[1]

        angle = math.atan2(ay-py, ax-px)
        temp = i + (angle,)
        
        sortedangle.append(temp)

    sortedangle = sorted(sortedangle, key = lambda p:p[2])    


    stack.append(0)
    stack.append(1)
    k = 2

    while k<len(points):
        j = stack.pop()  #second
        i = stack.pop()  #first

        if ccw(sortedangle[i],sortedangle[j],sortedangle[k]) == True:
            #볼록이므로, i-j-k모두 convex hull에 해당
            stack.append(i)  #first
            stack.append(j)  #second
            stack.append(k)   
            k = k+1
        else:
            #오목이므로, j를 제외하고 i-k를 직접 연결
            stack.append(i)
        
    result = [] 
    for i in stack:
        result.append(sortedangle[i][0:2])

    return result

#print(grahamScan([(0,0),(-2,-1),(-1,1),(1,-1),(3,-1),(-3,-1)]))

#print(grahamScan([(4,2),(3,-1),(2,-2),(1,0),(0,2),(0,-2),(-1,1),(-2,-1),(-2,-3),(- 3,3),(-4,0),(-4,-2),(-4,-4)]))
