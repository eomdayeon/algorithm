def solution(answers):
    result = []
    
    one = 0
    two = 0
    three = 0
    
    count = [0,0,0,0]
    
    for i in range(len(answers)):
        if i % 8 == 1:
            two = 1
        elif i % 8 == 3:
            two = 3
        elif i % 8 == 5:
            two = 4
        elif i % 8  == 7:
            two = 5
        else : 
            two = 2
        
        if i % 5 == 0:
            one = 1
        elif i % 5 ==1:
            one = 2
        elif i % 5 ==2:
            one = 3
        elif i % 5 ==3:
            one = 4
        elif i % 5 == 4:
            one = 5
            
            
        if i % 10 == 0 or i % 10 == 1:
            three = 3
        elif i % 10 == 2 or i % 10 == 3:
            three = 1
        elif i % 10 == 4 or i % 10 == 5:
            three = 2            
        elif i % 10 == 6 or i % 10 == 7:
            three = 4
        elif i % 10 == 8 or i % 10 == 9:
            three = 5
            
        if answers[i] == one:
            count[1] += 1
        if answers[i] == two:
            count[2] += 1
        if answers[i] == three:
            count[3] += 1
            
    #result.append(count.index(max(count)))
    
    m = max(count)
    for i in range(4):
        if count[i] == m:
            result.append(i)
    
    
    result.sort
    
    
    return result