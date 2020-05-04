base_list ='0123456789ABCDEF'
def find_num_base(num, base):
    q,r  = divmod(num,base) #몫,나머지
    if q == 0:
        return base_list[r]
    n_v = base_list[r]
    return find_num_base(q,base) + n_v

def solution(n, t, m, p):
    answer = ''
    result_answer = ''
    turn = p #순서
    p -= 1 # 인덱스가 0부터 시작이므로 미리 빼줌
    for i in range(0,t*m): #0부터 시작
        value = find_num_base(i,n)
        #print(value)
        answer += value
        if len(answer) == t*m:
            break
    for i,d in enumerate(answer):
        if len(result_answer) == t:
            break
        if i % m == p:
            result_answer += d

    return result_answer

n = 16 #진법
t = 20 #미리구할 숫자개수
m = 2 # 사람수
p = 1 #튜브 순서

print(solution(n,t,m,p))