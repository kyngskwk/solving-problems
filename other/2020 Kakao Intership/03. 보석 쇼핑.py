# # 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
# # 가장 짧은 구간의 시작 번호대와 끝번호 때
# # 만약 가짱 짧은 구간이 여러개 -> 시작 진열이 가장 작은 구간 return
#


def solution(gems):
    size = len(set(gems))
    dic = {gems[0]:1}
    temp = [0, len(gems) - 1]
    start, end = 0, 0

    while(start < len(gems) and end < len(gems)):
        if len(dic) == size:
            if end - start < temp[1] - temp[0]:
                temp = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1

        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] in dic.keys():
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1

    return [temp[0]+1, temp[1]+1]

# def solution(gems):
#     # 1. 보석 종류를 파악한다.
#     type = {}
#     for gem in set(gems):
#         type[gem] = 0
#     nums = len(type)
#
#     my_min = 999999999
#     my_max = 0
#
#     # 2. 있는 보석이면 갱신, 없는 보석이면 넣어주기
#     # 3. 대신 보석의 종류가 다 찼다 -> 구매확정
#     cnt = 0
#     for idx in range(len(gems)):
#         if type[gems[idx]] == 0:
#             cnt += 1
#             type[gems[idx]] = idx + 1
#         else:
#             type[gems[idx]] = idx + 1
#
#         if cnt == nums:
#             my_max = idx + 1
#             break
#
#     for idx in type.values():
#         my_min = min(idx, my_min)
#
#     answer = [my_min, my_max]
#     return answer
#
# def solution(gems):
#     # 1. 보석 종류를 파악한다.
#     # type = set(gems)
#     nums = len(set(gems))
#
#     start = 0
#     end = 1
#     while(1):
#         if len(set(gems[start:end])) == nums:
#             if end - start == nums:
#                 break
#             elif len(set(gems[start+1:end])) != nums:
#                 break
#             else:
#                 start += 1
#         else:
#             end += 1
#
#     # 2. 있는 보석이면 갱신, 없는 보석이면 넣어주기
#     # 3. 대신 보석의 종류가 다 찼다 -> 구매확정
#     # cnt = 0
#     # for idx in range(len(gems)):
#     #     if type[gems[idx]] == 0:
#     #         cnt += 1
#     #         type[gems[idx]] = idx + 1
#     #     else:
#     #         type[gems[idx]] = idx + 1
#     #
#     #     if cnt == nums:
#     #         break
#     #
#     # my_min = 9999999999
#     # my_max = 0
#     # for idx in type.values():
#     #     my_min = min(idx, my_min)
#     #     my_max = max(idx, my_max)
#
#     answer = [start+1, end]
#     return answer
#
# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))