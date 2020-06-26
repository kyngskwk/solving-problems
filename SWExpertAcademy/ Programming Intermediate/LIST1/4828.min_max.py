import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()

    print('#{} {}'.format(tc, num_list[-1] - num_list[0]))