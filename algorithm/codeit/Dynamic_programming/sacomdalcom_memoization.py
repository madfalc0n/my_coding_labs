def max_profit_memo(price_list, count, cache):
    
    if count == 1 or 0:
        cache[count] = price_list[count]
        return cache[count]

    else:
        if count not in cache.keys(): #캐시에 해당값이 없는 경우
            if count %2 == 0 : #짝수 일때
                tmp_max = 0
                for i in range(count//2, count):
                    tmp_val = max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count-i, cache)
                    if tmp_max < tmp_val:
                        tmp_max = tmp_val
                cache[count] = tmp_max 
                return cache[count]
            else: #홀수일때
                tmp_max = 0
                for i in range((count//2)+1, count):
                    tmp_val = max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count-i, cache)
                    if tmp_max < tmp_val:
                        tmp_max = tmp_val
                cache[count] = tmp_max                     
                return cache[count]
        else:
            return cache[count]
def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
#print(max_profit([0, 100, 400, 800, 900, 1000], 10))
#print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
