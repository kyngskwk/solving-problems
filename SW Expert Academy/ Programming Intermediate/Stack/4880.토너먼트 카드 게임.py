import sys

sys.stdin = open('input.txt', 'r')

def whoWin(a, b):
    res = 0

    # b가 이기는 경우만 체크
    if a == 1 and b == 2:
        res = 1
    elif a == 2 and b == 3:
        res = 1
    elif a == 3 and b == 1:
        res = 1

    return res

def torGame(start, end):
    if start == end:
        return start
    if start+1 == end:
        if whoWin(cards[start], cards[end]):
            return end
        else:
            return start

    half = (start + end)//2
    win1 = torGame(start, half)
    win2 = torGame(half+1, end)
    if whoWin(cards[win1], cards[win2]):
        return win2
    else:
        return win1



for tc in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))
    print('#{} {}'.format(tc, torGame(0, N - 1) + 1))