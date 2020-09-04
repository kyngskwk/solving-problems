def check(ans):
    for x, y, what in ans:
        if what == 0:
            # 바닥에 있는 경우
            if y == 0:
                continue
            # 아래에 보가 있는 경우
            elif [x, y, 1] in ans or [x - 1, y, 1] in ans:
                continue
            elif [x, y - 1, 0] in ans:
                continue
            else:
                return False

        elif what == 1:
            # 아래에 기둥이 있는 경우
            if [x, y - 1, 0] in ans or [x + 1, y - 1, 0] in ans:
                continue
            # 양 옆에 보가 있는 경우
            elif [x - 1, y, 1] in ans and [x + 1, y, 1] in ans:
                continue
            else:
                return False

    return True

# 보나 기둥을 세울 때
def plus(x, y, what, my_pan):
    if what == 0:
        # 바닥에 있는 경우
        if y == 0:
            return True
        # 아래에 보가 있는 경우
        elif [x, y, 1] in my_pan or [x-1, y, 1] in my_pan:
            return True
        elif [x, y-1, 0] in my_pan:
            return True

    else:
        # 아래에 기둥이 있는 경우
        if [x, y-1, 0] in my_pan or [x+1, y-1, 0] in my_pan:
            return True
        # 양 옆에 보가 있는 경우
        elif [x-1, y, 1] in my_pan and [x+1, y, 1] in my_pan:
            return True
    return False


def minus(x, y, what, my_pan):
    if what == 0:
        # 위에 기둥이 있는 경우
        if [x, y+1, 0] in my_pan:
            return False

        # 위에 보가 있는 경우
        elif [x, y+1, 1] in my_pan:
            if [x-1, y+1, 1] not in my_pan or [x+1, y+1, 1] not in my_pan:
                return False

    else:
        if [x, y-1, 0] in my_pan or [x+1, y-1, 0] in my_pan:
            return True
        # 위에 기둥이 있는 경우
        elif [x+1, y, 0] in my_pan:
            return False
        # 양옆의 보들이 끼어있는 경우
        elif [x-1, y, 1] in my_pan and [x-1, y-1, 0] not in my_pan:
            return False

        elif [x+1, y, 1] in my_pan and [x+2, y-1, 0] not in my_pan:
            return False
    return True


def solution(n, build_frame):
    ans = []
    for x, y, what, how in build_frame:
        # print(x, y, what, how)
        # print(ans)
        if how == 1:
            ans.append([x, y, what])
            if check(ans):
                continue
            else:
                ans.remove([x, y, what])

        elif how == 0:
            ans.remove([x, y, what])
            if check(ans):
                continue
            else:
                ans.append([x, y, what])

    ans.sort()
    return ans

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))