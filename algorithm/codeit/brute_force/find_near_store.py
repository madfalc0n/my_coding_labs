# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    len_store = len(coordinates)
    dist = distance(coordinates[0],coordinates[1])
    dist_list = [coordinates[0],coordinates[1]]
    print(dist, dist_list)
    for i in range(len_store-1):
        for j in range(i+1,len_store):
            if i == 0 and j == 1: # 0,1번째 튜플을 썻기 때문에 패스
                pass
            else:
                print(i,j)
                temp_dist = distance(coordinates[i], coordinates[j])
                print(dist, temp_dist)
                if temp_dist < dist : #거리가 가까울 경우
                    dist = temp_dist
                    dist_list = [coordinates[i], coordinates[j]] #매장 저장
    return dist_list

# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))