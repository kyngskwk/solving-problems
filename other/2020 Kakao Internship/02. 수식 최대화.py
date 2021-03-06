from itertools import permutations

def solution(expression):
    sign = ['-', '+', '*']
    nums = []
    signset = []
    start = 0
    for idx in range(len(expression)):
        if expression[idx] in sign:
            nums.append(int(expression[start:idx]))
            signset.append(expression[idx])
            start = idx+1
    nums.append(int(expression[start:]))

    my_max = 0
    nums = list(permutations(nums, len(nums)))
    for numset in nums:
        my_sum = numset[0]
        for idx in range(len(signset)):
            if signset[idx] == '*':
                my_sum *= numset[idx+1]
            elif signset[idx] == '+':
                my_sum += numset[idx+1]
            else:
                my_sum -= numset[idx+1]
        my_max = max(my_max, abs(my_sum))

    return my_max


#
#
# def perm(nums, k, N, answer, sign_list):
#     if k == N:
#         sum = nums[0]
#         for idx in range(len(sign_list)):
#             print(idx)
#             if sign_list[idx] == '-':
#                 sum -= nums[idx+1]
#             elif sign_list[idx] == '+':
#                 sum += nums[idx+1]
#             else:
#                 sum *= nums[idx+1]
#         print(sum)
#         answer = max(sum, answer)
#         print(answer)
#
#     else:
#         for i in range(k, N):
#             nums[k], nums[i] = nums[i], nums[k]
#             perm(nums, k + 1, N, answer, sign_list)
#             nums[k], nums[i] = nums[i], nums[k]
#
#
# def solution(expression):
#     input = list(expression)
#     sign = ['-', '+', '*']
#     nums = []
#     num = ''
#     sign_list = []
#     long = len(input)
#
#     answer = 0
#
#     for idx in range(long):
#         now = input.pop(0)
#         if now in sign:
#             nums.append(num)
#             sign_list.append(now)
#             num = ''
#         elif len(input) == 0:
#             num += now
#             nums.append(num)
#             num = ' '
#         else:
#             num += now
#     print(sign_list)
#     nums = list(map(int, nums))
#     perm(nums, 0, len(nums), answer, sign_list)
#     return answer

print(solution("50*6-3*2"))