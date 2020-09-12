
"""
코스요리 메뉴는 최소 2가지 이상의 단품메뉴
최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함
"""

def proc(point, orders,num):
    result_list = set()
    for i in orders:
        if num <= len(i):
            tmp_list = sorted(set(point) & set(i))
            if len(tmp_list) <= num:
                result_list.add(''.join(tmp_list))
    return list(result_list)



def solution(orders, course):
    #print(orders)
    result_list = list()
    for i in course:
        for j in range(len(orders)):
            if i <= len(orders[j]):
                tmp_val = orders.pop(j)
                tmp_list = proc(tmp_val, orders,i)
                orders.insert(j,tmp_val)
                result_list.extend(tmp_list)

    #print(sorted(result_list))

    tmp_dict = dict()
    course_dict = dict()
    for i in course:
        course_dict[i] = i
    for i in result_list:
        tmp_len = len(i)
        if 2 <= tmp_len <= 10:
            tmp_dict[i] = tmp_dict.get(i,0) + 1

    tmp_dict = sorted(tmp_dict.items(), key= lambda x: x[1], reverse=True)
    #print(tmp_dict)
    #print(course_dict)
    result_list2 = list()

    for i in tmp_dict:
        tmp_len = len(i[0])
        if course_dict[tmp_len] != 0:
            result_list2.append(i[0])
            course_dict[tmp_len] -= 1
        else:
            continue

    #print(result_list2)


    return sorted(result_list2)



orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD", "AXYZ"]
course = [2,3,4]
print(solution(orders, course))

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))

