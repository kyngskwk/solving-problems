def solution(n, weak, dist):
    answer = 9
    gap = 0
    weak_dist = []
    for idx in range(len(weak)):
        if idx < len(weak) - 1:
            gap = weak[idx+1] - weak[idx]
        else:
            gap = (n-weak[idx]) + weak[0]
    # print(weak_dist)
    return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))