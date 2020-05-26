def max_profit(price_list, count):
    total_val = [0] * (count+1)
    for i in range(1,count+1):
        profit = 0
        if i == 1 :
            total_val[i] = price_list[i]
            continue

        elif i < len(price_list):
            profit = price_list[i]
            
        else:
            profit = 0

        for j in range(1,(i//2)+1):
                total_val[i] = max(profit, total_val[j]+total_val[i-j])
        

    return total_val[count]


# #답
# def max_profit(price_list, count):
#     # 개수별로 가능한 최대 수익을 저장하는 리스트
#     # 새꼼달꼼 0개면 0원
#     profit_table = [0]

#     # 개수 1부터 count까지 계산하기 위해 반복문
#     for i in range(1, count + 1):
#         # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
#         # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
#         # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정   
#         if i < len(price_list):
#             profit = price_list[i]
#         else:
#             profit = 0

#         # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 찾는다
#         for j in range(1, i // 2 + 1):
#             profit = max(profit, profit_table[j] + profit_table[i - j])

#         profit_table.append(profit)

#     return profit_table[count]


# 테스트
#print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
