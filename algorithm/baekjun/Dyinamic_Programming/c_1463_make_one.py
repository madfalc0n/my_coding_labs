"""
1로 만들기 
https://www.acmicpc.net/problem/1463
https://kangmin1012.tistory.com/34
"""

num = int(input())
matrix = [0,0,1,1] # 1, 2, 3 은 각 0, 1, 1 번 소요됨, index는 실제 값이라면 value는 그 값이 소요되는 cost

if num <= 1:
    print(0)
else:
    for i in range(4, num+1):
        tmp_val = matrix[i-1] + 1
        
        if i % 2 == 0:
            tmp_val = min(tmp_val, matrix[i//2] + 1) # +1 하는 이유는 예를들어 3 -> 2로 바뀐다고 가정하면 드는 최소비용이 1이 발생하기 때문
        
        if i % 3 == 0:
            tmp_val = min(tmp_val, matrix[i//3] + 1)
        
        matrix.append(tmp_val)
    print(matrix[-1])