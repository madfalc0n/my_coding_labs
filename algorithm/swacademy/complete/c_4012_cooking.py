"""
4012 요리사
N개의 식재료가 있다.
식재료들을 각각 N / 2개씩 나누어 두 개의 요리를 하려고 한다. (N은 짝수이다.)
이때, 각각의 음식을 A음식, B음식이라고 하자.

비슷한 맛의 음식을 만들기 위해서는 A음식과 B음식의 맛의 차이가 최소가 되도록 재료를 배분해야 한다.
음식의 맛은 음식을 구성하는 식재료들의 조합에 따라 다르게 된다.

식재료 i는 식재료 j와 같이 요리하게 되면 궁합이 잘 맞아 시너지 Sij가 발생한다. (1 ≤ i ≤ N, 1 ≤ j ≤ N, i ≠ j)
각 음식의 맛은 음식을 구성하는 식재료들로부터 발생하는 시너지 Sij들의 합이다.

식재료 i를 식재료 j와 같이 요리하게 되면 발생하는 시너지 Sij의 정보가 주어지고, 
가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때, 
두 음식 간의 맛의 차이가 최소가 되는 경우를 찾고 그 최솟값을 정답으로 출력하는 프로그램을 작성하라.
"""
from itertools import permutations, combinations


for i in range(1,int(input())+1):
    N = int(input())
    list_v = [ number for number in range(1,N+1)]
    combi_list = []
    combi_list = list(combinations(list_v,N//2))
    #print(combi_list)
    
    #matrix 초기화 및 입력값 받기 
    matrix = [[0] * (N+1) for _ in range(N+1)]
    for n_v  in range(1,N+1):
        list_food_taste = list(input().split(' ') )
        list_food_taste = list(map(int,list_food_taste))
        matrix[n_v][1:] = list_food_taste
  
    min_val = 20001
    combi_element = combi_list.pop(0)
    index = 0 
    while combi_list:
        permutations_1 = list(permutations(combi_element,2)) # 2개씩 묶음
        tmp_val1 = sum(matrix[data[0]][data[1]] for data in permutations_1)
        # tmp_val1 = 0
        # for data in permutations_1:
        #     tmp_val1 += matrix[data[0]][data[1]]

        tmp_set = list(set(list_v) - set(combi_element))
        permutations_2 = list(permutations(tmp_set,2))
        tmp_val2 = sum(matrix[data[0]][data[1]] for data in permutations_2)
        # tmp_val2 = 0
        # for data in permutations_2:
        #     tmp_val2 += matrix[data[0]][data[1]]

        #print(tmp_val1, tmp_val2)
        result = abs(tmp_val1 - tmp_val2)
        #print(f"result : {result}") 
        if min_val > result:
            min_val = result

        combi_element = combi_list.pop(0)
        index += 1

    print(f"#{i} {min_val}")