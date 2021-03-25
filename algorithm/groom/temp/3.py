""""
단지번호 붙이기
https://www.acmicpc.net/problem/2667
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
"""

def bfs(start, info):
    x, y = start[0], start[1]
    result = 0
    for i in range(x,x+info):
        if i > num:
            break
        for j in range(y,y+info):
            if j > num:
                break
            if matrix[i][j] == 0:
                return 0
            else:
                result += 1
    if result == (info*info):
        return 1
    else:
        return 0

num = int(input())
matrix = [[0] * (num + 1) for _ in range(num+1)]
for i in range(1,num+1):
    matrix[i] = [0] + list(map(int,list(input())))

for i in range(len(matrix)):
    print(matrix[i])

info = 1
result_list = []
while True:
    print(f"info : {info}")
    tmp_result = 0
    for i in range(1,num+1):
        for j in range(1,num+1):
            if matrix[i][j] == 1: #방문한 적이 없고
                tmp_result += bfs([i,j],info)

    if tmp_result == 0:
        break
    result_list.append(tmp_result)
    print(f"tmp_result : {tmp_result}")
    info += 1

print(f'total: {sum(result_list)}')
for i in range(len(result_list)):
    print(f"size[{i+1}]: {result_list[i]}")