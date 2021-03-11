"""
피보나치
https://www.acmicpc.net/problem/1003
n 호출 시 0과 1 이 각각 몇번나왔는지 출력
"""



tc = int(input())
for i in range(tc):
    m = [[1,0] , [0,1] , [1,1] ]
    n = int(input())
    if n < 3:
        pass
    else: 
        for i in range(3, n+1):
            tmp_val_0 = m[i-1][0] + m[i-2][0]
            tmp_val_1 = m[i-1][1] + m[i-2][1]
            m.append([tmp_val_0,tmp_val_1])
    
    print(f"{m[n][0]} {m[n][1]}")



