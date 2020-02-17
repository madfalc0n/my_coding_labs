key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def solution(key, lock):

    cnt_k= 0 #1의 갯수 
    cnt_l= 0 #0의 갯수

    for i in range(len(key)):
        for j in range(len(key[0])):
            if key[i][j] == 1:
                cnt_k += 1
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if lock[i][j] == 0:
                cnt_l += 1


    print(cnt_k)
    print(cnt_l)

    if cnt_k < cnt_l or cnt_k == 0 : # key 1갯수 < lock 0의 갯수
        return False

    if cnt_l == 1 and cnt_k > 0:
        return True

print(solution(key, lock))

"""
열쇠로 자물쇠를 열수 있으면 True , 없으면 false
key <= lock
key 의 1 갯수가 lock의 0 갯수보다 작으면 false, 같거나 많아야 됨
key 의 1 갯수가 lock의 0 갯수보다 같거나 많으면 True 일 수 있다.
key 의 1 갯수는 움직일 수록 줄어들 수 있다.
 -> lock의 0 갯수가 1일 때 key 의 개수가 1보다 크거나 같을때 무조건 true
예시)


"""

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
a = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	

for i in range(len(key)):
    for j in range(len(key)):
        a[i][j] = key[abs(j-2)][i]


print(a)