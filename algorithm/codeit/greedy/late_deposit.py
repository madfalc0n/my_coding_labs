#지각시간에 따른 벌금내기 코드
def min_fee(pages_to_print):
    result = 0
    pages_to_print = sorted(pages_to_print)
    #print(pages_to_print)
    for i in range(len(pages_to_print)):
        result += pages_to_print[i] * (len(pages_to_print) - i) 
    return result

# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
