"""
미래를 보는 능력으로 사재기를 하고자 한다. 단, 다음조건이 있다.
    1. 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
    2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
    3. 판매는 얼마든지 할 수 있다.
"""
for index in range(1,int(input())+1):
    number = int(input())
    test_list = list(map(int, input().split(' ')))

    test_list_len = len(test_list)
    buy_list = 0
    my_sum = 0
    for _ in range(test_list_len):
        max_val = max(test_list)
        if test_list[0] < max_val: # 작으면 사야지이~
            buy_list += 1
            my_sum -= test_list[0]
        else: # 크거나 같다?
            if buy_list != 0: #이미 모아둔게 있으므로 팔아야지~
                my_sum += buy_list*test_list[0]
                buy_list = 0
            else: #모아둔게 없는데 바로앞에 큰거있다? 안사~
                pass
        test_list.pop(0)
    print(f"#{index} {my_sum}")

