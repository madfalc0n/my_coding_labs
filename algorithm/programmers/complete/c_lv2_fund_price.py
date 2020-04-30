"""
초 간격으로 떨어진 주식가격 출력하기,
주식가격이 떨어지지 않은 시간을 출력하는 것
시간복잡도 중요하다
"""

def solution(prices):
    #print(f"원본 : {prices}")
    len_prices = len(prices)
    answer = []
    queue = 0
    start_num = 0
    end_num = len_prices
    while True:
        if start_num == end_num-1:
            answer.append(0)
            return answer
        tmp_switch = 0 #주식가격 떨어짐 확인용

        for i in range(start_num+1,end_num):
            queue = prices[start_num]
            if queue > prices[i]: #주식가격 떨어질경우 -1로 변환
                #print(queue,i)
                tmp_switch = -1
                answer.append(i-start_num)
                break
        if tmp_switch ==0: #만약 떨어지지 않았다면
            answer.append(len(prices[start_num+1:]))
        start_num += 1

prices = [1, 2, 3, 2, 3]
#result
#[4, 3, 1, 1, 0]

print(solution(prices))