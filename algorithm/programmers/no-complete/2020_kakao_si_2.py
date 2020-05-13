"""
연산자 우선순위 정해서 가장 높은값 리턴
먼저 연산자만 추출
+, -, * 으로만 되어있다.

"""

from itertools import permutations

def rev_recur(index,expression): #숫자를 문자열로 반환해주는 함수
    if index == 0 or index == len(expression)-1: #처음이거나 마지막일 때
        return expression[index]
    if 48 <= ord(expression[index]) and ord(expression[index]) <= 57:
        result = rev_recur(index-1,expression) + expression[index] 
        return result
    else:
        return ''

def front_recur(index,expression): #숫자를 문자열로 반환해주는 함수
    if index == 0 or index == len(expression)-1: #처음이거나 마지막일 때
        return expression[index]
    if 48 <= ord(expression[index]) and ord(expression[index]) <= 57:
        result = expression[index] + front_recur(index+1,expression)
        return result
    else:
        return ''

def cal(val1,val2,ex_point):
    if ex_point == '+':
        tmp_sum = int(val1) + int(val2)
    elif ex_point == '-':
        tmp_sum = int(val1) - int(val2)
    else: # *일때
        tmp_sum = int(val1) * int(val2)
    return tmp_sum

def solution(expression):

    expression_list = list(permutations(['+','-','*'],3))
    print(expression_list)
    
    result_ex = []
    for expression_sub_list in expression_list:
        tmp_ex = ''
        #[('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'), ('-', '*', '+'), ('*', '+', '-'), ('*', '-', '+')]
        for sub_list in expression_sub_list:#('+', '-', '*')
            print(sub_list)
            expression_point = []
            for i,val in enumerate(expression):
                if val == sub_list:
                    expression_point.append(i)

            for index in expression_point: # '+'에 대한 인덱스값들 리스트

                val1 = rev_recur(index-1,expression)
                val2 = front_recur(index+1,expression)
                val1_index = index - len(val1) 
                val2_index = len(val2) + index
                total_index = expression[val1_index:val2_index+1]
                #print(total_index)
                
                cal_val = cal(val1,val2,expression[index])
                
                #print('cal val:',cal_val)            
                if val2_index == len(expression) -1 : #마지막자리라면?
                    tmp_ex = expression[:val1_index] + str(cal_val)
                elif val1_index == 0: #맨처음일때
                    tmp_ex = str(cal_val) + expression[val2_index+1:]


                print('expression')
                print(tmp_ex)
                result_ex.append([val1_index,val2_index+1])
           
            print('result_ex') 
            print(result_ex)
            
        print(expression)
        break


    answer = 0
    return abs(answer)


expression = "100-200*300-500+20"
print(solution(expression))