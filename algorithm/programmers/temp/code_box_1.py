
import collections

def solution(p):
    p += 1
    while True:
        list_p = list(str(p))
        cnt_p = collections.Counter(list_p)
        if len(cnt_p) == 4:
            return p
        else:
            p += 1

p = 1987
print(solution(p))