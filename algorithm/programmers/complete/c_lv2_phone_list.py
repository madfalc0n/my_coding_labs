#다른사람 풀이(해시맵 이용)
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    print(hash_map)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            print(temp)
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer



#내가푼  방법
# def find(str1,str2):
#     print(str1,str2)
#     len_str1 = len(str1)
#     for i in range(len(str2)-len_str1):
#         if str1 == str2[i:i+len_str1]:
#             print(str1, str2[i:i+len_str1])
#             return 1
#     return 0

# def solution(phone_book):
#     answer = True
#     phone_book.sort(key= lambda x: len(x)) #크기 작은순으로 정렬
#     for i in range(len(phone_book)-1):
#         for j in range(i+1,len(phone_book)):
#             result = find(phone_book[i],phone_book[j])
#             print(i,j)
#             if result: #접두사 있는것으로 판단되면
#                 return False




#     return answer



phone_book = ['123','456','789']
print(solution(phone_book))