"""
투자 귀재 규식이 2
divide and conquer 방식을 사용하여 풀어보자! 
**분할과 정복**이라는 뜻으로 문제를 단번에 알아내기 어려울 경우 부분 부분으로 나누어 푸는 방법론이다. 
이는 총 3단계로 나뉘는데 `Divide(분할)`, `Conquer(정복)`, `Combine(결합)`으로 나뉜다.
1. `Divide(분할)`는 하나의 복잡한 문제를 부분적으로 분할한다는  의미이다.
2. `Conquer(정복)`은 부분적으로 분할된 문제들의 답을 도출한다는 의미이다.
3. `Combine(결합)`은 도출된 답들을 모두 결합하여 기존 문제를 해결 한다는 의미이다.
"""

def sublist_max(profits, start, end):
    # 코드를 작성하세요. 
    if start == end:
        return profits[start]


    mid = (start + end)//2

    return 


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))