from itertools import combinations

def check(now, other):
    for idx in range(len(now)):
        if now[idx] not in other:
            return False
    return True

def solution(orders, course):
    answer = []
    orders = sorted(orders, key=len)

    while course:
        max = 0
        temp = []
        num = course.pop(0)
        for idx in range(len(orders)):
            if len(orders[idx]) >= num:
                for i in range(len(orders[idx:])):
                    temp_order = list(combinations(orders[idx+i], num))

                    for now in temp_order:
                        now = sorted(now)
                        if now in temp:
                            continue
                        else:
                            cnt = 0
                            for other in orders[idx:]:
                                if check(now, other):
                                    cnt += 1

                            if cnt >= 2:
                                if max == 0 or cnt == max:
                                    max = cnt
                                    cnt = 0
                                    temp += [now]

                                elif cnt > max:
                                    max = cnt
                                    cnt = 0
                                    temp = [now]

                answer += temp
                break

    answer = ["".join(a) for a in sorted(answer)]
    return answer

print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))





        #
        #
        #         now = orders[idx]
        #         cnt = 1
        #         for other in orders[idx + 1:]:
        #             if check(now, other):
        #                 cnt += 1
        #
        #         if cnt >= 2:
        #             print(temp)
        #             if max == 0 or cnt == max:
        #                 cnt = 1
        #                 temp += [now]
        #             elif cnt > max:
        #                 temp = [now]
        #
        #
        # for idx in range(len(orders)):
        #     if len(orders[idx]) == num:
        #         for order in orders[idx:]:
        #             d = list(combinations(order, num))
        #             for
        #             now = orders[idx]
        #             cnt = 1
        #             for other in orders[idx+1:]:
        #                 if check(now, other):
        #                     cnt += 1
        #
        #             if cnt >= 2:
        #                 print(temp)
        #                 if max == 0 or cnt == max:
        #                     cnt = 1
        #                     temp += [now]
        #                 elif cnt > max:
        #                     temp = [now]

            # else:
            #     orders = orders[idx:]
            #     answer += temp
            #     break

#     answer = sorted(answer)
#     return answer
#
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))