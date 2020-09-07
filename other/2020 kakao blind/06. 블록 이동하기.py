from pprint import pprint
# 가로 상태 / 세로 상태일 경우 x, y변경 해주면 된다.
left_dx = [0, 1, 0, -1, -1, 1, 0, 0]
left_dy = [1, 0, -1, 0, 1, 1, 0, 0]
right_dx = [0, 1, 0, -1, 0, 0, 1, -1]
right_dy = [1, 0, -1, 0, 0, 0, -1, -1]

answer = 999999999999999
def check1(idx, pan, l_x, l_y, r_x, r_y):
    if idx == 4 or idx == 5:
        if sum(pan[l_x][l_y - 1:l_y]) + sum(pan[r_x][r_y - 1:r_y]) != 0:
            return False
    elif idx == 6 or idx == 7:
        if sum(pan[l_x][l_y:l_y + 1]) + sum(pan[r_x][r_y:r_y + 1]) != 0:
            return False
    return True

def check2(idx, pan, left, right):
    if idx == 6 or idx == 5:
        if sum(pan[left[0]][left[1]: left[1] + 1]) + sum(pan[right[0]][right[1]:right[1] + 1]) != 0:
            return False
    elif idx == 4 or idx == 7:
        if sum(pan[left[0]][left[1]-1: left[1]]) + sum(pan[right[0]][right[1]-1:right[1]]) != 0:
            return False
    return True

def move(v, left, right, cnt, pan, N):
    global answer
    # print(cnt)
    if cnt >= answer:
        return

    if left == [N, N] or right == [N, N]:
        print(cnt)
        pprint(v)
        answer = min(answer, cnt)
        return

    else:
        # 가로일 경우
        if left[0] == right[0]:
            if left[1] > right[1]: left[1], right[1] = right[1], left[1]
            for idx in range(8):
                l_x = left[0] + left_dx[idx]
                l_y = left[1] + left_dy[idx]
                r_x = right[0] + right_dx[idx]
                r_y = right[1] + right_dy[idx]
                if check1(idx, pan, l_x, l_y, r_x, r_y):
                    if pan[l_x][l_y] + pan[r_x][r_y] == 0:
                        if v[l_x][l_y] == 0 and v[r_x][r_y] == 0:
                            v[l_x][l_y], v[r_x][r_y] = 1, 1
                            cnt += 1
                            move(v, [l_x, l_y], [r_x, r_y], cnt, pan, N)
                            v[l_x][l_y], v[r_x][r_y] = 0, 0
                            cnt -= 1

                        elif v[l_x][l_y] == 0 and v[r_x][r_y] == 1:
                            v[l_x][l_y] = 1
                            cnt += 1
                            move(v, [l_x, l_y], [r_x, r_y], cnt, pan, N)
                            v[l_x][l_y] = 0
                            cnt -= 1

                        elif v[l_x][l_y] == 1 and v[r_x][r_y] == 0:
                            v[r_x][r_y] = 1
                            cnt += 1
                            move(v, [l_x, l_y], [r_x, r_y], cnt, pan, N)
                            v[r_x][r_y] = 0
                            cnt -= 1

        # 세로일 경우
        elif left[1] == right[1]:
            if left[0] > right[0]: left[0], right[0] = right[0], left[0]
            for idx in range(8):
                l_x = left[0] + left_dy[idx]
                l_y = left[1] + left_dx[idx]
                r_x = right[0] + right_dy[idx]
                r_y = right[1] + right_dx[idx]
                if check2(idx, pan, left, right):
                    if pan[l_x][l_y] + pan[r_x][r_y] == 0:
                        if v[l_x][l_y] == 0 and v[r_x][r_y] == 0:
                            v[l_x][l_y], v[r_x][r_y] = 1, 1
                            cnt += 1
                            move(v, [l_x, l_y], [r_x, r_y], cnt, pan, N)
                            v[l_x][l_y], v[r_x][r_y] = 0, 0
                            cnt -= 1

                        elif v[l_x][l_y] == 0 and v[r_x][r_y] == 1:
                            v[l_x][l_y] = 1
                            cnt += 1
                            # print((l_x, l_y), (r_x, r_y))
                            move(v, [l_x, l_y], [r_x, r_y], cnt, pan, N)
                            v[l_x][l_y] = 0
                            cnt -= 1

                        elif v[l_x][l_y] == 1 and v[r_x][r_y] == 0:
                            v[r_x][r_y] = 1
                            cnt += 1
                            # print((l_x, l_y), (r_x, r_y))
                            move(v, [l_x, l_y], [r_x, r_y], cnt, pan, N)
                            v[r_x][r_y] = 0
                            cnt -= 1



def solution(board):
    global answer
    N = len(board)
    pan = [[1] * (N+2) for _ in range(N+2)]
    for idx in range(N):
        pan[idx+1][1:N+1] = board[idx]
    pprint(pan)
    v = [[0] * (N+2) for _ in range(N+2)]
    v[1][1], v[1][2] = 1, 1
    move(v, [1, 1], [1, 2], 0, pan, N)

    return answer

print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))