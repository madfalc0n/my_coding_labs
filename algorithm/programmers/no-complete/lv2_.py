from itertools import combinations

def solution(A,B):
    answer = 0
    min_list = []
    for i in A:
        for j in B:
            min_list.append(i*j)


    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return min_list


A = [1, 2]
B = [3, 4]

print(solution(A,B))