import sys

sys.stdin = open('input.txt', 'r')

def card(num_list):
    ans = []
    for i in range(0, len(num_list), 3):
        idx = shape.index(num_list[i])
        cnum = int(num_list[i+1:i+3]) - 1
        if cards[idx][cnum] == 0:
            return 'ERROR'
        cards[idx][cnum] -= 1

    for idx in range(4):
        ans.append(sum(cards[idx]))
    return ' '.join(list(map(str, ans)))


for tc in range(1, int(input())+1):
    cards = [[1]*13 for _ in range(4)]
    shape = ['S', 'D', 'H', 'C']
    num_list = input()
    print('#{} {}'.format(tc, card(num_list)))