def solution(prices):
    answer = [0] * len(prices)
    while prices:
        next = prices.pop()
        for idx in range(len(prices)):
            if prices[idx] <= next:
                answer[idx] += 1
            else:
                answer[idx] = 0

    for idx in range(len(answer)-1):
        if answer[idx] == 0:
            answer[idx] += 1

    return answer

print(solution([1, 2, 3, 2, 3]))