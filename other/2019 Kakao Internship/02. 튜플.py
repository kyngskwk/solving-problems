def solution(s):
    answer = []
    my_list = s.split('{') # 스트링 나눠주기
    new_list = []
    for idx in range(2, len(my_list)):
        item = set(my_list[idx][:-2].split(',')) # 필요한 부분 set 저장
        new_list.append(item)

    order = sorted(new_list, key=len)
    for idx in range(len(order)):
        if idx == 0:
            answer.append(list(order[idx])[0])
        else:
            answer.append(list(order[idx] - set(answer))[0])

    return list(map(int, answer))

print(solution("{{20,111},{111}}"))