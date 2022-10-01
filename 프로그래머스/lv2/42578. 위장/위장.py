def solution(clothes):
    answer = 0
    d = dict()
    
    for c in clothes:
        d.setdefault(c[1], 0)
        d[c[1]]+=1
    
    
    value = 1
    for v in d.values():
        value *= (v+1)



    answer = value-1
    print(answer)
    return answer


# solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])