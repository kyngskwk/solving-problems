import copy

stack = []
cnt = 0


def findid(user_id, banned_id, k, uv):
    global cnt
    if k == len(banned_id):
        if uv not in stack:
            k = copy.deepcopy(uv)
            stack.append(k)
        return

    for idx in range(len(user_id)):
        if uv[idx] == 0 and len(banned_id[k]) == len(user_id[idx]):
            for u, b in zip(user_id[idx], banned_id[k]):
                if b != '*' and u != b:
                    break
            else:
                uv[idx] = 1
                findid(user_id, banned_id, k + 1, uv)
                uv[idx] = 0


def solution(user_id, banned_id):
    uv = [0] * len(user_id)
    findid(user_id, banned_id, 0, uv)
    return len(stack)