import sys
import copy

sys.stdin = open('input.txt', 'r')

dx = [1, 0, -1, 0] #오, 위, 왼, 아래
dy = [0, -1, 0, 1]

# 드래곤 커브 만들기
def make(temp, d, g, rot):
    i = 0
    while i <= g:
        # 0 세대
        if i == 0:
            next_p = [temp[-1][0] + dx[d], temp[-1][1] + dy[d]]
            temp.append(next_p)
            i += 1

        # 1 세대 이상
        else:
            temp_rot = copy.deepcopy(rot)
            while temp_rot:
                n_d = (temp_rot.pop() + 1) % 4
                x, y = temp[-1][0], temp[-1][1]
                next_p = [x + dx[n_d], y + dy[n_d]]
                temp.append(next_p)
                rot.append(n_d)
            i += 1
    return

# 사각형 찾기
def find(p_list):
    global cnt
    for idx in range(len(p_list)):
        x, y = p_list[idx][0], p_list[idx][1]
        if [x, y] not in cnt:
            if [x-1, y] in p_list and [x, y-1] in p_list and [x-1, y-1] in p_list:
                cnt.append([x, y])


N = int(input())
d_list = [0] * N

for i in range(N):
    d_list[i] = list(map(int, input().split()))

p_list = []
cnt = []
for idx in range(N):
    x, y, d, g = d_list[idx]
    temp = [[x, y]]
    rot = [d]
    make(temp, d, g, rot)
    p_list += temp

find(p_list)
print(len(cnt))