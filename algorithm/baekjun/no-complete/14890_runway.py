"""
경사로
https://www.acmicpc.net/problem/14890
2:07 시작
"""
N, L = list(map(int,input().split()))
matrix = [list(map(int,input().split())) for _ in range(N)]
# print(N,L)
# for i in matrix:
#     print(i)

#총 가능한 다리 개수
# result = 2*N
result = []

# 생성 불가능한 다리 개수
bridge_list = []

for i in range(N):
    tmp_set = set()
    tmp_list = []
    max_val = 0
    for j in range(N):
        tmp_set.add(matrix[i][j])
        tmp_list.append(matrix[i][j])
        max_val = max(max_val, matrix[i][j])
    if len(tmp_set) != 1:
        bridge_list.append(tmp_list)
    result.append(tmp_list)

for i in range(N):
    tmp_set = set()
    tmp_list = []
    max_val = 0
    for j in range(N):
        tmp_set.add(matrix[j][i])
        tmp_list.append(matrix[j][i])
        max_val = max(max_val, matrix[j][i])
    if len(tmp_set) != 1:
        bridge_list.append(tmp_list)
    result.append(tmp_list)

# print(bridge_list)
no_list = []
for br in bridge_list:
    i = 0
    while i < (len(br)-1):
        if abs(br[i]-br[i+1]) > 1:
            no_list.append(br)
            break
        elif abs(br[i]-br[i+1]) == 1: # 높낮이 차이가 1 난다면?
            if br[i] < br[i+1]: #뒤에 놈이 큰경우
                if i-L+1 in range(N):
                    tmp_bool = True
                    for j in range(i-L+1, i):
                        if br[i] != br[j]:
                            tmp_bool = False
                            break
                    if tmp_bool == False: #서로 높이 다를 경우
                        no_list.append(br)
                        break
                else:# 범위에서 벗어나면 탈락
                    no_list.append(br)
                    break
                i += 1

            else: #앞에놈이 큰경우
                if i+L in range(N):
                    tmp_bool = True
                    for j in range(i+1, i+L+1):
                        if br[i+1] != br[j]:
                            tmp_bool = False
                            break
                    if tmp_bool == False: #서로 높이 다를 경우
                        no_list.append(br)
                        break
                else: # 범위에서 벗어나면 탈락
                    no_list.append(br)
                    break
                i += (L + 1) 
        else:
            i += 1
# print(no_list)
for no in no_list:
    if no in result:
        result.pop(result.index(no))

print(result)

