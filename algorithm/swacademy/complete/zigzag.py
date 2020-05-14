"""
1986번 지그재그
"""
for i in range(1,int(input())+1):
    input_num = int(input())
    
    answer = 0
    for num in range(1,input_num+1):
        if num %2 == 0 : #짝수
            answer -= num
        else: #홀수
            answer += num
    print(f"#{i} {answer}")
