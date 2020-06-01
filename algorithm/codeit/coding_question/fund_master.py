"""
계속해서 멋진 모습을 보여주기 위해, 
특정 기간 중 수익이 가장 큰 구간을 찾아내는 함수 sublist_max를 작성해 보려고 합니다.

Brute Force 방법을 이용해서 이 문제를 한 번 풀어봅시다!
sublist_max 함수는 profits에서 최대 수익을 내는 구간의 수익을 리턴합니다.

profits가 [7, -3, 4, -8]이라면 무엇을 리턴해야 할까요? profits에서 가장 많은 수익을 낸 구간은 [7, -3, 4]입니다. 
이 구간에서 낸 수익은 8달러이니, 8을 리턴하면 되겠죠!
만약 profits가 [-2, -3, 4, -1, -2, 1, 5, -3]이라면? profits에서 수익이 가장 큰 구간은 [4, -1, -2, 1, 5]입니다. 
이 구간에서 낸 수익은 7달러이니, 7을 리턴하겠죠?
"""

def sublist_max(profits):
    max_sum = 0
    max_index = 0
    for i in range(len(profits)):
        tmp_sum = sum(profits[:i+1])
        if max_sum < tmp_sum:
            max_index = i
            max_sum = tmp_sum
    #print(max_sum)
    #print(profits[:max_index])
    return max_sum
        

# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([4, -1, -2, 1, 5]))
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))