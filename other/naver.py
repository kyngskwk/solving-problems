cnt = 0
def find:



def solution(A):
    default = A
    after = A
    for i in range(len(after)-1, 0, -1):
        for j in range(0, i):
            if after[j] > after[j+1]:
                after[j], after[j+1] = after[j+1], after[j]

    for i in range(len(after)):
