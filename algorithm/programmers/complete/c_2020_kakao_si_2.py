"""
https://programmers.co.kr/learn/courses/30/lessons/67257
연산자 우선순위 정해서 가장 높은값 리턴
먼저 연산자만 추출
+, -, * 으로만 되어있다.

"""
def proc(express, num, expression):
    if num == 2:
        return str(eval(expression))
    else:
        print(express,num,expression)
        if express[num] == '*':
            result = str(eval('*'.join([ proc(express, num + 1, i)  for i in expression.split('*')])))
        elif express[num] == '-':
            result = str(eval('-'.join([ proc(express, num + 1, i)  for i in expression.split('-')])))
        elif express[num] == '+':
            result = str(eval('+'.join([ proc(express, num + 1, i)  for i in expression.split('+')])))
        return result

def solution(expression):
    ex_list = [
        ('*','-','+'),
        ('*','+','-'),
        ('+','-','*'),
        ('+','*','-'),
        ('-','+','*'),
        ('-','*','+')
    ]
    result = 0
    for express in ex_list:
        tmp_result = int(proc(express, 0, expression))
        print(tmp_result)
        result = max(result,abs(tmp_result))

    return result


expression = "100-200*300-500+20"
print(solution(expression))
