"""
피보나치 2 몸풀기
https://www.acmicpc.net/problem/2748
"""

n = int(input())
matrix = [0,1,1]


for i in range(3, n+1):
    tmp_val = matrix[i-1] + matrix[i-2]
    matrix.append(tmp_val)
print(matrix[-1])