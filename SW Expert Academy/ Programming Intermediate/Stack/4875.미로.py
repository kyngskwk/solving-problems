import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

# 재귀로 풀
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def find_way(pan, i, j):
    global visited, ans
    if pan[i][j] == 3:
        ans = 1
        return

    else:
        for way in range(4):
            next_i = i + dx[way]
            next_j = j + dy[way]
            if pan[next_i][next_j] != 1 and visited[next_i][next_j] == 0:
                visited[next_i][next_j] = 1
                find_way(pan, next_i, next_j)
                visited[next_i][next_j] = 0



for tc in range(1, int(input())+1):
    N = int(input())
    pan = [[0]*N for _ in range(N)]
    for i in range(N):
        pan[i] = [1] + list(map(int, list(input()))) + [1]
    pan = [[1]*(N+2)] + pan + [[1]*(N+2)]
    visited = [[0] * (N+2) for _ in range(N + 2)]
    ans = 0

    i, j = 0, 0
    for idx in range(N+2):
        for idx2 in range(N+2):
            if pan[idx][idx2] == 2:
                i, j = idx, idx2
                visited[i][j] = 1
                break
    find_way(pan, i, j)
    print('#{} {}'.format(tc, ans))기

# stack

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def my_way(my_map):
    visited = [[0 for _ in range(N+2)] for _ in range(N+2)]
    stack = []

    for i in range(N+2):
        for j in range(N+2):
            if my_map[i][j] == 2:
                stack.append((i, j))
                break

    while len(stack) > 0:
        r, c = stack.pop(-1)
        if visited[r][c] != 1:
            visited[r][c] = 1
            if my_map[r][c] == 3:
                return 1

            for k in range(4):
                wr = r + dx[k]
                wc = c + dy[k]
                if visited[wr][wc] != 1 and my_map[wr][wc] != 1:
                    stack.append((wr, wc))
    return 0

TC = int(input())
for i in range(TC):
    N = int(input())
    my_map = [[1 for _ in range(N+2)] for _ in range(N+2)]
    n_list = [0 for _ in range(N)]
    for k in range(N):
        n_list[k] = input()

    for x in range(1, N+1):
        for y in range(1, N+1):
            my_map[x][y] = int(n_list[x-1][y-1])

    print('#{} {}'.format(i+1, my_way(my_map)))
