stack = []
def find(idx, uv, user_id, banned_id):
    global stack
    if idx == len(banned_id):
        stack.append(uv)
        print(stack)
        # if uv in stack:
        #     print(uv, stack)
        #     return
        # else:
        #     stack += [uv]
        #     print(uv, stack)
        # print(stack)
        return

    else:
        for i in range(len(user_id)):
            if uv[i] == 0 and len(banned_id[idx]) == len(user_id[i]):
                for b, u in zip(banned_id[idx], user_id[i]):
                    if b != '*' and b != u:
                        break

                else:
                    uv[i] = 1
                    find(idx + 1, uv, user_id, banned_id)
                    uv[i] = 0


def solution(user_id, banned_id):
    uv = [0] * len(user_id)

    find(0, uv,  user_id, banned_id)
    return len(stack)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))






# stack = []
# cnt = 0
# def findid(uv, user_id, banned_id, idx):
#     global stack
#     if idx == len(banned_id):
#         if uv not in stack:
#             stack.append(uv)
#             print(stack)
#         return
#
#     else:
#         for i in range(len(user_id)):
#             print(uv)
#             if uv[i] == 0 and len(banned_id[idx]) == len(user_id[i]):
#                 for u, b in zip(user_id[i], banned_id[idx]):
#                     if b != '*' and u != b:
#                         break
#                 else:
#                     uv[i] = 1
#                     findid(uv, user_id, banned_id, idx+1)
#                     uv[i] = 0
#
#
#
# def solution(user_id, banned_id):
#     global bag, cnt
#     uv = [0] * len(user_id)
#     # bv = [0] * len(banned_id)
#
#
#     #
#     # def findid(user_id, banned_id, k):
#     #     global cnt, bag
#     #
#     #     if k == len(banned_id):
#     #         print(uv)
#     #         if uv not in bag:
#     #             # print(bag)
#     #             bag += [uv]
#     #         print(bag)
#     #         cnt += 1
#     #         return
#     #     for idx in range(len(user_id)):
#     #         if uv[idx] == 0 and bv[k] == 0 and len(banned_id[k]) == len(user_id[idx]):
#     #             for u, b in zip(user_id[idx], banned_id[k]):
#     #                 print(u, b)
#     #                 if b != '*' and u != b:
#     #                     break
#     #             else:
#     #                 uv[idx] = 1
#     #                 k += 1
#     #                 findid(user_id, banned_id, k)
#     #                 uv[idx] = 0
#     #                 k -= 1
#     findid(uv, user_id, banned_id, 0)
#     return len(stack)
#
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))