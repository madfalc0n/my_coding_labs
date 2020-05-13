"""
중간평균값 구하기
1984.

10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.

(소수점 첫째 자리에서 반올림한 정수를 출력한다.)
"""
for i in range(1, int(input())+1):
    list_v = input().split(' ')
    #print(list_v)
    if list_v[-1] == '':
        list_v = list(map(int,list_v[:-1]))
    else:
        list_v = list(map(int,list_v))
    list_v.sort()
    #print(list_v)
    list_sum = round(sum(list_v[1:-1])/8)
    print(f"#{i} {list_sum}")