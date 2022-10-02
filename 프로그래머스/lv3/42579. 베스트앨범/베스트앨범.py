def solution(genres, plays):
    answer = []
    
    genre_list = dict()
    all = []

    for i, (g,p) in enumerate(zip(genres,plays)):
        all.append((i,g,p))
        genre_list.setdefault(g,0)
        genre_list[g] += p
    # print(all)
    # print(genre_list)


    all = sorted(all, key = lambda x: (x[1],-x[2],x[0]))
    print(all)

    genre_list = sorted(genre_list.items(), key = lambda x: (-x[1]))
    print(genre_list)


    for g in genre_list:
        count = 0
        for i in all:
            if count == 2:
                break
            if i[1] == g[0]:
                answer.append(i[0])
                count += 1
            
    return answer

# solution(["classic", "pop", "classic", "classic", "musical"],[500, 3100, 150, 500, 2500])