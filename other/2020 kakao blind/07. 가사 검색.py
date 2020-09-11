from collections import defaultdict

def make_trie(trie, word):
    now = trie # {len(word): {}} 이 상태로 시작
    word = list(word)
    while word:
        w = word[0]
        now.setdefault(w, [0, {}]) # w가 dict안에 존재하지 않으면 w:[0, {}] 값으로 할당
        now[w][0] += 1 # [0, {}]의 숫자에 +1 -> 경우의 수를 더해주는 의미
        now = now[w][1] # [0, {}] 의 {}가 now가 되면서 가지를 치는 형식
        word.pop(0)

def find(trie, query):
    cnt = 0
    now = trie
    if len(trie) == 0:
        return 0

    query = list(query)
    while query:
        if query[0] == '?': # '?'를 만나면 cnt를 return
            return cnt

        else:
            if query[0] not in now: # 값이 없으면 0을 return
                return 0
            cnt = now[query[0]][0] # 경우의 수가 cnt가 된다.
            now = now[query[0]][1] # 아래의 dict, 가지로 이동
        query.pop(0)
    return cnt

def solution(words, queries):
    ans = []
    # 키에 대한 값을 주지 않으면 `키 : {}` 이상태로 시작하겠다는 말
    trie = defaultdict(dict)
    rev_trie = defaultdict(dict)
    # 키에 대한 값을 주지 않으면 `키 : 0` 이상태로 시작
    len_dict = defaultdict(int)

    for word in words:
        make_trie(trie[len(word)], word)
        make_trie(rev_trie[len(word)], word[::-1])
        len_dict[len(word)] += 1 # 전체가 ???? 인 경우를 생각해서 len dict도 만든다.

    for q in queries:
        if q[0] == '?' and q[-1] == '?':
            ans.append(len_dict[len(q)])
        elif q[-1] == '?':
            ans.append(find(trie[len(q)], q))
        else:
            ans.append(find(rev_trie[len(q)], q[::-1]))

    # print(trie, len_dict)
    return ans

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))

# def solution(words, queries):
#     words = sorted(words, key=len)
#     answer = [0] * len(queries)
#     word_dict = {}
#     start, end, k = 0, 0, len(words[0])
#     for idx in range(len(words)):
#         if k != len(words[idx]):
#             word_dict[k] = (start, end)
#             start = idx
#             k = len(words[idx])
#             end = idx + 1
#             if idx == len(words)-1:
#                 word_dict[k] = (start, end)
#         elif idx == len(words) - 1:
#             word_dict[k] = (start, end+1)
#         else:
#             end += 1
#
#     for ind in range(len(queries)):
#         q = queries[ind]
#         idx_set = word_dict.get(len(q), 0)
#         num, ans = 0, 0
#
#         if idx_set != 0:
#             if q[-1] == '?':
#                 num = q.index('?')
#                 check = q[0:num]
#                 for idx in range(idx_set[0], idx_set[1]):
#                     if words[idx][0:num] == check:
#                         ans += 1
#
#             else:
#                 q = q[::-1]
#                 num = q.index('?')
#                 check = q[0:num]
#                 for i in range(idx_set[0], idx_set[1]):
#                     if words[i][-1:-1-num:-1] == check:
#                         ans += 1
#
#             answer[ind] = ans
#
#     return answer