
u, v = '', ''
answer = ''
right = []
bal = []

def findright(p):
    global u, v, answer, right, bal
    if p[0] == '(':
        if len(v) > 0:
            answer += '('
            for g in list(v)[1:-1]:
                if g == '(':
                    answer += ')'
                else:
                    answer += '('
            answer += ')'
            v = ''

        right.append(p.pop(0))
        u += '('
        while right:
            if p[0] == '(':
                next = p.pop(0)
                right.append(next)
                u += next
            else:
                next = p.pop(0)
                right.pop()
                u += next

    else:
        if len(u) > 0:
            answer += u
            u = ''

        bal.append(p.pop(0))
        v += ')'
        while bal:
            if p[0] == ')':
                next = p.pop(0)
                bal.append(next)
                v += next
            else:
                next = p.pop(0)
                bal.pop()
                v += next

    if len(p) > 0:
        findright(p)


def solution(p):
    global u, v, answer
    p = list(p)
    if len(p) == 0:
        return answer
    findright(p)
    if len(u) > 0:
        answer += u
    else:
        answer += '('
        for g in list(v)[1:-1]:
            if g == '(':
                answer += ')'
            else:
                answer += '('
        answer += ')'
        v = ''

    return answer

print(solution(")()()()("))

u, v = '', ''
# answer = ''
# def solution(p):
#     global u, v, answer
#     p = list(p)
#     right = []
#     bal = []
#     if len(p) == 0:
#         return answer
#
#     if p[0] == '(':
#         right.append(p.pop(0))
#         u += '('
#         while right:
#             if p[0] == '(':
#                 next = p.pop(0)
#                 right.append(next)
#                 u += next
#             else:
#                 next = p.pop(0)
#                 right.pop()
#                 u += next
#
#         answer += u
#         u = ''
#
#     else:
#         bal.append(p.pop(0))
#         v += ')'
#         while bal:
#             if p[0] == ')':
#                 next = p.pop(0)
#                 bal.append(next)
#                 v += next
#             else:
#                 next = p.pop(0)
#                 bal.pop()
#                 v += next
#
#         answer += '('
#         for g in list(v)[1:-1]:
#             if g == '(':
#                 answer += ')'
#             else:
#                 answer += '('
#         answer += ')'
#         v = ''
#
#     if len(p) > 0:
#         solution(p)
#
#     return answer