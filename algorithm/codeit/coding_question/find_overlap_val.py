"""
무수히 많은 숫자들로 구성된 리스트에서 중복되는 값을 리턴하자!
인풋 리스트의 길이가 n이라고 할 때 사전의 크기는 인풋에 비례하는 크기를 갖는다.
이 알고리즘의 공간 복잡도는 O(n)이 된다.
"""



def find_same_number(some_list):
    val_dict = {}
    for i in range(len(some_list)):
        #중복되는 키값이 있나? 있으면 리턴
        if some_list[i] in val_dict.keys():
            return some_list[i]
        #없으면 키값 넣기
        else:
            val_dict[some_list[i]] = 1
            

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
