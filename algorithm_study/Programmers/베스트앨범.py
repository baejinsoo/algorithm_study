def solution(genres, plays):
    answer = []
    hashmap = {}
    for i in range(len(genres)):
        if genres[i] not in hashmap:
            hashmap[genres[i]] = [(plays[i], i)]
        elif genres[i] in hashmap:
            hashmap[genres[i]].append((plays[i], i))

    genres_list = []
    for key in hashmap.keys():
        add = 0
        for value in hashmap[key]:
            v, index = value
            add += v
        genres_list.append((add, key))
    genres_list.sort(reverse=True)
    # print(genres_list)
    for genres in genres_list:
        count, genre = genres
        plays_lists = hashmap[genre]
        plays_lists.sort(key = lambda x: (-x[0], x[1]))
        print(plays_lists)
        if len(plays_lists) >= 2:
            for i in range(2):
                answer.append(plays_lists[i][1])
        else:
            answer.append(plays_lists[0][1])
    return answer


genres = ['classic', 'pop', 'classic','pop', 'classic', 'classic']
plays = [400, 600, 150, 600, 500, 500]
print(solution(genres, plays))
