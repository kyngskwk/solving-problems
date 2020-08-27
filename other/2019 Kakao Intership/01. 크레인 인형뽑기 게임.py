def bomb(now):
    global stack, cnt
    stack.append(now)
    if len(stack) == 1:
        return
    else:
        while len(stack) >= 2:
            here = stack.pop()
            front = stack.pop()
            if front == here:
                cnt += 2
            else:
                stack.append(front)
                stack.append(here)
                break


stack = []
cnt = 0
def solution(board, moves):
    global stack, cnt
    new_board = list(map(list, zip(*board)))
    for idx in moves:
        for num in range(len(new_board)):
            if new_board[idx-1][num] > 0:
                now = new_board[idx - 1][num]
                new_board[idx - 1][num] = 0
                bomb(now)
                break
    return cnt
