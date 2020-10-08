def move(dice):
    new_dice = [0, [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]],
                 [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]],
                 [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]],
                 [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]]
    return new_dice


def my_dice(my_map, my_order, x, y):
    result = []
    dice = [0, 0, 0, 0, 0, 0]
    # 1, 2, 3, 4, 5, 6 (idx 0: 맨 위, idx -1: 바닥)

    dx = [0, 0, 0, -1, +1] # 동, 서, 북, 남
    dy = [0, 1, -1, 0, 0]
    for go in my_order:
        x += dx[go]
        y += dy[go]
        my_d = my_map[x][y]
        if my_d == 0:
            dice = move(dice)[go]
            result.append(dice[0])
            my_map[x][y] = dice[-1]
        elif my_d != 0 and my_d != 10:
            dice = move(dice)[go]
            result.append(dice[0])
            dice[-1] = my_map[x][y]
            my_map[x][y] = 0
        elif my_d == 10:
            x -= dx[go]
            y -= dy[go]
    return result



N, M, x, y, K = list(map(int, input().split()))
my_map = [[10 for _ in range(M+2)]] + [10 for _ in range(N)] +[[10 for _ in range(M+2)]]
for i in range(1, N+1):
    my_map[i] = [10] + list(map(int, input().split())) + [10]
my_order = list(map(int, input().split()))
x = x + 1
y = y + 1
print('\n'.join(map(str, my_dice(my_map, my_order, x, y))))
