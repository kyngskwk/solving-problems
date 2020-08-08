numbers = [1, 1, 1, 1, 1]
target = 3
answer = 0

def dfs(numbers, target, sum, k, end):
    global answer
    if k == end:
        if sum == target:
            answer += 1
            return
    else:
        sum = sum + (-1 * numbers[k])
        dfs(numbers, target, sum, k + 1, end)
        sum = sum + (2 * numbers[k])
        dfs(numbers, target, sum, k + 1, end)


def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0, len(numbers))
    return answer


print(solution([1, 1, 1, 1, 1], 3))