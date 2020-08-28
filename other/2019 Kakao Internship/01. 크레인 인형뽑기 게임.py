def solution(board, moves):
    stack = []
    cnt = 0
    length = len(board)
    for idx in moves:
        for num in range(length):
            if board[num][idx-1] > 0:
                stack.append(board[num][idx-1])
                board[num][idx-1] = 0
                if len(stack) >= 2:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        cnt += 2
                break
    return cnt
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))