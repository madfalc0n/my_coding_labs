def trapping_rain(buildings):
    rain_cnt = 0
    for i,val in enumerate(buildings):
        if i == 0:
            continue
        if i == len(buildings)-1:
            break
        #print(i)
        rain_val = min(max(buildings[:i]) , max(buildings[i+1:]))
        if rain_val > val: #왼쪽, 오른쪽 각 최대값에서 min 값이 자신값보다 클 경우
            rain_cnt += rain_val - val
    
    return rain_cnt


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))