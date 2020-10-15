import sys
from collections import deque

sys.stdin = open("input.txt", "r")

N = int(input())
pan = [[-1] + [0] * N + [-1] for _ in range(N)]
pan = [[-1] * (N+2)] + pan + [[-1] * (N+2)]

K = int(input()) # 사과
for _ in range(K):
    i, j = map(int, input().split())
    pan[i][j] = 1

L = int(input())
rot_dict = {}
for idx in range(L):
    x, c = input().split()
    rot_dict[int(x)] = c

dx = [0, 1, 0, -1] # 오, 아래, 왼, 위
dy = [1, 0, -1, 0]

snake = deque([[1, 1]])
cnt = 0

i, j = 1, 1
dir = 0

while True:
    cnt += 1
    i += dx[dir]
    j += dy[dir]

    # 벽을 만나거나 나 자신을 만나거나
    if pan[i][j] == -1 or [i, j] in snake:
        break

    snake.append([i, j])
    # 사과 만나는 경우가 아니면 꼬리 빼준다.
    if pan[i][j] == 0:
        snake.popleft()
    elif pan[i][j] == 1:
        pan[i][j] = 0

    # 방향 설정
    if cnt in rot_dict:
        if rot_dict[cnt] == 'D':
            dir += 1
        else:
            dir -= 1

    if dir > 3:
        dir = 0
    elif dir < 0:
        dir = 3

print(cnt)

