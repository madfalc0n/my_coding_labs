"""
3
1 3 1 2
10 2 6 4
1 1

2
1 3 1 2
10 2
4

4
1 3 1 2
10 2 6 4
1 1 10 9

"""

N = int(input())
matrix = [ [0] * 4 for _ in range(N) ]
for i in range(N): 
    matrix[i] = list(map(int, input().split()))


result = min(matrix[0][0] + matrix[1][0], matrix[0][0] + matrix[0][2] + matrix[1][1] , 
                matrix[0][1] + matrix[1][1], matrix[0][1] + matrix[0][3] + matrix[1][0])
for i in range(1, N-1):
    result += min(matrix[i+1][0] ,matrix[i][2] + matrix[i+1][1] , 
            matrix[i+1][1], matrix[i][3] + matrix[i+1][0])
print(result)