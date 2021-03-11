"""
11726 2 x N 타일링
https://www.acmicpc.net/problem/11726

1 : 1, 2 : 2, 3 : 3, 4 : 5, 5 : 8 , 6 : 13
피보나치 방식
"""
num = int(input())
matrix = [0,1,2,3]

if num <= 3:
    print(num)
else:
    for i in range(4, num + 1):
        tmp_val = matrix[i-1] + matrix[i-2]
        matrix.append(tmp_val)

    print(matrix[-1]%10007)