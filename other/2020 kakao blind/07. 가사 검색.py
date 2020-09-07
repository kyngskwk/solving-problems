def solution(words, queries):
    words = sorted(words, key=len)
    answer = [0] * len(queries)
    word_dict = {}
    q_dict = {}
    start, end, k = 0, 0, len(words[0])
    for idx in range(len(words)):
        if k != len(words[idx]):
            word_dict[k] = (start, end)
            start = idx
            k = len(words[idx])
            end = idx + 1
            if idx == len(words)-1:
                word_dict[k] = (start, end)
        elif idx == len(words) - 1:
            word_dict[k] = (start, end+1)
        else:
            end += 1

    for ind in range(len(queries)):
        q = queries[ind]
        idx_set = word_dict.get(len(q), 0)
        num, ans = 0, 0

        if idx_set != 0:
            if q[-1] == '?':
                num = q.index('?')
                check = q[0:num]
                for idx in range(idx_set[0], idx_set[1]):
                    if words[idx][0:num] == check:
                        ans += 1

            else:
                q = q[::-1]
                num = len(q) - q.index('?')

                check = q[0:num]
                for i in range(idx_set[0], idx_set[1]):
                    if words[i][-1:-1-num:-1] == check:
                        ans += 1

            answer[ind] = ans

    return answer