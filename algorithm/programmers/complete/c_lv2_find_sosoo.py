"""
소수찾기
https://programmers.co.kr/learn/courses/30/lessons/42839
"""



def recur(numbers, num_list, cur, max_val, tmp_str=''):
    if cur == max_val:
        if int(tmp_str) not in num_list:
            num_list.append(int(tmp_str))
    else:
        for i,d in enumerate(numbers):
            tmp_str += d
            numbers.pop(i)
            recur(numbers, num_list, cur+1, max_val,tmp_str)
            numbers.insert(i,d)
            tmp_str = tmp_str[:-1]

def find_sosoo(num_list):
    result = 0
    for i in num_list:
        if i <= 1:
            continue
        elif i <= 3:
            print(i, end=' ')
            result += 1
            continue
        j = 2
        sw = 0
        while j <= i // j:
            if i % j == 0:
                sw = 1
                break
            j += 1
        if sw == 0:
            print(i, end=' ')
            result += 1
    return result

def solution(numbers):
    numbers = list(numbers)
    print(numbers)
    num_list = list()
    for i in range(1, len(numbers)+1):
        recur(numbers, num_list, 0, i)

    print(num_list)

    return find_sosoo(num_list)


numbers = "123"

print(solution(numbers))