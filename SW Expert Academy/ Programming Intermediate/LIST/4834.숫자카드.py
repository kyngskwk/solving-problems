import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    num_list = list(input())

    count_list = [0]*10
    for num in num_list:
        count_list[int(num)] += 1

    max_count = -1
    max_num = -1

    for i in range(10):
        if count_list[i] > max_count:
            max_num = i
            max_count = count_list[i]

        elif count_list[i] == max_count:
            max_num = i
            max_count = count_list[i]

    print('#{} {} {}'.format(tc, max_num, max_count))

