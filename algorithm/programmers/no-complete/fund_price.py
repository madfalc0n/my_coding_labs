

def solution(prices):
    #print(f"원본 : {prices}")
    answer = []
    queue = 0
    while True:
        if len(prices) == 1:
            answer.append(0)
            return answer 
        
        queue = prices.pop(0)
        i = 0
        for n in prices:
            




    return answer

prices = [1, 2, 3, 2, 3]
#result
#[4, 3, 1, 1, 0]

print(solution(prices))