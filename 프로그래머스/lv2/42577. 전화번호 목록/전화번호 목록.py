def solution(phone_book):
    answer = True
    

    phone_book.sort()

    for i in range(len(phone_book)-1):
        if not phone_book[i+1].startswith(phone_book[i]):
            continue
        for j in range(i+1,len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                answer = False
                break
    print(answer)
    return answer


# solution(["12","123","1235","567","88"])