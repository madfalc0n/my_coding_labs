"""
줄기세포 배양
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo&categoryId=AWXRJ8EKe48DFAUo&categoryType=CODE
18:32 시작
텀있음
21:28 종료
도움 https://hongsj36.github.io/2020/02/24/SWEA_5653/
"""
def pr(list):
    for i in list:
        print(i)

tc = int(input())
for case in range(1,tc+1):
    n,m,k = list(map(int,input().split()))

    #줄기세포 생명력수치는 1~ 10까지
    cell_list = ['stats'] + [[] for _ in range(10)]
    # print(cell_list)   

    #매트릭스 증축, k만큼 
    matrix = [list(map(int,input().split())) + ([0] * k) for _ in range(n)] + [[0] * (m+k) for _ in range(k)] 
    
    cell_uni = set()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                power = matrix[i][j]
                cell_list[power] += [[i,j,power]]
                cell_uni.add(power)
    # print(cell_list)
    cell_uni = sorted(cell_uni, reverse=True)
    
    dx,dy = [1,-1,0,0],[0,0,1,-1]    
    for _ in range(k):
        for cell_index in cell_uni:
            new_list = []
            old_list = []
            cells = cell_list[cell_index]
            power = cell_index
            for cell_index2 in range(len(cells)-1, -1,-1):
                cells[cell_index2][2] -= 1 #hp상태 업데이트
                x,y,hp = cells[cell_index2]
                if hp == -1: #활성 상태 중 1시간 뒤 세포 복제
                    for i in range(4):
                        # 해당 영역들 내로 좌표가 잡힘
                        nx = (x + dx[i]) % (n+k) # -1이 될 경우 n+k -1 로
                        ny = (y + dy[i]) % (m+k)
                        if matrix[nx][ny] == 0: # 빈 영역일 경우, 추가
                            new_list.append([nx,ny,power])
                            matrix[nx][ny] = power                
                if hp == power * (-1):#해당 생명력수치 시간만큼 감소, 죽음상태
                    old_list.append(cell_index2)
            for old in old_list:
                cells.pop(old)
            cells += new_list


    # print(cell_list)
    result = 0
    for i in range(1,11):
        for cell in cell_list[i]:
            result += 1
    print(f"#{case} {result}")