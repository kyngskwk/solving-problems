# def solution(begin, target, words):
#     answer = 0
#     visited = [0] * len(words)
#
#     def dfs(begin, target, words, k):
#         global answer
#
#         if begin == target:
#             answer = k
#             return
#         else:
#             for word in words:
#                 cnt = 0
#                 for w in word:
#                     if w not in begin:
#                         cnt += 1
#                 if cnt == 1:
#                     dfs(word, target, words, k)
#
#     if target not in words:
#         return answer
#     else:
#         dfs(begin, target, words, 0)
#
#     return answer
answer = 0


def dfs(begin, target, words, visited):
    global answer
    stack = [begin]

    while stack:
        next = stack.pop()

        if next == target:
            return answer

        for idx in range(0, len(words)):
            cnt = 0
            for w in words[idx]:
                if w not in next: cnt += 1

            if cnt == 1 and visited[idx] == 0:
                visited[idx] = 1
                stack.append(words[idx])

        answer += 1


def solution(begin, target, words):
    global answer
    if target not in words:
        return 0

    visited = [0] * len(words)

    dfs(begin, target, words, visited)
    return answer


print(solution("hit", "cog", ["hot", "dot", "lot", "log", "dog", "cog"]))