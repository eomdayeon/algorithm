from itertools import permutations

def isprime(tmp):
    check = True
    if tmp == 1 or tmp == 0:
        return False
    for i in range(2,tmp):
        if tmp % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    
    numbers = list(numbers)
    numbers_set = set()
    num = []
    result = []

    for i in range(1,len(numbers)+1):           
        num += list(permutations(numbers, i))

        for i in num:       
            tmp = int(''.join(i))
            if tmp not in numbers_set:
                numbers_set.add(tmp)
                if isprime(tmp) == True:
                    answer += 1
            
    return answer

    