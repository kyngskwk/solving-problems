def solution(new_id):
    answer = ''
    ok = ['-', '_', '.']
    for word in new_id:
        if word.isalpha():
            answer += word.lower()
        elif word.isdigit() or word in ok:
            if word == '.':
                if len(answer) == 0 or answer[-1] == '.':
                    continue
                else:
                    answer += word
            else:
                answer += word

    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]

    if len(answer) == 0:
        answer += 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    elif len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer

print(solution("z-+.^."))