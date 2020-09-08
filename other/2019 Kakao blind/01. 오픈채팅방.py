def solution(record):
    answer = []
    nick = {}
    stack = []
    for words in record:
        word_set = words.split(' ')
        if word_set[0] == 'Enter':
            stack.append((word_set[1], 0))
            nick[word_set[1]] = word_set[2]
        elif word_set[0] == 'Leave':
            stack.append((word_set[1], 1))
        else:
            nick[word_set[1]] = word_set[2]

    for s in stack:
        if s[1]:
            answer.append(nick[s[0]] + "님이 나갔습니다.")
        else:
            answer.append(nick[s[0]] + "님이 들어왔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))