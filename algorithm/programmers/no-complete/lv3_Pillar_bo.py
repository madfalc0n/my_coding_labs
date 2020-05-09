def install(background,point,item): #구조물 설치
    x,y = point[0],point[1]
    #기둥 설치
    if item == 0: #기둥 '-'
        if y == 0: #현재위치가 바닥일때
            background[x][y] = '-' 
        
        else: #바닥이 아닐 때
            if background[x][y-1] == '-': # 아래에 기둥이 있을 때
                background[x][y] = '-'

            else: # 기둥이 밑에 없을 때, 보를 체크
                if 1 < x and x <= len(background):
                    if background[x-1][y] == '|': # 위에 보가 있을 때
                        background[x][y] = '-'
    
    elif item == 1: #보 '|'
        if y != 0: #무조건 바닥에 안되고 기둥위에 있어야 함
            if background[x][y-1] == '-': #기둥이 있을 때
                background[x][y] = '|'
            
            else: # 밑에 기둥이 없을 때
                if 1 < x and x < len(background):
                    if background[x-1][y] == '|': # 위에 보가 있을 때
                        background[x][y] = '|'
                    elif background[x+1][y-1] == '-': # 대각선 아래 기둥 있을 떄
                        background[x][y] = '|'


def delete(background,point,item): #구조물 제거
    x,y = point[0],point[1]
    #기둥삭제
    if item == 0:
        if y == 0 : #제일 아래 있을 때
            if x == 0: # 맨 처음일때
                if background[x][y+1] == '|': # 위에 보가 있나?, 있다면 삭제 못함
                    pass

                else: #위에 보가 없다면 삭제가능
                    background[x][y] = 0

            else: # 맨 처음 아닐 때
                if background[x-1][y+1] == '|' and background[x][y+1] == '|':
                    background[x][y] = 0



        



    #보 삭제
    elif item == 1: #보
        pass

def process(background,data):
    x,y = data[0],data[1]
    if data[3] == 0: #삭제
        delete(background,[x,y],data[2])
    else:#설치
        install(background,[x,y],data[2])


def print_want(list):
    print("------list-----")
    for i in list:
        print(i)
    print("------end------")

def solution(n, build_frame):
    background = [[0] * (n+1) for _ in range(n+1)] #0은 빈공간, -은 기둥, |는 보
    print_want(background)
    for data in build_frame:
        process(background,data)
          
    print_want(background)
    




    #결과 
    answer = []
    for i in range(len(background)):
        for j in range(len(background)):
            if background[i][j] != 0:
                print(f"x: {i}, y: {j}, item: {background[i][j]}")
                if background[i][j] == '-': #기둥
                    answer.append([i,j,0])
                elif background[i][j] == '|':
                    
                    answer.append([i,j,1])
    
    return answer


n = 5
#build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1]]
#build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n,build_frame))
