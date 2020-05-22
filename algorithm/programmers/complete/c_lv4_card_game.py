"""
카드게임
한쪽이 빌때 까지 진행
https://programmers.co.kr/learn/courses/30/lessons/42896

1. 언제든지 왼쪽 카드만 통에 버릴 수도 있고 왼쪽 카드와 오른쪽 카드를 둘 다 통에 버릴 수도 있다. 
 이때 얻는 점수는 없다.
 왼쪽은 언제나 상관없이 버릴 수 있다.
 오른쪽이 크면 왼쪽을 버려도 되고 둘다 버려도 되고

2. 오른쪽 카드에 적힌 수가 왼쪽 카드에 적힌 수보다 작은 경우에는 오른쪽 카드만 통에 버릴 수도 있다.  
 오른쪽 카드만 버리는 경우에는 오른쪽 카드에 적힌 수만큼 점수를 얻는다.
 
오른쪽은 왼쪽보다 작은 경우에만 버릴수있다.

3. (1)과 (2)의 규칙에 따라 게임을 진행하다가 어느 쪽 더미든 남은 카드가 없다면 게임이 끝나며 그때까지 얻은 점수의 합이  
 최종 점수가 된다.


"""
def solution(left, right):
    N = len(left)
    matrix = [ [-1] * (N+1) for _ in range(N+1)]
    matrix[0][0] = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != -1:
                if left[i] > right[j]: #왼쪽카드가 오른쪽 카드보다 큰경우
                    matrix[i][j] += right[j]
                    matrix[i][j+1] = max(matrix[i][j], matrix[i][j+1])
                else: # 같거나 작은경우, 다음차례를 위한 준비
                    matrix[i+1][j+1] = max(matrix[i][j], matrix[i+1][j]) # 1,1에 0,0(0) 과 1,0(-1) 중 최대 값
                    matrix[i+1][j] = matrix[i][j] # 1,0에  0,0(0) 값 넣음
    max_val = 0
    for i in range(N):
        max_val = max(max_val, matrix[N-1][i], matrix[i][N-1])
    return max_val




left = [3, 2, 5]
right = [2, 4, 1]
print(solution(left,right))


# #재귀이용, 런타임 에러
# index = {}
# def solution(left, right):
#     global index
#     answer = 0
#     len_l = len(left)
#     len_r = len(right)
#     len_index = str(len_l)+str(len_r)    
#     while True:
#         if len(left) == 0 or len(right) == 0 :
#             return answer
        
#         if index.get(len_index,0) != 0: #메모리에 있는경우
#             return index[len_index]

#         else: #메모리에 없는 경우
#             if left[0] > right[0]:
#                 index[len_index] = right[0] + solution(left,right[1:])
#             elif left[0] <= right[0]:
#                 tmp_answer_1 = solution(left[1:],right[1:]) # 둘다 빼버리는
#                 tmp_answer_2 = solution(left[1:],right) # 왼쪽만 빼버리는
#                 if tmp_answer_1 >  tmp_answer_2:
#                     index[len_index] =tmp_answer_1
#                 else:
#                     index[len_index] =tmp_answer_2
            
#             return index[len_index]
            
#     return answer