import sys
sys.stdin = open("input.txt", "r")


def findmin(points, idx, k, dist):
    global my_min, visited, N
    if k == N:
        # 집까지 거리
        dist += abs(points[1][0] - points[idx][0]) + abs(points[1][1] - points[idx][1])
        my_min = min(my_min, dist)
        return

    for i in range(2, N+2):
        next = dist + abs(points[idx][0] - points[i][0]) + abs(points[idx][1] - points[i][1])
        if visited[i] == 0 and my_min > next:
            visited[i] = 1
            findmin(points, i, k+1, next)
            visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))
    points = [[0, 0] for _ in range(N+2)]
    for num in range(N+2):
        points[num][0] = nums[2*num]
        points[num][1] = nums[2*num + 1]

    visited = [0] * (N+2)
    my_min = 9999999999999999
    for idx in range(2, N+2):
        # 회사부터 거리
        dist = abs(points[0][0] - points[idx][0]) + abs(points[0][1] - points[idx][1])
        if my_min > dist:
            visited[idx] = 1
            findmin(points, idx, 1, dist)
            visited[idx] = 0

    print('#{} {}'.format(tc, my_min))
