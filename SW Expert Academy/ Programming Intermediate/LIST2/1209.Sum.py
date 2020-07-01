import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    pan = [list(map(int, input().split())) for _ in range(100)]
    my_max = 0

    for i in range(100):
        my_sum = 0
        for j in range(100):
            my_sum += pan[j][i]
        my_max = max(my_max, my_sum, sum(pan[i]))

    my_sum1, my_sum2 = 0, 0
    for i, j in zip(range(100), range(100)):
        my_sum1 += pan[i][j]
        my_sum2 += pan[-i-1][-j-1]
        my_max = max(my_max, my_sum1, my_sum2)

    print('#{} {}'.format(tc, my_max))