import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    max_num = 0
    min_num = 9999999999999
    for i in range(0, N-M+1):
        my_sum = sum(num_list[i:i+M])
        max_num = max(max_num, my_sum)
        min_num = min(min_num, my_sum)

    print('#{} {}'.format(tc, max_num-min_num))