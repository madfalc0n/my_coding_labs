"""
피보나치 2 몸풀기
https://www.acmicpc.net/problem/2748
"""

n = int(input())
matrix = [0] + [1  for _ in range(n)]


for i in range(2, n+1):
    matrix[i] = matrix[i-1] + matrix[i-2]
# print(matrix)
print(matrix[n])


# def recur(n):
#     global val_dict

#     if n <= 1:
#         return n
    
#     else:
#         if val_dict.get(n,None) == None:
#             val_dict[n] = recur(n-1) + recur(n-2)
#         return val_dict[n]

# n = int(input())

# val_dict = {
#     0 : 0,
#     1 : 1
# }

# print(recur(n))

    
    