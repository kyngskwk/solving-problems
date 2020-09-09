def solution(food_times, k):
    length = len(food_times)
    food_dict = {}
    food_sort = []

    for idx in range(len(food_times)):
        food_dict[idx + 1] = food_times[idx]

    food_sort = sorted(food_dict.items(), key=lambda item: item[1])

    idx = 0
    mins = food_sort[idx][1] * length
    # 어떤 접시가 0개가 될 때 까지 최대바퀴를 한번에 뺌
    while mins <= k:
        now_min = food_sort[idx][1]  # 현재 min 값
        k -= mins
        cnt = food_times.count(now_min)
        idx += cnt
        length -= cnt  # 남은 접시의 수

        if length <= 0:
            return -1

        mins = (food_sort[idx][1] - now_min) * length  # 그 다음 작은 값으로 반복

    food_sort = sorted(food_sort[idx:], key=lambda x: x[0])

    if k == 0:
        return food_sort[0][0]

    elif k < len(food_sort):
        return food_sort[k][0]

    else:
        final = k % len(food_sort)
        return food_sort[final][0]

print(solution([3,1,1,1,2,4,3], 12))

