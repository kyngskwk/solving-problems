def solution(A, B):
    stack = []
    cnt = 0
    for idx in range(len(A)):
        if B[idx] == 1:
            stack.append(A[idx])
        else:
            if len(stack) == 0:
                cnt += 1
            else:
                for i in range(len(stack)):
                    fish = stack.pop()
                    if A[idx] < fish:
                        stack.append(fish)
                        break
                else:
                    cnt += 1

    cnt += len(stack)
    return cnt

print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))