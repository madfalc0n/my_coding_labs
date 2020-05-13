
def solution(arrangement):
    arrangement = arrangement.replace('()','0')
    print(arrangement)
    
    x,cnt = 0,0
    for item in arrangement:
        if item == '(': #막대기 있냐?
            x += 1
            cnt += 1
        elif item == '0':
            cnt += x
        else: # ')' 일 때
            x -= 1
        

    return cnt

arrangement = "()(((()())(())()))(())"
#arrangement = "(()())"
print(solution(arrangement))