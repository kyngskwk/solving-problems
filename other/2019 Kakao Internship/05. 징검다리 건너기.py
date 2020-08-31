def solution(stones, k):
    my_min = 99999999999999999999999999999
    start = 0
    for idx in range(len(stones) - k + 1):
        my_sum = (max(stones[idx:idx + k]) + min(stones[idx:idx + k]))
        if my_sum < my_min:
            my_min = my_sum
            start = idx

    my_max = max(stones[start:start + k])

    return my_max

def solution(stones, k):
    dict = {}
    length = len(stones)
    # for idx, value in zip(range(length), stones):
    #     dict[idx] = value

    cnt = 0
    while True:
        print(stones)
        for idx in range(length):
            print(idx)
            for key in dict:
                dict[key] += 1
                if dict[key] == k:
                    return cnt

            if stones[idx] != 0:
                stones[idx] -= 1
            else:
                if idx not in dict:
                    dict[idx] = 1
                else:
                    dict[idx] += 1
        cnt += 1


# 이분탐색 알고리즘
def check(stones, k, jump):
    temp = k
    for stone in stones:
        if stone < jump:
            temp -= 1
        else:
            temp = k
        # 각 돌이 예측값 jump보다 작은게 k번 연속으로 나오면
        if temp == 0:
            return False
    return True


def solution(stones, k):
    left = 0
    right = 200000000
    while left <= right:
        jump = (left + right) // 2
        print(left, jump, right)

        canJump = check(stones, k, jump)

        if canJump:
            answer = jump
            left = jump + 1
        else:
            right = jump - 1

    # print(answer)
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))